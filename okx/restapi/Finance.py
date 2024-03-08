from .BaseClient import OkxBaseClient
from ..constants import *


class FinanceClient(OkxBaseClient):
    def __init__(self, api_key='', api_secret_key='', pass_phrase='', use_server_time=False, simulation=False,
                 domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, api_key, api_secret_key, pass_phrase, use_server_time, simulation, domain, debug,
                               proxy)

    def get_offers(self, productId='', protocolType='', ccy=''):
        params = {
            'productId': productId,
            'protocolType': protocolType,
            'ccy': ccy
        }
        return self._request(GET, FINANCE_STACKING_DEFI_OFFERS, params)

    def purchase(self, productId='', investData=[], term=''):
        params = {
            'productId': productId,
            'investData': investData,
            'tag': BROKER_ID,
        }
        if term != '':
            params['term'] = term
        return self._request(POST, FINANCE_STACKING_DEFI_PURCHASE, params)

    def redeem(self, ordId='', protocolType='', allowEarlyRedeem=''):
        params = {
            'ordId': ordId,
            'protocolType': protocolType,
            'allowEarlyRedeem': allowEarlyRedeem
        }
        return self._request(POST, FINANCE_STACKING_DEFI_REDEEM, params)

    def cancel(self, ordId='', protocolType=''):
        params = {
            'ordId': ordId,
            'protocolType': protocolType
        }
        return self._request(POST, FINANCE_STACKING_DEFI_CANCEL, params)

    def get_activity_orders(self, productId='', protocolType='', ccy='', state=''):
        params = {
            'productId': productId,
            'protocolType': protocolType,
            'ccy': ccy,
            'state': state
        }
        return self._request(GET, FINANCE_STACKING_DEFI_ORDERS_ACTIVE, params)

    def get_orders_history(self, productId='', protocolType='', ccy='', after='', before='', limit=''):
        params = {
            'productId': productId,
            'protocolType': protocolType,
            'ccy': ccy,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, FINANCE_STACKING_DEFI_ORDERS_HISTORY, params)

    # TODO
    # TODO
    # TODO
    # TODO
    # TODO

    # Get saving balance
    def get_saving_balance(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, FINANCE_SAVINGS_BALANCE, params)

    # Savings purchase/redemption
    def savings_purchase_redemption(self, ccy='', amt='', side='', rate=''):
        params = {
            'ccy': ccy,
            'amt': amt,
            'side': side,
            'rate': rate
        }
        return self._request(POST, FINANCE_SAVINGS_PURCHASE_REDEMPT, params)

    # Set lending rate
    def set_lending_rate(self, ccy='', rate=''):
        params = {'ccy': ccy, 'rate': rate}
        return self._request(POST, FINANCE_SAVINGS_SET_LENDING_RATE, params)

    # Get lending history
    def get_lending_history(self, ccy='', after='', before='', limit=''):
        params = {
            'ccy': ccy,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, FINANCE_SAVINGS_LENDING_HISTORY, params)

    # Get public borrow info (public)
    def get_public_borrow_info(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, FINANCE_SAVINGS_LENDING_RATE_SUMMARY, params)

    # Get public borrow history (public)
    def get_public_borrow_history(self, ccy='', after='', before='', limit=''):
        params = {
            'ccy': ccy,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, FINANCE_SAVINGS_LENDING_RATE_HISTORY, params)
