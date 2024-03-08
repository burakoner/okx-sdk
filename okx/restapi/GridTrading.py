from .BaseClient import OkxBaseClient
from ..constants import *


class GridTradingClient(OkxBaseClient):
    def __init__(self, api_key='', api_secret_key='', pass_phrase='', use_server_time=False, simulation=False,
                 domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, api_key, api_secret_key, pass_phrase, use_server_time, simulation, domain, debug,
                               proxy)

    def grid_order_algo(self, instId='', algoOrdType='', maxPx='', minPx='', gridNum='', runType='', tpTriggerPx='',
                        slTriggerPx='', quoteSz='', baseSz='', sz='', direction='', lever='', basePos=''):
        params = {'instId': instId, 'algoOrdType': algoOrdType, 'maxPx': maxPx, 'minPx': minPx, 'gridNum': gridNum,
                  'runType': runType, 'tpTriggerPx': tpTriggerPx, 'slTriggerPx': slTriggerPx, 'tag': BROKER_ID,
                  'quoteSz': quoteSz, 'baseSz': baseSz, 'sz': sz, 'direction': direction, 'lever': lever,
                  'basePos': basePos}
        return self._request(POST, GRID_ORDER_ALGO, params)

    def grid_amend_order_algo(self, algoId='', instId='', slTriggerPx='', tpTriggerPx=''):
        params = {'algoId': algoId, 'instId': instId, 'slTriggerPx': slTriggerPx, 'tpTriggerPx': tpTriggerPx}
        return self._request(POST, GRID_AMEND_ORDER_ALGO, params)

    def grid_stop_order_algo(self, algoId='', instId='', algoOrdType='', stopType=''):
        params = [{'algoId': algoId, 'instId': instId, 'algoOrdType': algoOrdType, 'stopType': stopType}]
        return self._request(POST, GRID_STOP_ORDER_ALGO, params)

    # TODO
    # TODO

    def grid_orders_algo_pending(self, algoOrdType='', algoId='', instId='', instType='', after='', before='',
                                 limit='', instFamily=''):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId, 'instId': instId, 'instType': instType, 'after': after,
                  'before': before, 'limit': limit, 'instFamily': instFamily}
        return self._request(GET, GRID_ORDERS_ALGO_PENDING, params)

    def grid_orders_algo_history(self, algoOrdType='', algoId='', instId='', instType='', after='', before='',
                                 limit='', instFamily=''):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId, 'instId': instId, 'instType': instType, 'after': after,
                  'before': before, 'limit': limit, 'instFamily': instFamily}
        return self._request(GET, GRID_ORDERS_ALGO_HISTORY, params)

    def grid_orders_algo_details(self, algoOrdType='', algoId=''):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId}
        return self._request(GET, GRID_ORDERS_ALGO_DETAILS, params)

    def grid_sub_orders(self, algoId='', algoOrdType='', type='', groupId='', after='', before='', limit=''):
        params = {'algoId': algoId, 'algoOrdType': algoOrdType, 'type': type, 'groupId': groupId, 'after': after,
                  'before': before, 'limit': limit}
        return self._request(GET, GRID_SUB_ORDERS, params)

    def grid_positions(self, algoOrdType='', algoId=''):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId}
        return self._request(GET, GRID_POSITIONS, params)

    def grid_withdraw_income(self, algoId=''):
        params = {'algoId': algoId}
        return self._request(POST, GRID_WITHDRAW_INCOME, params)

    def grid_compute_margin_balance(self, algoId='', type='', amt=''):
        params = {
            'algoId': algoId,
            'type': type,
            'amt': amt
        }
        return self._request(POST, GRID_COMPUTE_MARGIN_BALANCE, params)

    def grid_adjust_margin_balance(self, algoId='', type='', amt='', percent=''):
        params = {
            'algoId': algoId,
            'type': type,
            'amt': amt,
            'percent': percent
        }
        return self._request(POST, GRID_MARGIN_BALANCE, params)

    def grid_ai_param(self, algoOrdType='', instId='', direction='', duration=''):
        params = {
            'algoOrdType': algoOrdType,
            'instId': instId,
            'direction': direction,
            'duration': duration
        }
        return self._request(GET, GRID_AI_PARAM, params)

    # TODO
    # TODO
