from .BaseClient import OkxBaseClient
from ..constants import *


class SignalTradingClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    # Create signal
    def create_signal(self, signalChanName, signalChanDesc=''):
        params = {'signalChanName': signalChanName, 'signalChanDesc': signalChanDesc}
        return self._request(POST, SIGNAL_CREATE_SIGNAL, params)
    
    # Get signals
    def get_signals(self, signalSourceType, signalChanId='', after='', before='', limit=''):
        params = {'signalSourceType': signalSourceType, 'signalChanId': signalChanId, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, SIGNAL_SIGNALS, params)
    
    # Create signal bot
    def create(self, signalChanId, lever, investAmt, subOrdType, includeAll='', instIds='', ratio='', entrySettingParam={},exitSettingParam={}):
        params = {'signalChanId': signalChanId, 'lever': lever, 'investAmt': investAmt, 'subOrdType': subOrdType, 'includeAll': includeAll, 'instIds': instIds, 'ratio': ratio, 'entrySettingParam': entrySettingParam, 'exitSettingParam': exitSettingParam}
        return self._request(POST, SIGNAL_ORDER_ALGO, params)
    
    # Cancel signal bot
    def cancel(self, algoId):
        params = {'algoId': algoId}
        return self._request(POST, SIGNAL_STOP_ORDER_ALGO, params)
    
    # Adjust margin balance
    def adjust_margin_balance(self, algoId, type, amt, allowReinvest=False):
        params = {'algoId': algoId, 'type': type, 'amt': amt, 'allowReinvest': allowReinvest}
        return self._request(POST, SIGNAL_MARGIN_BALANCE, params)
    
    # Amend TP SL
    def amend_tpsl(self, algoId, exitSettingParam={}):
        params = {'algoId': algoId, 'exitSettingParam': exitSettingParam}
        return self._request(POST, SIGNAL_AMEND_TPSL, params)
    
    # Set instruments
    def set_instruments(self, algoId, instIds=[], includeAll=False):
        params = {'algoId': algoId, 'instIds': instIds, 'includeAll': includeAll}
        return self._request(POST, SIGNAL_SET_INSTRUMENTS, params)
    
    # Get Signal bot order details
    def get_order(self, algoOrdType, algoId):
        params = {'algoOrdType': algoOrdType,'algoId': algoId}
        return self._request(GET, SIGNAL_ORDERS_ALGO_DETAILS_01, params)
    
    # Get Active signal bot
    def get_active(self, algoOrdType, algoId, after='', before='', limit=''):
        params = {'algoOrdType': algoOrdType,'algoId': algoId, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, SIGNAL_ORDERS_ALGO_DETAILS_02, params)
    
    # Get Signal bot history
    def get_history(self, algoOrdType, algoId, after='', before='', limit=''):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, SIGNAL_ORDERS_ALGO_HISTORY, params)
    
    # Get Signal bot order positions
    def get_positions(self, algoOrdType, algoId):
        params = {'algoOrdType': algoOrdType, 'algoId': algoId}
        return self._request(GET, SIGNAL_POSITIONS, params)
    
    # Get Signal bot order positions
    def get_position_history(self, algoId='', instId='', after='', before='', limit=''):
        params = {'algoId': algoId, 'instId': instId, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, SIGNAL_POSITIONS_HISTORY, params)
    
    # Close position
    def close_position(self, algoId, instId):
        params = {'algoId': algoId, 'instId': instId}
        return self._request(POST, SIGNAL_CLOSE_POSITION, params)
    
    # Place sub order
    def place_sub_order(self, algoId, instId, side, ordType, sz, px='', reduceOnly=False):
        params = {'algoId': algoId, 'instId': instId, 'side': side, 'ordType': ordType, 'sz': sz, 'px': px, 'reduceOnly': reduceOnly}
        return self._request(POST, SIGNAL_SUB_ORDER, params)
    
    # Cancel sub order
    def cancel_sub_order(self, algoId, instId, signalOrdId):
        params = {'algoId': algoId, 'instId': instId, 'signalOrdId': signalOrdId}
        return self._request(POST, SIGNAL_CANCEL_SUB_ORDER, params)
    
    # Get sub orders
    def get_sub_orders(self, algoId, algoOrdType, type='', clOrdId='', state='', signalOrdId='', after='', before='', begin='', end='', limit=''):
        params = {'algoId': algoId, 'algoOrdType': algoOrdType, 'type': type, 'clOrdId': clOrdId, 'state': state, 'signalOrdId': signalOrdId, 'after': after, 'before': before, 'begin': begin, 'end': end, 'limit': limit}
        return self._request(GET, SIGNAL_SUB_ORDERS, params)
    
    # Get bot events
    def get_bot_events(self, algoId, after='', before='', limit=''):
        params = {'algoId': algoId, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, SIGNAL_EVENT_HISTORY, params)
    