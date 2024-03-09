import base64
import hmac
import json
import time
import requests

def init_login_params(apikey, apisecret, passphrase, use_server_time: bool):
    timestamp = local_time()
    if use_server_time:
        timestamp = server_time()
    message = str(timestamp) + 'GET' + '/users/self/verify'
    mac = hmac.new(bytes(apisecret, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    sign = base64.b64encode(d)
    arg = {"apiKey": apikey, "passphrase": passphrase, "timestamp": timestamp, "sign": sign.decode("utf-8")}
    payload = {"op": "login", "args": [arg]}
    return json.dumps(payload)

def is_not_blank_str(param: str) -> bool:
    return param is not None and isinstance(param, str) and (~param.isspace())

def get_param_key(arg: dict) -> str:
    s = ""
    for k in arg:
        if k == 'channel':
            continue
        s = s + "@" + arg.get(k)
    return s

def init_subscribe_set(arg: dict) -> set:
    paramsSet = set()
    if arg is None:
        return paramsSet
    elif isinstance(arg, dict):
        paramsSet.add(get_param_key(arg))
        return paramsSet
    else:
        raise ValueError("arg must dict")

def check_socket_params(args: list, channelArgs, channelParamMap):
    for arg in args:
        channel = arg['channel'].strip()
        if ~is_not_blank_str(channel):
            raise ValueError("channel must not none")
        argSet = channelParamMap.get(channel, set())
        argKey = get_param_key(arg)
        if argKey in argSet:
            continue
        else:
            validParams = init_subscribe_set(arg)
        if len(validParams) < 1:
            continue
        p = {}
        for k in arg:
            p[k.strip()] = arg.get(k).strip()
        channelParamMap[channel] = channelParamMap.get(channel, set()) | validParams
        if channel not in channelArgs:
            channelArgs[channel] = []
        channelArgs[channel].append(p)

def server_time():
    url = "https://www.okx.com/api/v5/public/time"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data'][0]['ts']
    else:
        return ""

def local_time():
    return int(time.time())
