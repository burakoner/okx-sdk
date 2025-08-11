from .BaseClient import OkxBaseClient
from ..constants import *


class FundingClient(OkxBaseClient):

    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    # Get Currencies
    def get_currencies(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, ASSET_CURRENCIES, params)

    # Get Balance
    def get_balances(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, ASSET_BALANCES, params)

    # Get non-tradable assets
    def get_non_tradable_assets(self, ccy=''):
        params = {
            'ccy': ccy
        }
        return self._request(GET, ASSET_NON_TRADABLE_ASSETS, params)

    # Get account asset valuation
    def get_asset_valuation(self, ccy=''):
        params = {
            'ccy': ccy
        }
        return self._request(GET, ASSET_ASSET_VALUATION, params)

    # Funds transfer
    def funds_transfer(self, ccy, amt, from_, to, type='0', subAcct='', instId='', toInstId='', loanTrans=''):
        params = {'ccy': ccy, 'amt': amt, 'from': from_, 'to': to, 'type': type, 'subAcct': subAcct, 'instId': instId,
                  'toInstId': toInstId, 'loanTrans': loanTrans}
        return self._request(POST, ASSET_TRANSFER, params)

    # Get funds transfer state
    def transfer_state(self, transId, type=''):
        params = {'transId': transId, 'type': type}
        return self._request(GET, ASSET_TRANSFER_STATE, params)

    # Asset bills details
    def get_bills(self, ccy='', type='', after='', before='', limit=''):
        params = {'ccy': ccy, 'type': type, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, ASSET_BILLS, params)
    
    # Asset bills history
    def get_bills_history(self, ccy='', type='', clientId='', after='', before='', limit='', pagingType=''):
        params = {'ccy': ccy, 'type': type, 'clientId': clientId, 'after': after, 'before': before, 'limit': limit, 'pagingType': pagingType}
        return self._request(GET, ASSET_BILLS_HISTORY, params)

    # Get Deposit Address
    def get_deposit_address(self, ccy):
        params = {'ccy': ccy}
        return self._request(GET, ASSET_DEPOSIT_ADDRESS, params)

    # Get Deposit History
    def get_deposit_history(self, ccy='', state='', after='', before='', limit='', txId='', depId='', fromWdId=''):
        params = {'ccy': ccy, 'state': state, 'after': after, 'before': before, 'limit': limit, 'txId': txId,
                  'depId': depId, 'fromWdId': fromWdId}
        return self._request(GET, ASSET_DEPOSIT_HISTORY, params)

    # Withdrawal
    def withdrawal(self, ccy, amt, dest, toAddr, fee, chain='', areaCode='', clientId=''):
        params = {'ccy': ccy, 'amt': amt, 'dest': dest, 'toAddr': toAddr, 'fee': fee, 'chain': chain,
                  'areaCode': areaCode, 'clientId': clientId}
        return self._request(POST, ASSET_WITHDRAWAL, params)

    # Cancel withdrawal
    def cancel_withdrawal(self, wdId=''):
        params = {
            'wdId': wdId
        }
        return self._request(POST, ASSET_CANCEL_WITHDRAWAL, params)

    # Get Withdrawal History
    def get_withdrawal_history(self, ccy='', wdId='', state='', after='', before='', limit='', txId=''):
        params = {'ccy': ccy, 'wdId': wdId, 'state': state, 'after': after, 'before': before, 'limit': limit,
                  'txId': txId}
        return self._request(GET, ASSET_WITHDRAWAL_HISTORY, params)

    # Get deposit withdraw status
    def get_deposit_withdraw_status(self, wdId='', txId='', ccy='', to='', chain=''):
        params = {'wdId': wdId, 'txId': txId, 'ccy': ccy, 'to': to, 'chain': chain}
        return self._request(GET, ASSET_DEPOSIT_WITHDRAW_STATUS, params)

    # Get exchange list (public)
    def get_exchange_list(self):
        return self._request(GET, ASSET_EXCHANGE_LIST)

    # Apply for monthly statement
    def apply_monthly_statement(self, month):
        params = {
            'month': month
        }
        return self._request(POST, ASSET_MONTHLY_STATEMENT_APPLY, params)

    # Apply for monthly statement
    def get_monthly_statement(self, month):
        params = {
            'month': month
        }
        return self._request(GET, ASSET_MONTHLY_STATEMENT_RETRIEVE, params)

    def get_convert_currencies(self):
        params = {}
        return self._request(GET, ASSET_CONVERT_CURRENCIES, params)

    def get_convert_currency_pair(self, fromCcy='', toCcy=''):
        params = {"fromCcy": fromCcy, 'toCcy': toCcy}
        return self._request(GET, ASSET_CONVERT_CURRENCY_PAIR, params)

    def estimate_quote(self, baseCcy='', quoteCcy='', side='', rfqSz='', rfqSzCcy='', clQReqId=''):
        params = {'baseCcy': baseCcy, 'quoteCcy': quoteCcy, 'side': side, 'rfqSz': rfqSz, 'rfqSzCcy': rfqSzCcy,
                  'clQReqId': clQReqId, 'tag': BROKER_ID}
        return self._request(POST, ASSET_CONVERT_ESTIMATE_QUOTE, params)

    def convert_trade(self, quoteId='', baseCcy='', quoteCcy='', side='', sz='', szCcy='', clTReqId=''):
        params = {'quoteId': quoteId, 'baseCcy': baseCcy, 'quoteCcy': quoteCcy, 'side': side, 'sz': sz, 'szCcy': szCcy,
                  'clTReqId': clTReqId, 'tag': BROKER_ID}
        return self._request(POST, ASSET_CONVERT_TRADE, params)

    def get_convert_history(self, after='', before='', limit='', tag=''):
        params = {'after': after, 'before': before, 'limit': limit, 'tag': tag}
        return self._request(GET, ASSET_CONVERT_HISTORY, params)

    def get_fiat_deposit_payment_methods(self, ccy):
        params = {'ccy': ccy}
        return self._request(GET, FIAT_DEPOSIT_PAYMENT_METHODS, params)

    def get_fiat_withdrawal_payment_methods(self, ccy):
        params = {'ccy': ccy}
        return self._request(GET, FIAT_WITHDRAWAL_PAYMENT_METHODS, params)

    def fiat_withdraw(self, paymentAcctId, ccy, amt, paymentMethod, clientId):
        params = {'paymentAcctId': paymentAcctId, 'ccy': ccy, 'amt': amt, 'paymentMethod': paymentMethod,
                  'clientId': clientId}
        return self._request(POST, FIAT_CREATE_WITHDRAWAL, params)

    def cancel_fiat_withdrawal(self, ordId):
        params = {'ordId': ordId}
        return self._request(POST, FIAT_CANCEL_WITHDRAWAL, params)

    def get_fiat_withdrawal_history(self, ccy='', paymentMethod='', state='', after='', before='', limit=''):
        params = {'ccy': ccy, 'paymentMethod': paymentMethod, 'state': state, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, FIAT_WITHDRAWAL_ORDER_HISTORY, params)

    def get_fiat_withdrawal_details(self, ordId):
        params = {'ordId': ordId}
        return self._request(GET, FIAT_WITHDRAWAL, params)

    def get_fiat_deposit_history(self, ccy='', paymentMethod='', state='', after='', before='', limit=''):
        params = {'ccy': ccy, 'paymentMethod': paymentMethod, 'state': state, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, FIAT_DEPOSIT_ORDER_HISTORY, params)

    def get_fiat_deposit_details(self, ordId):
        params = {'ordId': ordId}
        return self._request(GET, FIAT_DEPOSIT, params)

    def fiat_buy_sell_currencies(self):
        return self._request(POST, FIAT_BUY_SELL_CURRENCIES)

    def fiat_buy_sell_currency_pairs(self, fromCcy='', toCcy=''):
        params = {"fromCcy": fromCcy, 'toCcy': toCcy}
        return self._request(POST, FIAT_BUY_SELL_CURRENCY_PAIR, params)

    def get_fiat_buy_sell_quote(self,side, fromCcy, toCcy, rfqAmt, rfqCcy):
        params = {"fromCcy": fromCcy, 'toCcy': toCcy, 'side': side, 'rfqAmt': rfqAmt, 'rfqCcy': rfqCcy}
        return self._request(GET, FIAT_BUY_SELL_QUOTE, params)

    def fiat_buy_sell_trade(self, quoteId, side, fromCcy, toCcy, rfqAmt, rfqCcy, paymentMethod, clOrdId):
        params = {'quoteId': quoteId, 'side': side, 'fromCcy': fromCcy, 'toCcy': toCcy, 'rfqAmt': rfqAmt,
                  'rfqCcy': rfqCcy, 'paymentMethod': paymentMethod, 'clOrdId': clOrdId}
        return self._request(POST, FIAT_BUY_SELL_TRADE, params)

    def get_fiat_buy_sell_history(self, ordId='', clOrdId='', state='', begin='', end='', limit=''):
        params = {'ordId': ordId, 'clOrdId': clOrdId, 'state': state, 'begin': begin, 'end': end, 'limit': limit}
        return self._request(GET, FIAT_BUY_SELL_HISTORY, params)