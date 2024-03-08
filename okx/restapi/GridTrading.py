from .BaseClient import OkxBaseClient
from ..constants import *


class GridTradingClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase,
                               use_server_time, simulation, domain, debug, proxy)

    def place_order(self, instId, algoOrdType, maxPx, minPx, gridNum, runType='', tpTriggerPx='',
                    slTriggerPx='', quoteSz='', baseSz='', sz='', direction='', lever='', basePos=''):
        params = {'instId': instId, 'algoOrdType': algoOrdType, 'maxPx': maxPx, 'minPx': minPx, 'gridNum': gridNum,
                  'runType': runType, 'tpTriggerPx': tpTriggerPx, 'slTriggerPx': slTriggerPx, 'tag': BROKER_ID,
                  'quoteSz': quoteSz, 'baseSz': baseSz, 'sz': sz, 'direction': direction, 'lever': lever,
                  'basePos': basePos}
        return self._request(POST, GRID_ORDER_ALGO, params)

    def amend_order(self, algoId, instId, slTriggerPx='', tpTriggerPx=''):
        params = {'algoId': algoId, 'instId': instId,
                  'slTriggerPx': slTriggerPx, 'tpTriggerPx': tpTriggerPx}
        return self._request(POST, GRID_AMEND_ORDER_ALGO, params)

    def stop_order(self, algoId, instId, algoOrdType, stopType):
        params = [{'algoId': algoId, 'instId': instId,
                   'algoOrdType': algoOrdType, 'stopType': stopType}]
        return self._request(POST, GRID_STOP_ORDER_ALGO, params)

    def close_position(self, algoId, mktClose, sz='', px=''):
        params = [{'algoId': algoId, 'mktClose': mktClose, 'sz': sz, 'px': px}]
        return self._request(POST, GRID_CLOSE_POSITION, params)

    def cancel_close_position_order(self, algoId, ordId):
        params = [{'algoId': algoId, 'ordId': ordId}]
        return self._request(POST, GRID_CANCEL_CLOSE_ORDER, params)

    def get_pending_orders(self, algoOrdType='', algoId='', instId='', instType='', after='', before='',
                           limit='', instFamily=''):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId, 'instId': instId, 'instType': instType, 'after': after,
                  'before': before, 'limit': limit, 'instFamily': instFamily}
        return self._request(GET, GRID_ORDERS_ALGO_PENDING, params)

    def get_orders_history(self, algoOrdType='', algoId='', instId='', instType='', after='', before='',
                           limit='', instFamily=''):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId, 'instId': instId, 'instType': instType, 'after': after,
                  'before': before, 'limit': limit, 'instFamily': instFamily}
        return self._request(GET, GRID_ORDERS_ALGO_HISTORY, params)

    def get_orders_details(self, algoOrdType='', algoId=''):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId}
        return self._request(GET, GRID_ORDERS_ALGO_DETAILS, params)

    def get_sub_orders(self, algoId='', algoOrdType='', type='', groupId='', after='', before='', limit=''):
        params = {'algoId': algoId, 'algoOrdType': algoOrdType, 'type': type, 'groupId': groupId, 'after': after,
                  'before': before, 'limit': limit}
        return self._request(GET, GRID_SUB_ORDERS, params)

    def get_positions(self, algoOrdType='', algoId=''):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId}
        return self._request(GET, GRID_POSITIONS, params)

    def withdraw_income(self, algoId=''):
        params = {'algoId': algoId}
        return self._request(POST, GRID_WITHDRAW_INCOME, params)

    def compute_margin_balance(self, algoId='', type='', amt=''):
        params = {
            'algoId': algoId,
            'type': type,
            'amt': amt
        }
        return self._request(POST, GRID_COMPUTE_MARGIN_BALANCE, params)

    def adjust_margin_balance(self, algoId='', type='', amt='', percent=''):
        params = {
            'algoId': algoId,
            'type': type,
            'amt': amt,
            'percent': percent
        }
        return self._request(POST, GRID_MARGIN_BALANCE, params)

    def get_ai_param(self, algoOrdType='', instId='', direction='', duration=''):
        params = {
            'algoOrdType': algoOrdType,
            'instId': instId,
            'direction': direction,
            'duration': duration
        }
        return self._request(GET, GRID_AI_PARAM, params)

    def compute_min_investment(self, instId, algoOrdType, maxPx, minPx, gridNum, runType, direction='', lever='', basePos='', investmentData=[]):
        params = {
            'instId': instId,
            'algoOrdType': algoOrdType,
            'maxPx': maxPx,
            'minPx': minPx,
            'gridNum': gridNum,
            'runType': runType,
            'direction': direction,
            'lever': lever,
            'basePos': basePos,
            'investmentData': investmentData,
        }
        return self._request(POST, GRID_MIN_INVESTMENT, params)

    def get_rsi_back_testing(self, instId, timeframe, thold, timePeriod, triggerCond='', duration=''):
        params = {
            'instId': instId,
            'timeframe': timeframe,
            'thold': thold,
            'timePeriod': timePeriod,
            'triggerCond': triggerCond,
            'duration': duration,
        }
        return self._request(GET, GRID_AI_PARAM, params)