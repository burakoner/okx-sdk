import hmac
import base64
from . import constants as c


def sign(message, secret):
    mac = hmac.new(bytes(secret, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)


def pre_hash(timestamp, method, request_path, body, debug=True):
    if debug:
        print('body: ', body)
    return str(timestamp) + str.upper(method) + request_path + body


def get_header(api_key, signature, timestamp, pass_phrase, simulation, debug):
    header = dict()
    header[c.CONTENT_TYPE] = c.APPLICATION_JSON
    header[c.OK_ACCESS_KEY] = api_key
    header[c.OK_ACCESS_SIGN] = signature
    header[c.OK_ACCESS_TIMESTAMP] = str(timestamp)
    header[c.OK_ACCESS_PASSPHRASE] = pass_phrase
    if simulation:
        header['x-simulated-trading'] = '1'
    if debug:
        print('header: ', header)
    return header


def get_header_no_sign(simulation, debug):
    header = dict()
    header[c.CONTENT_TYPE] = c.APPLICATION_JSON
    if simulation:
        header['x-simulated-trading'] = '1'
    if debug:
        print('header: ', header)
    return header


def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        if value != '':
            url = url + str(key) + '=' + str(value) + '&'
    url = url[0:-1]
    return url

def signature(timestamp, method, request_path, body, secret_key):
    if str(body) == '{}' or str(body) == 'None':
        body = ''
    message = str(timestamp) + str.upper(method) + request_path + str(body)

    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()

    return base64.b64encode(d)
