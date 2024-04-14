from .BaseClient import OkxBaseClient
from ..constants import *


class NonDisclosedBrokerClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase,
                               use_server_time, simulation, domain, debug, proxy)

    def get_broker_info(self):
        return self._request(GET, BROKER_ND_INFO)

    def create_subaccount(self, subAcct='', label=''):
        params = {
            'subAcct': subAcct,
            'label': label
        }
        return self._request(POST, BROKER_ND_CREATE_SUBACCOUNT, params)

    def delete_subaccount(self, subAcct=''):
        params = {
            'subAcct': subAcct
        }
        return self._request(POST, BROKER_ND_DELETE_SUBACCOUNT, params)

    def get_subaccount_info(self, subAcct='', page='', limit=''):
        params = {
            'subAcct': subAcct,
            'page': page,
            'limit': limit
        }
        return self._request(GET, BROKER_ND_SUBACCOUNT_INFO, params)

    def create_subaccount_apikey(self, subAcct='', label='', passphrase='', ip='', perm=''):
        params = {
            'subAcct': subAcct,
            'label': label,
            'passphrase': passphrase,
            'ip': ip,
            'perm': perm
        }
        return self._request(POST, BROKER_ND_CREATE_APIKEY, params)

    def get_subaccount_apikey(self, subAcct='', apiKey=''):
        params = {
            'subAcct': subAcct,
            'apiKey': apiKey
        }
        return self._request(GET, BROKER_ND_SELECT_APIKEY, params)

    def reset_subaccount_apikey(self, subAcct='', apiKey='', label='', perm='', ip=''):
        params = {
            'subAcct': subAcct,
            'apiKey': apiKey,
            'label': label,
            'perm': perm,
            'ip': ip
        }
        return self._request(POST, BROKER_ND_MODIFY_APIKEY, params)

    def delete_subaccount_apikey(self, subAcct='', apiKey=''):
        params = {
            'subAcct': subAcct,
            'apiKey': apiKey
        }
        return self._request(POST, BROKER_ND_DELETE_APIKEY, params)

    def set_subaccount_level(self, subAcct='', acctLv=''):
        params = {
            'subAcct': subAcct,
            'acctLv': acctLv
        }
        return self._request(POST, BROKER_ND_SET_SUBACCOUNT_LEVEL, params)

    def set_subaccount_fee_rate(self, subAcct='', instType='', chgType='', chgTaker='', chgMaker='', effDate=''):
        params = {
            'subAcct': subAcct,
            'instType': instType,
            'chgType': chgType,
            'chgTaker': chgTaker,
            'chgMaker': chgMaker,
            'effDate': effDate
        }
        return self._request(POST, BROKER_ND_SET_SUBACCOUNT_FEE_RATE, params)

    def create_subaccount_deposit_address(self, subAcct='', ccy='', chain='', addrType='', to=''):
        params = {
            'subAcct': subAcct,
            'ccy': ccy,
            'chain': chain,
            'addrType': addrType,
            'to': to
        }
        return self._request(POST, BROKER_ND_SUBACCOUNT_DEPOSIT_ADDRESS, params)

    def reset_subaccount_deposit_address(self, subAcct='', ccy='', chain='', addr='', to=''):
        params = {
            'subAcct': subAcct,
            'ccy': ccy,
            'chain': chain,
            'addr': addr,
            'to': to
        }
        return self._request(POST, BROKER_ND_MODIFY_SUBACCOUNT_DEPOSIT_ADDRESS, params)

    def get_subaccount_deposit_address(self, subAcct='', ccy=''):
        params = {
            'subAcct': subAcct,
            'ccy': ccy
        }
        return self._request(GET, BROKER_ND_SUBACCOUNT_DEPOSIT_ADDRESS, params)

    def get_subaccount_deposit_history(self, subAcct='', ccy='', txId='', state='', after='', before='', limit=''):
        params = {
            'subAcct': subAcct,
            'ccy': ccy,
            'txId': txId,
            'state': state,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, BROKER_ND_SUBACCOUNT_DEPOSIT_HISTORY, params)

    def get_subaccount_withdrawal_history(self, subAcct='', ccy='', wdId='', clientId='', txId='', type='', state='', before='', limit=''):
        params = {
            'subAcct': subAcct,
            'ccy': ccy,
            'wdId': wdId,
            'clientId': clientId,
            'txId': txId,
            'type': type,
            'state': state,
            'before': before,
            'limit': limit
        }
        return self._request(GET, BROKER_ND_SUBACCOUNT_WITHDRAWAL_HISTORY, params)

    def get_rebate_daily(self, subAcct='', begin='', end='', page='', limit=''):
        params = {
            'subAcct': subAcct,
            'begin': begin,
            'end': end,
            'page': page,
            'limit': limit
        }
        return self._request(GET, BROKER_ND_REBATE_DAILY, params)

    def get_rebate_details_download_link(self, type='', begin='', end=''):
        params = {
            'type': type,
            'begin': begin,
            'end': end
        }
        return self._request(GET, BROKER_ND_GET_REBATE_PER_ORDERS, params)

    def generate_rebate_details_download_link(self, begin='', end=''):
        params = {
            'begin': begin,
            'end': end
        }
        return self._request(POST, BROKER_ND_GEN_REBATE_PER_ORDERS, params)

    def get_dcd_products(self, ccy, alternativeCcy, optType, tag):
        params = { 'ccy': ccy, 'alternativeCcy': alternativeCcy, 'optType': optType, 'tag': tag }
        return self._request(GET, FINANCE_SFP_DCD_PRODUCTS, params)

    def request_dcd_quote(self, notional, notionalCcy, productId, tag, markUp='', clReqId=''):
        params = { 'notional': notional, 'notionalCcy': notionalCcy, 'productId': productId, 'tag': tag, 'markUp': markUp, 'clReqId': clReqId }
        return self._request(POST, FINANCE_SFP_DCD_QUOTE, params)

    def exec_dcd_order(self, quoteId, clReqId=''):
        params = { 'quoteId': quoteId, 'clReqId': clReqId }
        return self._request(GET, FINANCE_SFP_DCD_ORDER, params)

    def get_dcd_order(self, ordId='', clReqId=''):
        params = { 'ordId': ordId, 'clReqId': clReqId }
        return self._request(GET, FINANCE_SFP_DCD_ORDER, params)

    def get_dcd_orders(self, productId='', uly='', state='', beginId='', endId='', begin='', end='', limit=''):
        params = { 'productId': productId, 'uly': uly, 'state': state, 'beginId': beginId, 'endId': endId, 'begin': begin, 'end': end, 'limit': limit }
        return self._request(GET, FINANCE_SFP_DCD_ORDERS, params)

    def set_subaccount_asset(self, subAcct, ccy):
        params = { 'subAcct': subAcct, 'ccy': ccy}
        return self._request(POST, BROKER_ND_SET_SUBACCOUNT_ASSETS, params)
    
    def report_subaccount_ip(self, subAcct, clientIP):
        params = { 'subAcct': subAcct, 'clientIP': clientIP}
        return self._request(POST, BROKER_ND_REPORT_SUBACCOUNT_IP, params)

    def get_rebate_info(self, apiKey='', uid='', subAcct=''):
        params = { 'apiKey': apiKey, 'uid': uid, 'subAcct': subAcct }
        return self._request(GET, BROKER_ND_IF_REBATE, params)

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
