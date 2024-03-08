from .BaseClient import OkxBaseClient
from ..constants import *


class AlgoTradingClient(OkxBaseClient):

    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase,
                               use_server_time, simulation, domain, debug, proxy)

    # Place Algo Order
    def place_algo_order(self, instId='', tdMode='', side='', ordType='', sz='', ccy='',
                         posSide='', reduceOnly='', tpTriggerPx='',
                         tpOrdPx='', slTriggerPx='', slOrdPx='',
                         triggerPx='', orderPx='', tgtCcy='', pxVar='',
                         pxSpread='',
                         szLimit='', pxLimit='', timeInterval='', tpTriggerPxType='', slTriggerPxType='',
                         callbackRatio='', callbackSpread='', activePx='', triggerPxType='', closeFraction='', quickMgnType='', algoClOrdId=''):
        params = {'instId': instId, 'tdMode': tdMode, 'side': side, 'ordType': ordType, 'sz': sz, 'ccy': ccy,
                  'posSide': posSide, 'reduceOnly': reduceOnly, 'tpTriggerPx': tpTriggerPx, 'tpOrdPx': tpOrdPx,
                  'slTriggerPx': slTriggerPx, 'slOrdPx': slOrdPx, 'triggerPx': triggerPx, 'orderPx': orderPx,
                  'tgtCcy': tgtCcy, 'pxVar': pxVar, 'szLimit': szLimit, 'pxLimit': pxLimit,
                  'timeInterval': timeInterval,
                  'pxSpread': pxSpread, 'tpTriggerPxType': tpTriggerPxType, 'slTriggerPxType': slTriggerPxType,
                  'callbackRatio': callbackRatio, 'callbackSpread': callbackSpread, 'activePx': activePx,
                  'tag': BROKER_ID, 'triggerPxType': triggerPxType, 'closeFraction': closeFraction,
                  'quickMgnType': quickMgnType, 'algoClOrdId': algoClOrdId}
        return self._request(POST, TRADE_PLACE_ALGO_ORDER, params)

    # Cancel Algo Order
    def cancel_algo_order(self, params):
        return self._request(POST, TRADE_CANCEL_ALGOS, params)

    # Amend algo order
    def amend_algo_order(self, instId='', algoId='', algoClOrdId='', cxlOnFail='', reqId='', newSz='',
                         newTpTriggerPx='', newTpOrdPx='', newSlTriggerPx='', newSlOrdPx='', newTpTriggerPxType='',
                         newSlTriggerPxType=''):
        params = {'instId': instId, 'algoId': algoId, 'algoClOrdId': algoClOrdId, 'cxlOnFail': cxlOnFail,
                  'reqId': reqId, 'newSz': newSz, 'newTpTriggerPx': newTpTriggerPx, 'newTpOrdPx': newTpOrdPx,
                  'newSlTriggerPx': newSlTriggerPx, 'newSlOrdPx': newSlOrdPx,
                  'newTpTriggerPxType': newTpTriggerPxType, 'newSlTriggerPxType': newSlTriggerPxType}
        return self._request(POST, TRADE_AMEND_ALGOS, params)

    # Cancel Advance Algos
    def cancel_advance_algos(self, params):
        return self._request(POST, TRADE_CANCEL_ADVANCE_ALGOS, params)

    # Get algo order details
    def get_algo_order_details(self, algoId='', algoClOrdId=''):
        params = {'algoId': algoId, 'algoClOrdId': algoClOrdId}
        return self._request(GET, TRADE_GET_ALGO_ORDER, params)

    # Get Algo Order List
    def order_algos_list(self, ordType='', algoId='', instType='', instId='', after='', before='', limit='',
                         algoClOrdId=''):
        params = {'ordType': ordType, 'algoId': algoId, 'instType': instType, 'instId': instId, 'after': after,
                  'before': before, 'limit': limit, 'algoClOrdId': algoClOrdId}
        return self._request(GET, TRADE_ORDERS_ALGO_PENDING, params)

    # Get Algo Order History
    def order_algos_history(self, ordType, state='', algoId='', instType='', instId='', after='', before='', limit=''):
        params = {'ordType': ordType, 'state': state, 'algoId': algoId, 'instType': instType, 'instId': instId,
                  'after': after, 'before': before, 'limit': limit}
        return self._request(GET, TRADE_ORDERS_ALGO_HISTORY, params)
