from .BaseClient import OkxBaseClient
from ..constants import *


class AlgoTradingClient(OkxBaseClient):

    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase,
                               use_server_time, simulation, domain, debug, proxy)

    # Place Algo Order
    def place_order(self, instId, tdMode, side, ordType,
                         ccy='', posSide='', sz='', tgtCcy='', algoClOrdId='', closeFraction='', tradeQuoteCcy=''):
        params = {'instId': instId, 'tdMode': tdMode, 'side': side, 'ordType': ordType, 'sz': sz, 'ccy': ccy,
                  'posSide': posSide, 'tgtCcy': tgtCcy, 'algoClOrdId': algoClOrdId, 'closeFraction': closeFraction,
                  'tradeQuoteCcy': tradeQuoteCcy}
        return self._request(POST, TRADE_PLACE_ALGO_ORDER, params)

    # Cancel Algo Order
    def cancel_order(self, payload=[]):
        return self._request(POST, TRADE_CANCEL_ALGOS, payload)

    # Amend algo order
    def amend_order(self, instId='', algoId='', algoClOrdId='', cxlOnFail='', reqId='', newSz='',
                         newTpTriggerPx='', newTpOrdPx='', newSlTriggerPx='', newSlOrdPx='', newTpTriggerPxType='', newSlTriggerPxType='',
                         newTriggerPx='', newOrdPx='', newTriggerPxType='', attachAlgoOrds=[]):
        params = {'instId': instId, 'algoId': algoId, 'algoClOrdId': algoClOrdId, 'cxlOnFail': cxlOnFail, 'reqId': reqId, 'newSz': newSz,
                  'newTpTriggerPx': newTpTriggerPx, 'newTpOrdPx': newTpOrdPx, 'newSlTriggerPx': newSlTriggerPx, 'newSlOrdPx': newSlOrdPx, 'newTpTriggerPxType': newTpTriggerPxType, 'newSlTriggerPxType': newSlTriggerPxType,
                  'newTriggerPx': newTriggerPx, 'newOrdPx': newOrdPx, 'newTriggerPxType': newTriggerPxType, 'attachAlgoOrds': attachAlgoOrds}
        return self._request(POST, TRADE_AMEND_ALGOS, params)

    # Get algo order details
    def get_order(self, algoId='', algoClOrdId=''):
        params = {'algoId': algoId, 'algoClOrdId': algoClOrdId}
        return self._request(GET, TRADE_GET_ALGO_ORDER, params)

    # Get Algo Order List
    def get_pending_orders(self, ordType='', algoId='', instType='', instId='', after='', before='', limit=''):
        params = {'ordType': ordType, 'algoId': algoId, 'instType': instType, 'instId': instId, 'after': after,
                  'before': before, 'limit': limit}
        return self._request(GET, TRADE_ORDERS_ALGO_PENDING, params)

    # Get Algo Order History
    def get_order_history(self, ordType, state='', algoId='', instType='', instId='', after='', before='', limit=''):
        params = {'ordType': ordType, 'state': state, 'algoId': algoId, 'instType': instType, 'instId': instId,
                  'after': after, 'before': before, 'limit': limit}
        return self._request(GET, TRADE_ORDERS_ALGO_HISTORY, params)
