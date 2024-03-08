from .BaseClient import OkxBaseClient
from ..constants import *


class SubAccountClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    # Get sub-account list
    def get_subaccount_list(self, enable='', subAcct='', after='', before='', limit=''):
        params = {'enable': enable, 'subAcct': subAcct, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, USERS_SUBACCOUNT_LIST, params)

    # Reset the API Key of a sub-account
    def reset_subaccount_apikey(self, subAcct, apiKey, label='', perm='', ip=''):
        params = {'subAcct': subAcct, 'apiKey': apiKey}

        if ip != '':
            params['ip'] = ip
        if label != '':
            params['label'] = label
        if perm != '':
            params['perm'] = perm
        return self._request(POST, USERS_SUBACCOUNT_MODIFY_APIKEY, params)

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
    def transfer_between_sub_accounts(self, ccy, amt, froms, to, fromSubAccount, toSubAccount, loanTrans='false',
                                      omitPosRisk='false'):
        params = {'ccy': ccy, 'amt': amt, 'from': froms, 'to': to, 'fromSubAccount': fromSubAccount,
                  'toSubAccount': toSubAccount, 'loanTrans': loanTrans, 'omitPosRisk': omitPosRisk}
        return self._request(POST, ASSET_SUBACCOUNT_TRANSFER, params)

    # Set permission of transfer out
    def set_permission_transfer_out(self, subAcct='', canTransOut=''):
        params = {
            'subAcct': subAcct,
            'canTransOut': canTransOut
        }
        return self._request(POST, USERS_SUBACCOUNT_SET_TRANSFER_OUT, params)

    # Get custody trading sub-account list
    def get_entrust_subaccount_list(self, subAcct=''):
        params = {
            'subAcct': subAcct
        }
        return self._request(GET, USERS_ENTRUST_SUBACCOUNT_LIST, params)

    # Set sub-accounts VIP loan allocation
    def set_sub_accounts_VIP_loan(self, enable='', alloc=[]):
        params = {
            'enable': enable,
            'alloc': alloc
        }
        return self._request(POST, ACCOUNT_SUBACCOUNT_SET_LOAN_ALLOCATION, params)

    # Get sub_account borrow interest and limit
    def get_sub_account_borrow_interest_and_limit(self, subAcct='', ccy=''):
        params = {
            'subAcct': subAcct,
            'ccy': ccy
        }
        return self._request(GET, ACCOUNT_SUBACCOUNT_INTEREST_LIMITS, params)
