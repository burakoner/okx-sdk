from .BaseClient import OkxBaseClient
from ..constants import *

class MarketDataClient(OkxBaseClient):

    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    # Get Tickers
    def get_tickers(self, instType,  instFamily=''):
        params = {'instType': instType, 'instFamily': instFamily}
        return self._request(GET, MARKET_TICKERS, params)

    # Get Ticker
    def get_ticker(self, instId):
        params = {'instId': instId}
        return self._request(GET, MARKET_TICKER, params)

    # Get Order Book
    def get_orderbook(self, instId, sz=''):
        params = {'instId': instId, 'sz': sz}
        return self._request(GET, MARKET_BOOKS, params)

    # Get Full Order Book
    def get_full_orderbook(self, instId, sz=''):
        params = {'instId': instId, 'sz': sz}
        return self._request(GET, MARKET_BOOKS_FULL, params)

    # Get Candlesticks
    def get_candlesticks(self, instId, bar='', after='', before='', limit=''):
        params = {'instId': instId, 'bar': bar, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, MARKET_CANDLES, params)

    # Get Candlesticks history
    def get_history_candlesticks(self, instId,  bar='', after='', before='', limit=''):
        params = {'instId': instId, 'bar': bar, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, MARKET_HISTORY_CANDLES, params)

    # Get Trades
    def get_trades(self, instId, limit=''):
        params = {'instId': instId, 'limit': limit}
        return self._request(GET, MARKET_TRADES, params)

    # GET Trades history
    def get_trades_history(self, instId='', type='', after='', before='', limit=''):
        params = {
            'instId': instId,
            'type': type,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, MARKET_HISTORY_TRADES, params)

    # Option trades by instrument family
    def get_option_trades_by_family(self, instFamily=''):
        params = {
            'instFamily': instFamily
        }
        return self._request(GET, MARKET_OPTION_INSTRUMENT_FAMILY_TRADES, params)

    # Get option trades
    def get_option_trades(self, instId='', instFamily='', optType=''):
        params = {
            'instId': instId,
            'instFamily': instFamily,
            'optType': optType
        }
        return self._request(GET, PUBLIC_OPTION_TRADES, params)

    # Get 24H total volume
    def get_volume(self):
        return self._request(GET, MARKET_PLATFORM_24_VOLUME)

    # Get Call auction details
    def get_call_auction_details(self, instId):
        params = {'instId': instId}
        return self._request(GET, MARKET_CALL_AUCTION_DETAILS, params)