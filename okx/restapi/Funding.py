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

    # Lightning deposits
    def get_deposit_lightning(self, ccy, amt, to=""):
        params = {'ccy': ccy, 'amt': amt}
        if to:
            params = {'to': to}
        return self._request(GET, ASSET_DEPOSIT_LIGHTNING, params)

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

    # Withdrawal Lightning
    def withdrawal_lightning(self, ccy, invoice, memo=''):
        params = {'ccy': ccy, 'invoice': invoice, 'memo': memo}
        return self._request(POST, ASSET_WITHDRAWAL_LIGHTNING, params)

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

    # Small assets convert
    def convert_dust_assets(self, ccy=[]):
        params = {
            'ccy': ccy
        }
        return self._request(POST, ASSET_CONVERT_DUST_ASSETS, params)

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
