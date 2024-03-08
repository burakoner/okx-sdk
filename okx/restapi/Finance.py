from .BaseClient import OkxBaseClient
from ..constants import *


class FinanceClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    def earn_get_offers(self, productId='', protocolType='', ccy=''):
        params = {
            'productId': productId,
            'protocolType': protocolType,
            'ccy': ccy
        }
        return self._request(GET, FINANCE_STACKING_DEFI_OFFERS, params)

    def earn_purchase(self, productId='', investData=[], term=''):
        params = {
            'productId': productId,
            'investData': investData,
            'tag': BROKER_ID,
        }
        if term != '':
            params['term'] = term
        return self._request(POST, FINANCE_STACKING_DEFI_PURCHASE, params)

    def earn_redeem(self, ordId='', protocolType='', allowEarlyRedeem=''):
        params = {
            'ordId': ordId,
            'protocolType': protocolType,
            'allowEarlyRedeem': allowEarlyRedeem
        }
        return self._request(POST, FINANCE_STACKING_DEFI_REDEEM, params)

    def earn_cancel(self, ordId='', protocolType=''):
        params = {
            'ordId': ordId,
            'protocolType': protocolType
        }
        return self._request(POST, FINANCE_STACKING_DEFI_CANCEL, params)

    def earn_get_active_orders(self, productId='', protocolType='', ccy='', state=''):
        params = {
            'productId': productId,
            'protocolType': protocolType,
            'ccy': ccy,
            'state': state
        }
        return self._request(GET, FINANCE_STACKING_DEFI_ORDERS_ACTIVE, params)

    def earn_get_orders_history(self, productId='', protocolType='', ccy='', after='', before='', limit=''):
        params = {
            'productId': productId,
            'protocolType': protocolType,
            'ccy': ccy,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, FINANCE_STACKING_DEFI_ORDERS_HISTORY, params)

    def eth_purchase(self, amt):
        params = { 'amt': amt }
        return self._request(POST, FINANCE_STACKING_DEFI_ETH_PURCHASE, params)

    def eth_redeem(self, amt):
        params = { 'amt': amt }
        return self._request(POST, FINANCE_STACKING_DEFI_ETH_REDEEM, params)

    def eth_get_balance(self):
        return self._request(GET, FINANCE_STACKING_DEFI_ETH_BALANCE)

    def eth_get_purchase_redeem_history(self, type, status='', after='', before='', limit=''):
        params = {'type': type, 'status': status, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, FINANCE_STACKING_DEFI_ETH_PURCHASE_REDEEM_HISTORY, params)

    def eth_apy_history(self, days):
        params = { 'days': days }
        return self._request(GET, FINANCE_STACKING_DEFI_ETH_APY_HISTORY, params)

    # Get saving balance
    def savings_get_saving_balance(self, ccy=''):
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
    def savings_set_lending_rate(self, ccy='', rate=''):
        params = {'ccy': ccy, 'rate': rate}
        return self._request(POST, FINANCE_SAVINGS_SET_LENDING_RATE, params)

    # Get lending history
    def savings_get_lending_history(self, ccy='', after='', before='', limit=''):
        params = {
            'ccy': ccy,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, FINANCE_SAVINGS_LENDING_HISTORY, params)

    # Get public borrow info (public)
    def savings_get_public_borrow_info(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, FINANCE_SAVINGS_LENDING_RATE_SUMMARY, params)

    # Get public borrow history (public)
    def savings_get_public_borrow_history(self, ccy='', after='', before='', limit=''):
        params = {
            'ccy': ccy,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, FINANCE_SAVINGS_LENDING_RATE_HISTORY, params)
