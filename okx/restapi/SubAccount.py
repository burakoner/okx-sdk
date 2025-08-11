from .BaseClient import OkxBaseClient
from ..constants import *


class SubAccountClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    # Get sub-account list
    def get_subaccounts(self, enable='', subAcct='', after='', before='', limit=''):
        params = {'enable': enable, 'subAcct': subAcct, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, USERS_SUBACCOUNT_LIST, params)
    
    # Create sub-account
    def create_subaccount(self, subAcct, type, label='', pwd=''):
        params = {'subAcct': subAcct, 'type': type, 'label': label, 'pwd': pwd}
        return self._request(POST, USERS_SUBACCOUNT_CREATE, params)
    
    # Create an API Key for a sub-account
    def create_apikey(self, subAcct, label, passphrase, perm='', ip=''):
        params = {'subAcct': subAcct, 'label': label, 'passphrase': passphrase}
        if perm != '':
            params['perm'] = perm
        if ip != '':
            params['ip'] = ip
        return self._request(POST, USERS_SUBACCOUNT_APIKEY_CREATE, params)
    
    # Query the API Key of a sub-account
    def get_apikey(self, subAcct, apiKey=''):
        params = {'subAcct': subAcct, 'apiKey': apiKey}
        return self._request(GET, USERS_SUBACCOUNT_APIKEY_QUERY, params)

    # Reset the API Key of a sub-account
    def set_apikey(self, subAcct, apiKey, label='', perm='', ip=''):
        params = {'subAcct': subAcct, 'apiKey': apiKey}

        if ip != '':
            params['ip'] = ip
        if label != '':
            params['label'] = label
        if perm != '':
            params['perm'] = perm
        return self._request(POST, USERS_SUBACCOUNT_MODIFY_APIKEY, params)
    
    # Delete the API Key of sub-accounts
    def delete_apikey(self, subAcct, apiKey):
        params = {'subAcct': subAcct, 'apiKey': apiKey}
        return self._request(POST, USERS_SUBACCOUNT_DELETE_APIKEY, params)

    # Get sub-account trading balance
    def get_trading_balance(self, subAcct):
        params = {"subAcct": subAcct}
        return self._request(GET, ACCOUNT_SUBACCOUNT_BALANCES, params)

    # Get sub-account funding balance
    def get_funding_balance(self, subAcct='', ccy=''):
        params = {
            'subAcct': subAcct,
            'ccy': ccy
        }
        return self._request(GET, ASSET_SUBACCOUNT_BALANCES, params)

    # Get sub-account maximum withdrawals
    def get_max_withdrawal(self, subAcct, ccy=''):
        params = {
            'subAcct': subAcct,
            'ccy': ccy
        }
        return self._request(GET, ACCOUNT_SUBACCOUNT_MAX_WITHDRAWAL, params)

    # Get history of sub-account transfer
    def get_transfer_history(self, ccy='', type='', subAcct='', after='', before='', limit=''):
        params = {"ccy": ccy, 'type': type, 'subAcct': subAcct, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, ASSET_SUBACCOUNT_BILLS, params)

    # Get history of managed sub-account transfer
    def get_managed_transfer_history(self, ccy='', type='', subAcct='', subUid='', after='', before='', limit=''):
        params = {"ccy": ccy, 'type': type, 'subAcct': subAcct, 'subUid': subUid, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, ASSET_SUBACCOUNT_MANAGED_SUBACCOUNT_BILLS, params)

    # Master accounts manage the transfers between sub-accounts
    def transfer(self, ccy, amt, from_, to, fromSubAccount, toSubAccount, loanTrans='false', omitPosRisk='false'):
        params = {'ccy': ccy, 'amt': amt, 'from': from_, 'to': to, 'fromSubAccount': fromSubAccount,
                  'toSubAccount': toSubAccount, 'loanTrans': loanTrans, 'omitPosRisk': omitPosRisk}
        return self._request(POST, ASSET_SUBACCOUNT_TRANSFER, params)

    # Set permission of transfer out
    def set_permission_transfer_out(self, subAcct, canTransOut=''):
        params = {
            'subAcct': subAcct,
            'canTransOut': canTransOut
        }
        return self._request(POST, USERS_SUBACCOUNT_SET_TRANSFER_OUT, params)

    # Get custody trading sub-account list
    def get_entrust_subaccounts(self, subAcct=''):
        params = {
            'subAcct': subAcct
        }
        return self._request(GET, USERS_ENTRUST_SUBACCOUNT_LIST, params)
