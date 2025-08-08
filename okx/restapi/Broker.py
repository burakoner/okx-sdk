from .BaseClient import OkxBaseClient
from ..constants import *


class DmaBrokerClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase,
                               use_server_time, simulation, domain, debug, proxy)

    def get_subaccount_list(self, subAcct='', uid='', page='', limit=''):
        params = {
            'subAcct': subAcct,
            'uid': uid,
            'page': page,
            'limit': limit
        }
        return self._request(GET, BROKER_DMA_SUBACCOUNT_INFO, params)

    def get_subaccount_fee_rates(self, subAcct='', uid='', page='', limit=''):
        params = {
            'subAcct': subAcct,
            'uid': uid,
            'page': page,
            'limit': limit
        }
        return self._request(GET, BROKER_DMA_SUBACCOUNT_TRADE_FEE, params)

    def create_subaccount_apikey(self, subAcct, label, passphrase, ip='', perm=''):
        params = {
            'subAcct': subAcct,
            'label': label,
            'passphrase': passphrase,
            'ip': ip,
            'perm': perm
        }
        return self._request(POST, BROKER_DMA_ADD_SUBACCOUNT_APIKEY, params)

    def get_subaccount_apikey(self, subAcct, apiKey=''):
        params = {
            'subAcct': subAcct,
            'apiKey': apiKey,
        }
        return self._request(GET, BROKER_DMA_GET_SUBACCOUNT_APIKEY, params)

    def get_trading_data_link(self, type, begin='', end=''):
        params = {
            'type': type,
            'begin': begin,
            'end': end
        }
        return self._request(GET, BROKER_DMA_REBATE_PER_ORDERS, params)

    def generate_trades_download_link(self,  begin='', end=''):
        params = {
            'begin': begin,
            'end': end
        }
        return self._request(POST, BROKER_DMA_TRADES, params)

class FullyDisclosedBrokerClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='', use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    def get_rebate_details_download_link(self, type='', begin='', end=''):
        params = {'type': type, 'begin': begin, 'end': end}
        return self._request(GET, BROKER_FD_GET_REBATE_PER_ORDERS, params)

    def generate_rebate_details_download_link(self, begin='', end=''):
        params = {'begin': begin, 'end': end}
        return self._request(POST, BROKER_FD_GEN_REBATE_PER_ORDERS, params)

    def get_users_broker_rebate_information(self, apiKey, brokerType):
        params = {'apiKey': apiKey, 'brokerType': brokerType}
        return self._request(GET, BROKER_FD_IF_REBATE, params)
