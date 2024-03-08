from .BaseClient import OkxBaseClient
from ..constants import *


class SignalTradingClient(OkxBaseClient):
    def __init__(self, api_key='', api_secret_key='', pass_phrase='', use_server_time=False, simulation=False,
                 domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, api_key, api_secret_key, pass_phrase, use_server_time, simulation, domain, debug,
                               proxy)
