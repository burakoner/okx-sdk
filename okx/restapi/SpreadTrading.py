from .BaseClient import OkxBaseClient
from ..constants import *


class SpreadTradingClient(OkxBaseClient):

    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase,
                               use_server_time, simulation, domain, debug, proxy)

    # Place Order
    def place_order(self, sprdId='', clOrdId='', side='', ordType='', sz='', px=''):
        params = {'sprdId': sprdId, 'clOrdId': clOrdId, 'tag': BROKER_ID, 'side': side, 'ordType': ordType, 'sz': sz,
                  'px': px}
        return self._request(POST, SPREAD_PLACE_ORDER, params)

    # Cancel Order
    def cancel_order(self, ordId='', clOrdId=''):
        params = {'ordId': ordId, 'clOrdId': clOrdId}
        return self._request(POST, SPREAD_CANCEL_ORDER, params)

    # Cancel All orders
    def cancel_all_orders(self, sprdId=''):
        params = {'sprdId': sprdId}
        return self._request(POST, SPREAD_MASS_CANCEL, params)

    def amend_order(self, ordId='', clOrdId='', reqId='', newSz='', newPx=''):
        params = {'ordId': ordId, 'clOrdId': clOrdId,
                  'reqId': reqId, 'newSz': newSz, 'newPx': newPx}
        return self._request(POST, SPREAD_AMEND_ORDER, params)

    # Get order details
    def get_order_details(self, ordId='', clOrdId=''):
        params = {'ordId': ordId, 'clOrdId': clOrdId}
        return self._request(GET, SPREAD_GET_ORDER, params)

    # Get active orders
    def get_active_orders(self, sprdId='', ordType='', state='', beginId='', endId='', limit=''):
        params = {'sprdId': sprdId, 'ordType': ordType, 'state': state, 'beginId': beginId, 'endId': endId,
                  'limit': limit}
        return self._request(GET, SPREAD_ORDERS_PENDING, params)

    # Get orders (last 7 days)
    def get_orders_history(self, sprdId='', ordType='', state='', beginId='', endId='', begin='', end='', limit=''):
        params = {'sprdId': sprdId, 'ordType': ordType, 'state': state, 'beginId': beginId, 'endId': endId,
                  'begin': begin, 'end': end, 'limit': limit}
        return self._request(GET, SPREAD_ORDERS_HISTORY, params)
    
    # Get orders history (last 3 months)
    def get_orders_archive(self, sprdId='', ordType='', state='', instType='', instFamily='', beginId='', endId='', begin='', end='', limit=''):
        params = {'sprdId': sprdId, 'ordType': ordType, 'state': state, 'instType': instType, 'instFamily': instFamily, 'beginId': beginId, 'endId': endId, 'begin': begin, 'end': end, 'limit': limit}
        return self._request(GET, SPREAD_ORDERS_HISTORY_ARCHIVE, params)

    # Get trades (last 7 days)
    def get_trades(self, sprdId='', tradeId='', ordId='', beginId='', endId='', begin='', end='', limit=''):
        params = {'sprdId': sprdId, 'tradeId': tradeId, 'ordId': ordId, 'beginId': beginId, 'endId': endId,
                  'begin': begin, 'end': end, 'limit': limit}
        return self._request(GET, SPREAD_TRADES, params)

    # Get Spreads (Public)
    def get_spreads(self, baseCcy='', instId='', sprdId='', state=''):
        params = {'baseCcy': baseCcy, 'instId': instId,
                  'sprdId': sprdId, 'state': state}
        return self._request(GET, SPREAD_SPREADS, params)

    # Get order book (Public)
    def get_order_book(self, sprdId='', sz=''):
        params = {'sprdId': sprdId, 'sz': sz}
        return self._request(GET, SPREAD_BOOKS, params)

    # Get ticker (Public)
    def get_ticker(self, sprdId=''):
        params = {'sprdId': sprdId}
        return self._request(GET, SPREAD_TICKER, params)

    # Get public trades (Public)
    def get_public_trades(self, sprdId=''):
        params = {'sprdId': sprdId}
        return self._request(GET, SPREAD_PUBLIC_TRADES, params)
