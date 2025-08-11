from .BaseClient import OkxBaseClient
from ..constants import *


class GridTradingClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase,
                               use_server_time, simulation, domain, debug, proxy)

    def place_order(self, instId, algoOrdType, maxPx, minPx, gridNum, runType='', tpTriggerPx='',
                    slTriggerPx='', algoClOrdId='', profitSharingRatio='', triggerParams=[],
                    quoteSz='', baseSz='', sz='', direction='', lever='', basePos='', tpRatio='', slRatio=''):
        params = {'instId': instId, 'algoOrdType': algoOrdType, 'maxPx': maxPx, 'minPx': minPx, 'gridNum': gridNum,
                  'runType': runType, 'tpTriggerPx': tpTriggerPx, 'slTriggerPx': slTriggerPx, 'algoClOrdId': algoClOrdId,
                  'tag': BROKER_ID, 'profitSharingRatio': profitSharingRatio, 'triggerParams': triggerParams,
                  'quoteSz': quoteSz, 'baseSz': baseSz, 'sz': sz, 'direction': direction, 'lever': lever,
                  'basePos': basePos, 'tpRatio': tpRatio, 'slRatio': slRatio}
        return self._request(POST, GRID_ORDER_ALGO, params)

    def amend_order(self, algoId, instId, slTriggerPx='', tpTriggerPx='', tpRatio='', slRatio='', triggerParams=[]):
        params = {'algoId': algoId, 'instId': instId,
                  'slTriggerPx': slTriggerPx, 'tpTriggerPx': tpTriggerPx, 'tpRatio': tpRatio, 'slRatio': slRatio, 'triggerParams': triggerParams}
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

    def instant_trigger_order(self, algoId):
        params = [{'algoId': algoId}]
        return self._request(POST, GRID_ORDER_INSTANT_TRIGGER, params)

    def get_pending_orders(self, algoOrdType='', algoId='', instId='', instType='', after='', before='',
                           limit=''):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId, 'instId': instId, 'instType': instType, 'after': after,
                  'before': before, 'limit': limit}
        return self._request(GET, GRID_ORDERS_ALGO_PENDING, params)

    def get_orders_history(self, algoOrdType='', algoId='', instId='', instType='', after='', before='',
                           limit=''):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId, 'instId': instId, 'instType': instType, 'after': after,
                  'before': before, 'limit': limit}
        return self._request(GET, GRID_ORDERS_ALGO_HISTORY, params)

    def get_order_details(self, algoOrdType='', algoId=''):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId}
        return self._request(GET, GRID_ORDERS_ALGO_DETAILS, params)

    def get_sub_orders(self, algoId='', algoOrdType='', type='', groupId='', after='', before='', limit=''):
        params = {'algoId': algoId, 'algoOrdType': algoOrdType, 'type': type, 'groupId': groupId, 'after': after,
                  'before': before, 'limit': limit}
        return self._request(GET, GRID_SUB_ORDERS, params)

    def get_positions(self, algoOrdType, algoId):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId}
        return self._request(GET, GRID_POSITIONS, params)

    def withdraw_income(self, algoId):
        params = {'algoId': algoId}
        return self._request(POST, GRID_WITHDRAW_INCOME, params)

    def compute_margin_balance(self, algoId, type, amt=''):
        params = {
            'algoId': algoId,
            'type': type,
            'amt': amt
        }
        return self._request(POST, GRID_COMPUTE_MARGIN_BALANCE, params)

    def adjust_margin_balance(self, algoId, type, amt='', percent=''):
        params = {
            'algoId': algoId,
            'type': type,
            'amt': amt,
            'percent': percent
        }
        return self._request(POST, GRID_MARGIN_BALANCE, params)

    def add_investment(self, algoId,  amt, allowReinvestProfit=''):
        params = {
            'algoId': algoId,
            'amt': amt,
            'allowReinvestProfit': allowReinvestProfit
        }
        return self._request(POST, GRID_ADJUST_INVESTMENT, params)

    def get_ai_param(self, algoOrdType='', instId='', direction='', duration=''):
        params = {
            'algoOrdType': algoOrdType,
            'instId': instId,
            'direction': direction,
            'duration': duration
        }
        return self._request(GET, GRID_AI_PARAM, params)

    def compute_min_investment(self, instId, algoOrdType, maxPx, minPx, gridNum, runType, direction='', lever='', basePos='', investmentType='', triggerStrategy='', investmentData=[]):
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
            'investmentType': investmentType,
            'triggerStrategy': triggerStrategy,
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
    
    def get_max_grid_quantity(self, instId, runType, algoOrdType, maxPx, minPx, lever=''):
        params = {
            'instId': instId,
            'runType': runType,
            'algoOrdType': algoOrdType,
            'maxPx': maxPx,
            'minPx': minPx,
            'lever': lever,
        }
        return self._request(GET, GRID_QUANTITY, params)
    