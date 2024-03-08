from .BaseClient import OkxBaseClient
from ..constants import *


class RubikClient(OkxBaseClient):

    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    def get_support_coin(self):
        return self._request(GET, RUBIK_STAT_TRADING_DATA_SUPPORT_COIN)

    def get_taker_volume(self, ccy, instType, begin='', end='', period=''):
        params = {'ccy': ccy, 'instType': instType, 'begin': begin, 'end': end, 'period': period}
        return self._request(GET, RUBIK_STAT_TAKER_VOLUME, params)

    def get_margin_lending_ratio(self, ccy, begin='', end='', period=''):
        params = {'ccy': ccy, 'begin': begin, 'end': end, 'period': period}
        return self._request(GET, RUBIK_STAT_MARGIN_LOAN_RATIO, params)

    def get_long_short_ratio(self, ccy, begin='', end='', period=''):
        params = {'ccy': ccy, 'begin': begin, 'end': end, 'period': period}
        return self._request(GET, RUBIK_STAT_CONTRACTS_LONG_SHORT_RATIO, params)

    def get_contracts_interest_volume(self, ccy, begin='', end='', period=''):
        params = {'ccy': ccy, 'begin': begin, 'end': end, 'period': period}
        return self._request(GET, RUBIK_STAT_CONTRACTS_INTEREST_VOLUME, params)

    def get_options_interest_volume(self, ccy, period=''):
        params = {'ccy': ccy, 'period': period}
        return self._request(GET, RUBIK_STAT_OPTION_OPEN_INTEREST_VOLUME, params)

    def get_put_call_ratio(self, ccy, period=''):
        params = {'ccy': ccy, 'period': period}
        return self._request(GET, RUBIK_STAT_OPTION_OPEN_INTEREST_RATIO, params)

    def get_interest_volume_expiry(self, ccy, period=''):
        params = {'ccy': ccy, 'period': period}
        return self._request(GET, RUBIK_STAT_OPTION_OPEN_INTEREST_VOLUME_EXPIRY, params)

    def get_interest_volume_strike(self, ccy, expTime, period=''):
        params = {'ccy': ccy, 'expTime': expTime, 'period': period}
        return self._request(GET, RUBIK_STAT_OPTION_OPEN_INTEREST_VOLUME_STRIKE, params)

    def get_taker_block_volume(self, ccy, period=''):
        params = {'ccy': ccy, 'period': period}
        return self._request(GET, RUBIK_STAT_OPTION_TAKER_BLOCK_VOLUME, params)
