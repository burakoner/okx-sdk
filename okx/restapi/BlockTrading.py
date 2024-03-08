from .BaseClient import OkxBaseClient
from ..constants import *


class BlockTradingClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase,
                               use_server_time, simulation, domain, debug, proxy)

    def counterparties(self):
        params = {}
        return self._request(GET, RFQ_COUNTERPARTIES, params)

    def create_rfq(self, counterparties=[], anonymous='false', clRfqId='', allowPartialExecution='false',
                   legs=[]):
        params = {'counterparties': counterparties, 'anonymous': anonymous, 'clRfqId': clRfqId, 'tag': BROKER_ID,
                  'allowPartialExecution': allowPartialExecution, 'legs': legs}
        return self._request(POST, RFQ_CREATE_RFQ, params)

    def cancel_rfq(self, rfqId='', clRfqId=''):
        params = {'rfqId': rfqId, 'clRfqId': clRfqId}
        return self._request(POST, RFQ_CANCEL_RFQ, params)

    def cancel_batch_rfqs(self, rfqIds=[], clRfqIds=[]):
        params = {'rfqIds': rfqIds, 'clRfqIds': clRfqIds}
        return self._request(POST, RFQ_CANCEL_BATCH_RFQS, params)

    def cancel_all_rfqs(self):
        params = {}
        return self._request(POST, RFQ_CANCEL_ALL_RSQS, params)

    def execute_quote(self, rfqId='', quoteId='', legs=[]):
        params = {'rfqId': rfqId, 'quoteId': quoteId, 'legs': legs}
        return self._request(POST, RFQ_EXECUTE_QUOTE, params)

    # Get Quote products
    def get_quote_products(self):
        return self._request(GET, RFQ_GET_MARKER_INSTRUMENT_SETTING)

    # Set Quote products
    def set_marker_instrument(self, params=[]):
        return self._request(POST, RFQ_SET_MARKER_INSTRUMENT_SETTING, params)

    def reset_mmp(self):
        return self._request(POST, RFQ_MMP_RESET)

    def set_mmp_config(self, timeInterval, frozenInterval, countLimit):
        params = {'timeInterval': timeInterval,
                  'frozenInterval': frozenInterval, 'countLimit': countLimit}
        return self._request(POST, RFQ_SET_MMP_CONFIG, params)

    def get_mmp_config(self, timeInterval='', frozenInterval='', countLimit='', mmpFrozen='', mmpFrozenUntil=''):
        params = {'timeInterval': timeInterval, 'frozenInterval': frozenInterval,
                  'countLimit': countLimit, 'mmpFrozen': mmpFrozen, 'mmpFrozenUntil': mmpFrozenUntil}
        return self._request(GET, RFQ_GET_MMP_CONFIG, params)

    def create_quote(self, rfqId='', clQuoteId='', quoteSide='', legs=[], anonymous=False, expiresIn=''):
        params = {'rfqId': rfqId, 'clQuoteId': clQuoteId, 'tag': BROKER_ID, 'quoteSide': quoteSide, 'legs': legs,
                  'anonymous': anonymous, 'expiresIn': expiresIn}
        return self._request(POST, RFQ_CREATE_QUOTE, params)

    def cancel_quote(self, quoteId='', clQuoteId=''):
        params = {'quoteId': quoteId, 'clQuoteId': clQuoteId}
        return self._request(POST, RFQ_CANCEL_QUOTE, params)

    def cancel_batch_quotes(self, quoteIds='', clQuoteIds=''):
        params = {'quoteIds': quoteIds, 'clQuoteIds': clQuoteIds}
        return self._request(POST, RFQ_CANCEL_BATCH_QUOTES, params)

    def cancel_all_quotes(self):
        params = {}
        return self._request(POST, RFQ_CANCEL_ALL_QUOTES, params)

    def get_rfqs(self, rfqId='', clRfqId='', state='', beginId='', endId='', limit=''):
        params = {'rfqId': rfqId, 'clRfqId': clRfqId, 'state': state, 'beginId': beginId, 'endId': endId,
                  'limit': limit}
        return self._request(GET, RFQ_RFQS, params)

    def get_quotes(self, rfqId='', clRfqId='', quoteId='', clQuoteId='', state='', beginId='', endId='', limit=''):
        params = {'rfqId': rfqId, 'clRfqId': clRfqId, 'quoteId': quoteId, 'clQuoteId': clQuoteId, 'state': state,
                  'beginId': beginId, 'endId': endId, 'limit': limit}
        return self._request(GET, RFQ_QUOTES, params)

    def get_trades(self, rfqId='', clRfqId='', quoteId='', clQuoteId='', state='', beginId='', endId='', beginTs='',
                   endTs='', limit=''):
        params = {'rfqId': rfqId, 'clRfqId': clRfqId, 'quoteId': quoteId, 'clQuoteId': clQuoteId, 'state': state,
                  'beginId': beginId, 'endId': endId, 'beginTs': beginTs, 'endTs': endTs, 'limit': limit}
        return self._request(GET, RFQ_TRADES, params)

    def get_public_trades(self, beginId='', endId='', limit=''):
        params = {'beginId': beginId, 'endId': endId, 'limit': limit}
        return self._request(GET, RFQ_PUBLIC_TRADES, params)

    # Get block tickers
    def get_block_tickers(self, instType='', uly='', instFamily=''):
        params = {
            'instType': instType,
            'uly': uly,
            'instFamily': instFamily
        }
        return self._request(GET, MARKET_BLOCK_TICKERS, params)

    # Get block ticker
    def get_block_ticker(self, instId=''):
        params = {
            'instId': instId
        }
        return self._request(GET, MARKET_BLOCK_TICKER, params)

    # Get block trades
    def get_block_trades(self, instId=''):
        params = {
            'instId': instId
        }
        return self._request(GET, MARKET_BLOCK_TRADES, params)
