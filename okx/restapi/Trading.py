from .BaseClient import OkxBaseClient
from ..constants import *


class TradingClient(OkxBaseClient):

    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase,
                               use_server_time, simulation, domain, debug, proxy)

    # Place Order
    def place_order(self, instId, tdMode, side, ordType, sz, ccy='', clOrdId='', posSide='', px='',
                    reduceOnly='', tgtCcy='', tpTriggerPx='', tpOrdPx='', slTriggerPx='', slOrdPx='',
                    tpTriggerPxType='', slTriggerPxType='', quickMgnType='', stpId='', stpMode='',
                    attachAlgoOrds=None):
        params = {'instId': instId, 'tdMode': tdMode, 'side': side, 'ordType': ordType, 'sz': sz, 'ccy': ccy,
                  'clOrdId': clOrdId, 'tag': BROKER_ID, 'posSide': posSide, 'px': px, 'reduceOnly': reduceOnly,
                  'tgtCcy': tgtCcy, 'tpTriggerPx': tpTriggerPx, 'tpOrdPx': tpOrdPx, 'slTriggerPx': slTriggerPx,
                  'slOrdPx': slOrdPx, 'tpTriggerPxType': tpTriggerPxType, 'slTriggerPxType': slTriggerPxType,
                  'quickMgnType': quickMgnType, 'stpId': stpId, 'stpMode': stpMode, 'attachAlgoOrds': attachAlgoOrds}
        return self._request(POST, TRADE_PLACE_ORDER, params)

    # Place Multiple Orders
    def place_multiple_orders(self, orders_data):
        return self._request(POST, TRADE_BATCH_ORDERS, orders_data)

    # Cancel Order
    def cancel_order(self, instId, ordId='', clOrdId=''):
        params = {'instId': instId, 'ordId': ordId, 'clOrdId': clOrdId}
        return self._request(POST, TRADE_CANCEL_ORDER, params)

    # Cancel Multiple Orders
    def cancel_multiple_orders(self, orders_data):
        return self._request(POST, TRADE_CANCEL_BATCH_ORDERS, orders_data)

    # Amend Order
    def amend_order(self, instId, cxlOnFail='', ordId='', clOrdId='', reqId='', newSz='', newPx='', newTpTriggerPx='',
                    newTpOrdPx='', newSlTriggerPx='', newSlOrdPx='', newTpTriggerPxType='', newSlTriggerPxType='',
                    attachAlgoOrds=''):
        params = {'instId': instId, 'cxlOnFailc': cxlOnFail, 'ordId': ordId, 'clOrdId': clOrdId, 'reqId': reqId,
                  'newSz': newSz, 'newPx': newPx, 'newTpTriggerPx': newTpTriggerPx, 'newTpOrdPx': newTpOrdPx,
                  'newSlTriggerPx': newSlTriggerPx, 'newSlOrdPx': newSlOrdPx, 'newTpTriggerPxType': newTpTriggerPxType,
                  'newSlTriggerPxType': newSlTriggerPxType}
        params['attachAlgoOrds'] = attachAlgoOrds
        return self._request(POST, TRADE_AMEND_ORDER, params)

    # Amend Multiple Orders
    def amend_multiple_orders(self, orders_data):
        return self._request(POST, TRADE_AMEND_BATCH_ORDER, orders_data)

    # Close Positions
    def close_positions(self, instId, mgnMode, posSide='', ccy='', autoCxl='', clOrdId=''):
        params = {'instId': instId, 'mgnMode': mgnMode, 'posSide': posSide, 'ccy': ccy, 'autoCxl': autoCxl,
                  'clOrdId': clOrdId, 'tag': BROKER_ID}
        return self._request(POST, TRADE_CLOSE_POSITION, params)

    # Get Order Details
    def get_order(self, instId, ordId='', clOrdId=''):
        params = {'instId': instId, 'ordId': ordId, 'clOrdId': clOrdId}
        return self._request(GET, TRADE_GET_ORDER, params)

    # Get Order List
    def get_order_list(self, instType='', uly='', instId='', ordType='', state='', after='', before='', limit='',
                       instFamily=''):
        params = {'instType': instType, 'uly': uly, 'instId': instId, 'ordType': ordType, 'state': state,
                  'after': after, 'before': before, 'limit': limit, 'instFamily': instFamily}
        return self._request(GET, TRADE_ORDERS_PENDING, params)

    # Get Order History (last 7 days）
    def get_orders_history(self, instType, uly='', instId='', ordType='', state='', after='', before='', begin='',
                           end='', limit='', instFamily=''):
        params = {'instType': instType, 'uly': uly, 'instId': instId, 'ordType': ordType, 'state': state,
                  'after': after, 'before': before, 'begin': begin, 'end': end, 'limit': limit,
                  'instFamily': instFamily}
        return self._request(GET, TRADE_ORDERS_HISTORY, params)

    # Get Order History (last 3 months)
    def get_orders_history_archive(self, instType, uly='', instId='', ordType='', state='', after='', before='',
                                   begin='', end='', limit='', instFamily=''):
        params = {'instType': instType, 'uly': uly, 'instId': instId, 'ordType': ordType, 'state': state,
                  'after': after, 'before': before, 'begin': begin, 'end': end, 'limit': limit,
                  'instFamily': instFamily}
        return self._request(GET, TRADE_ORDERS_HISTORY_ARCHIVE, params)

    # Get Transaction Details (last 3 days）
    def get_fills(self, instType='', uly='', instId='', ordId='', after='', before='', limit='', instFamily=''):
        params = {'instType': instType, 'uly': uly, 'instId': instId, 'ordId': ordId, 'after': after, 'before': before,
                  'limit': limit, 'instFamily': instFamily}
        return self._request(GET, TRADE_FILLS, params)

    # Get Transaction Details (last 3 months)
    def get_fills_history(self, instType, uly='', instId='', ordId='', after='', before='', limit='', instFamily=''):
        params = {'instType': instType, 'uly': uly, 'instId': instId, 'ordId': ordId, 'after': after, 'before': before,
                  'limit': limit, 'instFamily': instFamily}
        return self._request(GET, TRADE_FILLS_HISTORY, params)

    def apply_fills_archive(self, year, quarter):
        params = {'year': year, 'quarter': quarter}
        return self._request(POST, TRADE_APPLY_ORDERS_FILLS_ARCHIVE, params)

    def get_fills_archive(self, year, quarter):
        params = {'year': year, 'quarter': quarter}
        return self._request(GET, TRADE_RETRIEVE_ORDERS_FILLS_ARCHIVE, params)

    def get_easy_convert_currency_list(self):
        return self._request(GET, TRADE_EASY_CONVERT_CURRENCY_LIST)

    def easy_convert(self, fromCcy=[], toCcy=''):
        params = {
            'fromCcy': fromCcy,
            'toCcy': toCcy
        }
        return self._request(POST, TRADE_EASY_CONVERT, params)

    def get_easy_convert_history(self, before='', after='', limit=''):
        params = {
            'before': before,
            'after': after,
            'limit': limit
        }
        return self._request(GET, TRADE_CONVERT_EASY_HISTORY, params)

    def get_oneclick_repay_list(self, debtType=''):
        params = {
            'debtType': debtType
        }
        return self._request(GET, TRADE_ONE_CLICK_REPAY_CURRENCY_LIST, params)

    def oneclick_repay(self, debtCcy=[], repayCcy=''):
        params = {
            'debtCcy': debtCcy,
            'repayCcy': repayCcy
        }
        return self._request(POST, TRADE_ONE_CLICK_REPAY, params)

    def oneclick_repay_history(self, after='', before='', limit=''):
        params = {
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, TRADE_ONE_CLICK_REPAY_HISTORY, params)

    def cancel_all_orders(self, instType, instFamily):
        params = {'instType': instType, 'instFamily': instFamily}
        return self._request(POST, TRADE_MASS_CANCEL, params)

    def cancel_all_after(self, timeOut):
        params = {'timeOut': timeOut}
        return self._request(POST, TRADE_CANCEL_ALL_AFTER, params)

    def get_account_rate_limit(self):
        return self._request(GET, TRADE_ACCOUNT_RATE_LIMIT)
