from .BaseClient import OkxBaseClient
from ..constants import *


class PublicDataClient(OkxBaseClient):

    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    # Get System Time
    def get_system_time(self):
        return self._request(GET, SYSTEM_TIME)

    # Status
    def status(self, state=''):
        params = {'state': state}
        return self._request(GET, SYSTEM_STATUS, params)

    # Get Instruments
    def get_instruments(self, instType, uly='', instId='', instFamily=''):
        params = {'instType': instType, 'uly': uly, 'instId': instId, 'instFamily': instFamily}
        return self._request(GET, PUBLIC_INSTRUMENTS, params)

    # Get Delivery/Exercise History
    def get_delivery_exercise_history(self, instType, uly='', after='', before='', limit='', instFamily=''):
        params = {'instType': instType, 'uly': uly, 'after': after, 'before': before, 'limit': limit,
                  'instFamily': instFamily}
        return self._request(GET, PUBLIC_DELIVERY_EXERCISE_HISTORY, params)

    # Get Open Interest
    def get_open_interest(self, instType, uly='', instId='', instFamily=''):
        params = {'instType': instType, 'uly': uly, 'instId': instId, 'instFamily': instFamily}
        return self._request(GET, PUBLIC_OPEN_INTEREST, params)

    # Get Funding Rate
    def get_funding_rate(self, instId):
        params = {'instId': instId}
        return self._request(GET, PUBLIC_FUNDING_RATE, params)

    # Get Funding Rate History
    def funding_rate_history(self, instId, after='', before='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, PUBLIC_FUNDING_RATE_HISTORY, params)

    # Get Limit Price
    def get_price_limit(self, instId):
        params = {'instId': instId}
        return self._request(GET, PUBLIC_PRICE_LIMIT, params)

    # Get Option Market Data
    def get_opt_summary(self, uly='', expTime='', instFamily=''):
        params = {'uly': uly, 'expTime': expTime, 'instFamily': instFamily}
        return self._request(GET, PUBLIC_OPT_SUMMARY, params)

    # Get Estimated Delivery/Excercise Price
    def get_estimated_price(self, instId):
        params = {'instId': instId}
        return self._request(GET, PUBLIC_ESTIMATED_PRICE, params)

    # Get Discount Rate And Interest-Free Quota
    def discount_interest_free_quota(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, PUBLIC_DISCOUNT_RATE_INTETEST_FREE_QUOTA, params)

    # Get Mark Price
    def get_mark_price(self, instType, uly='', instId='', instFamily=''):
        params = {'instType': instType, 'uly': uly, 'instId': instId, 'instFamily': instFamily}
        return self._request(GET, PUBLIC_MARK_PRICE, params)

    # Get position tiers
    def get_position_tiers(self, instType, tdMode, uly='', instFamily='', instId='', ccy='', tier=''):
        params = {'instType': instType, 'tdMode': tdMode, 'uly': uly, 'instId': instId, 'ccy': ccy, 'tier': tier,
                  'instFamily': instFamily}
        return self._request(GET, PUBLIC_POSITION_TIERS, params)

    # Get interest rate and loan quota
    def get_interest_rate_loan_quota(self):
        return self._request(GET, PUBLIC_INTEREST_RATE_LOAN_QUOTA)

    # Get interest rate and loan quota for VIP loans
    def get_vip_interest_rate_loan_quota(self):
        return self._request(GET, PUBLIC_VIP_INTEREST_RATE_LOAN_QUOTA)

    # Get underlying
    def get_underlying(self, instType=''):
        params = {
            'instType': instType
        }
        return self._request(GET, PUBLIC_UNDERLYING, params)

    # Get insurance fund
    def get_insurance_fund(self, instType='', type='', uly='', ccy='', before='', after='', limit='', instFamily=''):
        params = {
            'instType': instType,
            'type': type,
            'uly': uly,
            'ccy': ccy,
            'before': before,
            'after': after,
            'limit': limit,
            'instFamily': instFamily
        }
        return self._request(GET, PUBLIC_INSURANCE_FUND, params)

    # Unit convert
    def unit_convert(self, type='', instId='', sz='', px='', unit=''):
        params = {
            'type': type,
            'instId': instId,
            'sz': sz,
            'px': px,
            'unit': unit
        }
        return self._request(GET, PUBLIC_CONVERT_CONTRACT_COIN, params)

    # Get option tick bands
    def get_option_tickBands(self, instType='', instFamily=''):
        params = {
            'instType': instType,
            'instFamily': instFamily
        }
        return self._request(GET, PUBLIC_INSTRUMENT_TICK_BANDS, params)

    # Get Index Tickers
    def get_index_tickers(self, quoteCcy='', instId=''):
        params = {'quoteCcy': quoteCcy, 'instId': instId}
        return self._request(GET, MARKET_INDEX_TICKERS, params)

    # Get Index Candlesticks
    def get_index_candlesticks(self, instId, after='', before='', bar='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, MARKET_INDEX_CANDLES, params)

    # Get Index Candlesticks History
    def get_index_candlesticks_history(self, instId, after='', before='', bar='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, MARKET_HISTORY_INDEX_CANDLES, params)

    # Get Mark Price Candlesticks
    def get_mark_price_candlesticks(self, instId, after='', before='', bar='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, MARKET_MARK_PRICE_CANDLES, params)

    # Get Mark Price Candlesticks History
    def get_mark_price_candlesticks_history(self, instId, after='', before='', bar='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, MARKET_HISTORY_MARK_PRICE_CANDLES, params)

    # Get Oracle
    def get_oracle(self):
        return self._request(GET, MARKET_OPEN_ORACLE)

    # Get exchange rate
    def get_exchange_rate(self):
        return self._request(GET, MARKET_EXCHANGE_RATE)

    # Get index components
    def get_index_components(self, index=''):
        param = {
            'index': index
        }
        return self._request(GET, MARKET_INDEX_COMPONENTS, param)

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

    # Get economic calendar data
    def get_economic_calendar(self, region='', importance='', before='', after='', limit=''):
        params = {
            'region': region,
            'importance': importance,
            'before': before,
            'after': after,
            'limit': limit,
        }
        return self._request(GET, PUBLIC_ECONOMIC_CALENDAR, params)

    # Get Tickers
    def get_tickers(self, instType, uly='', instFamily=''):
        if uly:
            params = {'instType': instType, 'uly': uly, 'instFamily': instFamily}
        else:
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
    def get_candlesticks(self, instId, after='', before='', bar='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, MARKET_CANDLES, params)

    # Get Candlesticks history
    def get_history_candlesticks(self, instId, after='', before='', bar='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, MARKET_HISTORY_CANDLES, params)

    # Get Trades
    def get_trades(self, instId, limit=''):
        params = {'instId': instId, 'limit': limit}
        return self._request(GET, MARKET_TRADES, params)

    # GET Trades history
    def get_history_trades(self, instId='', type='', after='', before='', limit=''):
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
