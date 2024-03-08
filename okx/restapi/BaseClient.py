import json
import datetime
from httpx import Client

from ..constants import *
from .. import exceptions
from .. import utils


class OkxBaseClient(Client):

    def __init__(self, apikey='', apisecret='', passphrase='', 
                 use_server_time=False, simulation=False, base_api=API_URL, debug=False, proxy=None):
        super().__init__(base_url=base_api, http2=True, proxy=proxy)
        self.API_KEY = apikey
        self.API_SECRET_KEY = apisecret
        self.PASS_PHRASE = passphrase
        self.use_server_time = use_server_time
        self.simulation = simulation
        self.domain = base_api
        self.debug = debug

    def _request(self, method, request_path, params=None):
        if params is None:
            params = {}

        if method == GET:
            request_path = request_path + utils.parse_params_to_str(params)

        timestamp = self.local_time()
        if self.use_server_time:
            timestamp = self.server_time()

        body = json.dumps(params) if method == POST else ""

        if self.API_KEY != '' and self.API_SECRET_KEY != '':
            signature = utils.sign(utils.pre_hash(timestamp, method, request_path, str(body), self.debug),
                                   self.API_SECRET_KEY)
            header = utils.get_header(self.API_KEY, signature, timestamp, self.PASS_PHRASE, self.simulation, self.debug)
        else:
            header = utils.get_header_no_sign(self.simulation, self.debug)

        response = None
        if self.debug:
            print('domain:', self.domain)
            print('url:', request_path)
        if method == GET:
            response = self.get(request_path, headers=header)
        elif method == POST:
            response = self.post(request_path, data=body, headers=header)
        return response.json()

    def server_time(self):
        request_path = API_URL + SYSTEM_TIME
        response = self.get(request_path)
        if response.status_code == 200:
            return response.json()['data'][0]['ts']
        else:
            return ""

    def local_time(self):
        now = datetime.datetime.utcnow()
        t = now.isoformat("T", "milliseconds")
        return t + "Z"
