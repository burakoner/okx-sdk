from .BaseClient import OkxBaseClient
from ..constants import *


class RecurringBuyClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    # - Place recurring buy order
    def place_recurring_buy_order(self, stgyName='', recurringList=[], period='', recurringDay='', recurringTime='',
                                  timeZone='', amt='', investmentCcy='', tdMode='', algoClOrdId=''):
        params = {'stgyName': stgyName, 'recurringList': recurringList, 'period': period, 'recurringDay': recurringDay,
                  'recurringTime': recurringTime,
                  'timeZone': timeZone, 'amt': amt, 'investmentCcy': investmentCcy, 'tdMode': tdMode,
                  'algoClOrdId': algoClOrdId, 'tag': BROKER_ID}
        return self._request(POST, RECURRING_ORDER_ALGO, params)

    # - Amend recurring buy order
    def amend_recurring_buy_order(self, algoId='', stgyName=''):
        params = {'algoId': algoId, 'stgyName': stgyName}
        return self._request(POST, RECURRING_AMEND_ORDER_ALGO, params)

    # - Stop recurring buy order
    def stop_recurring_buy_order(self, orders_data):
        return self._request(POST, RECURRING_STOP_ORDER_ALGO, orders_data)

    # - Get recurring buy order list
    def get_recurring_buy_order_list(self, algoId='', after='', before='', limit=''):
        params = {
            'algoId': algoId,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, RECURRING_ORDERS_ALGO_PENDING, params)

    # - Get recurring buy order history
    def get_recurring_buy_order_history(self, algoId='', after='', before='', limit=''):
        params = {
            'algoId': algoId,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, RECURRING_ORDERS_ALGO_HISTORY, params)

    # - Get recurring buy order details
    def get_recurring_buy_order_details(self, algoId=''):
        params = {'algoId': algoId}
        return self._request(GET, RECURRING_ORDERS_ALGO_DETAILS, params)

    # - Get recurring buy sub orders
    def get_recurring_buy_sub_orders(self, algoId='', ordId='', after='', before='', limit=''):
        params = {
            'algoId': algoId,
            'ordId': ordId,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, RECURRING_SUB_ORDERS, params)
