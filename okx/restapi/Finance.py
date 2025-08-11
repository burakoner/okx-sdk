from .BaseClient import OkxBaseClient
from ..constants import *


class FinanceClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    # On-chain Earn Begin
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
    # On-chain Earn End

    # ETH Staking Begin
    def eth_product_info(self):
        return self._request(GET, FINANCE_STACKING_DEFI_ETH_PRODUCT_INFO)

    def eth_purchase(self, amt):
        params = { 'amt': amt }
        return self._request(POST, FINANCE_STACKING_DEFI_ETH_PURCHASE, params)

    def eth_redeem(self, amt):
        params = { 'amt': amt }
        return self._request(POST, FINANCE_STACKING_DEFI_ETH_REDEEM, params)

    def eth_get_balance(self):
        return self._request(GET, FINANCE_STACKING_DEFI_ETH_BALANCE)

    def eth_get_purchase_redeem_history(self, type='', status='', after='', before='', limit=''):
        params = {'type': type, 'status': status, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, FINANCE_STACKING_DEFI_ETH_PURCHASE_REDEEM_HISTORY, params)

    def eth_apy_history(self, days):
        params = { 'days': days }
        return self._request(GET, FINANCE_STACKING_DEFI_ETH_APY_HISTORY, params)
    # ETH Staking End
    
    # SOL Staking Begin
    def sol_product_info(self):
        return self._request(GET, FINANCE_STACKING_DEFI_SOL_PRODUCT_INFO)

    def sol_purchase(self, amt):
        params = { 'amt': amt }
        return self._request(POST, FINANCE_STACKING_DEFI_SOL_PURCHASE, params)

    def sol_redeem(self, amt):
        params = { 'amt': amt }
        return self._request(POST, FINANCE_STACKING_DEFI_SOL_REDEEM, params)

    def sol_get_balance(self):
        return self._request(GET, FINANCE_STACKING_DEFI_SOL_BALANCE)

    def sol_get_purchase_redeem_history(self, type='', status='', after='', before='', limit=''):
        params = {'type': type, 'status': status, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, FINANCE_STACKING_DEFI_SOL_PURCHASE_REDEEM_HISTORY, params)

    def sol_apy_history(self, days):
        params = { 'days': days }
        return self._request(GET, FINANCE_STACKING_DEFI_SOL_APY_HISTORY, params)
    # SOL Staking End

    # Simple Earn Flexible Begin
    def savings_get_saving_balance(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, FINANCE_SAVINGS_BALANCE, params)

    def savings_purchase_redemption(self, ccy='', amt='', side='', rate=''):
        params = {
            'ccy': ccy,
            'amt': amt,
            'side': side,
            'rate': rate
        }
        return self._request(POST, FINANCE_SAVINGS_PURCHASE_REDEMPT, params)

    def savings_set_lending_rate(self, ccy='', rate=''):
        params = {'ccy': ccy, 'rate': rate}
        return self._request(POST, FINANCE_SAVINGS_SET_LENDING_RATE, params)

    def savings_get_lending_history(self, ccy='', after='', before='', limit=''):
        params = {
            'ccy': ccy,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, FINANCE_SAVINGS_LENDING_HISTORY, params)

    def savings_get_public_borrow_info(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, FINANCE_SAVINGS_LENDING_RATE_SUMMARY, params)

    def savings_get_public_borrow_history(self, ccy='', after='', before='', limit=''):
        params = {
            'ccy': ccy,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, FINANCE_SAVINGS_LENDING_RATE_HISTORY, params)
    # Simple Earn Flexible End

    # Flexible Loan Begin
    def get_flexible_loan_borrow_currencies(self):
        return self._request(GET, FINANCE_FLEXIBLE_LOAN_BORROW_CURRENCIES)

    def get_flexible_loan_collateral_assets(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, FINANCE_FLEXIBLE_LOAN_COLLATERAL_ASSETS, params)

    def get_flexible_loan_max_loan(self, borrowCcy, supCollateral=[]):
        params = {
            'borrowCcy': borrowCcy,
            'supCollateral': supCollateral
        }
        return self._request(POST, FINANCE_FLEXIBLE_LOAN_MAX_LOAN, params)

    def get_flexible_loan_max_collateral_redeem_amount(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, FINANCE_FLEXIBLE_LOAN_MAX_COLLATERAL_REDEEM_AMOUNT, params)

    def get_flexible_loan_adjust_collateral(self, type, collateralCcy, collateralAmt):
        params = {
            'type': type,
            'collateralCcy': collateralCcy,
            'collateralAmt': collateralAmt
        }
        return self._request(POST, FINANCE_FLEXIBLE_LOAN_ADJUST_COLLATERAL, params)

    def get_flexible_loan_loan_info(self):
        return self._request(GET, FINANCE_FLEXIBLE_LOAN_LOAN_INFO)

    def get_flexible_loan_loan_history(self, type='', after='', before='', limit=''):
        params = {
            'type': type,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, FINANCE_FLEXIBLE_LOAN_LOAN_HISTORY, params)

    def get_flexible_loan_interest_accrued(self, ccy='', after='', before='', limit=''):
        params = {
            'ccy': ccy,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, FINANCE_FLEXIBLE_LOAN_INTEREST_ACCRUED, params)
    # Flexible Loan End
    
