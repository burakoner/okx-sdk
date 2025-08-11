from .BaseClient import OkxBaseClient
from ..constants import *

class PublicDataClient(OkxBaseClient):

    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    # Get System Time
    def get_time(self):
        return self._request(GET, SYSTEM_TIME)

    # Status
    def get_status(self, state=''):
        params = {'state': state}
        return self._request(GET, SYSTEM_STATUS, params)
    
    # Get Announcements
    def get_announcements(self, annType='', page=''):
        params = {'annType': annType, 'page': page}
        return self._request(GET, SUPPORT_ANNOUNCEMENTS, params)
    
    # Get Announcement types
    def get_announcement_types(self):
        return self._request(GET, SUPPORT_ANNOUNCEMENT_TYPES)

    # Get Instruments
    def get_instruments(self, instType, instId='', instFamily=''):
        params = {'instType': instType, 'instId': instId, 'instFamily': instFamily}
        return self._request(GET, PUBLIC_INSTRUMENTS, params)

    # Get Estimated Delivery/Excercise Price
    def get_estimated_price(self, instId):
        params = {'instId': instId}
        return self._request(GET, PUBLIC_ESTIMATED_PRICE, params)

    # Get Delivery/Exercise History
    def get_delivery_exercise_history(self, instType, instFamily, after='', before='', limit=''):
        params = {'instType': instType, 'after': after, 'before': before, 'limit': limit,
                  'instFamily': instFamily}
        return self._request(GET, PUBLIC_DELIVERY_EXERCISE_HISTORY, params)
    
    # Get estimated future settlement price
    def get_estimated_settlement_info(self, instId):
        params = {'instId': instId}
        return self._request(GET, PUBLIC_ESTIMATED_SETTLEMENT_INFO, params)

    # Get futures settlement history
    def get_settlement_history(self, instFamily, after='', before='', limit=''):
        params = {'instFamily': instFamily, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, PUBLIC_SETTLEMENT_HISTORY, params)

    # Get Funding Rate
    def get_funding_rate(self, instId):
        params = {'instId': instId}
        return self._request(GET, PUBLIC_FUNDING_RATE, params)

    # Get Funding Rate History
    def funding_rate_history(self, instId, after='', before='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, PUBLIC_FUNDING_RATE_HISTORY, params)

    # Get Open Interest
    def get_open_interest(self, instType, instId='', instFamily=''):
        params = {'instType': instType, 'instId': instId, 'instFamily': instFamily}
        return self._request(GET, PUBLIC_OPEN_INTEREST, params)

    # Get Limit Price
    def get_price_limit(self, instId):
        params = {'instId': instId}
        return self._request(GET, PUBLIC_PRICE_LIMIT, params)

    # Get Option Market Data
    def get_option_summary(self, expTime='', instFamily=''):
        params = {'expTime': expTime, 'instFamily': instFamily}
        return self._request(GET, PUBLIC_OPT_SUMMARY, params)

    # Get Discount Rate And Interest-Free Quota
    def discount_rate_interest_free_quota(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, PUBLIC_DISCOUNT_RATE_INTEREST_FREE_QUOTA, params)

    # Get Mark Price
    def get_mark_price(self, instType, instId='', instFamily=''):
        params = {'instType': instType, 'instId': instId, 'instFamily': instFamily}
        return self._request(GET, PUBLIC_MARK_PRICE, params)

    # Get position tiers
    def get_position_tiers(self, instType, tdMode, instFamily='', instId='', ccy='', tier=''):
        params = {'instType': instType, 'tdMode': tdMode, 'instId': instId, 'ccy': ccy, 'tier': tier,
                  'instFamily': instFamily}
        return self._request(GET, PUBLIC_POSITION_TIERS, params)

    # Get interest rate and loan quota
    def get_interest_rate_loan_quota(self, payload):
        return self._request(GET, PUBLIC_INTEREST_RATE_LOAN_QUOTA, payload)

    # Get underlying
    def get_underlying(self, instType=''):
        params = {
            'instType': instType
        }
        return self._request(GET, PUBLIC_UNDERLYING, params)

    # Get insurance fund
    def get_insurance_fund(self, instType='', type='', instFamily='', ccy='', before='', after='', limit=''):
        params = {
            'instType': instType,
            'type': type,
            'instFamily': instFamily,
            'ccy': ccy,
            'before': before,
            'after': after,
            'limit': limit,
            'instFamily': instFamily
        }
        return self._request(GET, PUBLIC_INSURANCE_FUND, params)

    # Unit convert
    def unit_convert(self, type='', instId='', sz='', px='', unit='', opType=''):
        params = {
            'type': type,
            'instId': instId,
            'sz': sz,
            'px': px,
            'unit': unit,
            'opType': opType
        }
        return self._request(GET, PUBLIC_CONVERT_CONTRACT_COIN, params)

    # Get option tick bands
    def get_option_tick_bands(self, instType, instFamily=''):
        params = {
            'instType': instType,
            'instFamily': instFamily
        }
        return self._request(GET, PUBLIC_INSTRUMENT_TICK_BANDS, params)
    
    # Get premium history
    def get_premium_history(self, instId, after='', before='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, PUBLIC_PREMIUM_HISTORY, params)

    # Get Index Tickers
    def get_index_tickers(self, quoteCcy='', instId=''):
        params = {'quoteCcy': quoteCcy, 'instId': instId}
        return self._request(GET, MARKET_INDEX_TICKERS, params)

    # Get Index Candlesticks
    def get_index_candlesticks(self, instId, bar='', after='', before='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, MARKET_INDEX_CANDLES, params)

    # Get Index Candlesticks History
    def get_index_candlesticks_history(self, instId, bar='', after='', before='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, MARKET_HISTORY_INDEX_CANDLES, params)

    # Get Mark Price Candlesticks
    def get_mark_price_candlesticks(self, instId, bar='', after='', before='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, MARKET_MARK_PRICE_CANDLES, params)

    # Get Mark Price Candlesticks History
    def get_mark_price_candlesticks_history(self, instId, bar='', after='', before='', limit=''):
        params = {'instId': instId, 'after': after, 'before': before, 'bar': bar, 'limit': limit}
        return self._request(GET, MARKET_HISTORY_MARK_PRICE_CANDLES, params)

    # Get exchange rate
    def get_exchange_rate(self):
        return self._request(GET, MARKET_EXCHANGE_RATE)

    # Get index components
    def get_index_components(self, index):
        param = {
            'index': index
        }
        return self._request(GET, MARKET_INDEX_COMPONENTS, param)

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
