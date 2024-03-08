from .BaseClient import OkxBaseClient
from ..constants import *


class CopyTradingClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    # Get existing leading positions
    def get_existing_leading_positions(self, instId=''):
        params = {'instId': instId}
        return self._request(GET, COPYTRADING_CURRENT_SUBPOSITIONS, params)

    # Get leading position history
    def get_leading_position_history(self, instId='', after='', before='', limit=''):
        params = {
            'instId': instId,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, COPYTRADING_SUBPOSITIONS_HISTORY, params)

    # Place leading stop order
    def place_leading_stop_order(self, subPosId='', tpTriggerPx='', slTriggerPx='', tpTriggerPxType='',
                                 slTriggerPxType=''):
        params = {
            'subPosId': subPosId,
            'tpTriggerPx': tpTriggerPx,
            'slTriggerPx': slTriggerPx,
            'tpTriggerPxType': tpTriggerPxType,
            'slTriggerPxType': slTriggerPxType
        }
        return self._request(POST, COPYTRADING_ALGO_ORDER, params)

    # Close leading position
    def close_leading_position(self, subPosId=''):
        params = {'subPosId': subPosId}
        return self._request(POST, COPYTRADING_CLOSE_SUBPOSITION, params)

    # Get leading instruments
    def get_leading_instruments(self):
        return self._request(GET, COPYTRADING_INSTRUMENTS)

    # Amend leading instruments
    def amend_leading_instruments(self, instId=''):
        params = {'instId': instId}
        return self._request(POST, COPYTRADING_SET_INSTRUMENTS, params)

    # Get profit sharing details
    def get_profit_sharing_details(self, after='', before='', limit=''):
        params = {
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, COPYTRADING_PROFIT_SHARING_DETAILS, params)

    # Get total profit sharing
    def get_total_profit_sharing(self):
        return self._request(GET, COPYTRADING_TOTAL_PROFIT_SHARING)

    # Get unrealized profit sharing details
    def get_unrealized_profit_sharing_details(self):
        return self._request(GET, COPYTRADING_UNREALIZED_PROFIT_SHARING_DETAILS)

    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
    # TODO
