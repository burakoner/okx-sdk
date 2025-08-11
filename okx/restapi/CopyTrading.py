from .BaseClient import OkxBaseClient
from ..constants import *


class CopyTradingClient(OkxBaseClient):
    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

    # Get existing leading positions
    def get_current_subpositions(self, instType='', instId='', after='', before='', limit=''):
        params = {'instType': instType, 'instId': instId, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, COPYTRADING_CURRENT_SUBPOSITIONS, params)

    # Get leading position history
    def get_subpositions_history(self, instType='', instId='', after='', before='', limit=''):
        params = {
            'instType': instType,
            'instId': instId,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, COPYTRADING_SUBPOSITIONS_HISTORY, params)

    # Place leading stop order
    def place_order(self, subPosId, 
                    instType='', tpTriggerPx='', slTriggerPx='', tpOrdPx='', slOrdPx='',
                    tpTriggerPxType='', slTriggerPxType=''):
        params = {
            'subPosId': subPosId,
            'instType': instType,
            'tpTriggerPx': tpTriggerPx,
            'slTriggerPx': slTriggerPx,
            'tpOrdPx': tpOrdPx,
            'slOrdPx': slOrdPx,
            'tpTriggerPxType': tpTriggerPxType,
            'slTriggerPxType': slTriggerPxType,
            'tag': BROKER_ID
        }
        return self._request(POST, COPYTRADING_ALGO_ORDER, params)

    # Close leading position
    def close_subposition(self, subPosId, instType='', ordType='', px=''):
        params = {'subPosId': subPosId, 'instType': instType, 'ordType': ordType, 'px': px, 'tag': BROKER_ID}
        return self._request(POST, COPYTRADING_CLOSE_SUBPOSITION, params)

    # Get leading instruments
    def get_leading_instruments(self, instType=''):
        params = {'instType': instType}
        return self._request(GET, COPYTRADING_INSTRUMENTS, params)

    # Amend leading instruments
    def set_leading_instruments(self, instId, instType=''):
        params = {'instId': instId, 'instType': instType}
        return self._request(POST, COPYTRADING_SET_INSTRUMENTS, params)

    # Get profit sharing details
    def get_profit_sharing_details(self, instType='', after='', before='', limit=''):
        params = {
            'instType': instType,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, COPYTRADING_PROFIT_SHARING_DETAILS, params)

    # Get total profit sharing
    def get_total_profit_sharing(self, instType=''):
        params = { 'instType': instType }
        return self._request(GET, COPYTRADING_TOTAL_PROFIT_SHARING, params)

    # Get unrealized profit sharing details
    def get_unrealized_profit_sharing_details(self, instType=''):
        params = { 'instType': instType }
        return self._request(GET, COPYTRADING_UNREALIZED_PROFIT_SHARING_DETAILS, params)

    # Get Total unrealized profit sharing
    def get_total_unrealized_profit_sharing(self, instType=''):
        params = { 'instType': instType }
        return self._request(GET, COPYTRADING_TOTAL_UNREALIZED_PROFIT_SHARING, params)
    
    # Amend profit sharing ratio
    def set_profit_sharing_ratio(self, profitSharingRatio, instType=''):
        params = {
            'instType': instType,
            'profitSharingRatio': profitSharingRatio,
        }
        return self._request(POST, COPYTRADING_AMEND_PROFIT_SHARING_RATIO, params)
    
    # Get Account configuration
    def get_account_configuration(self):
        return self._request(GET, COPYTRADING_CONFIG)
    
    # First copy settings
    def first_copy_settings(self, uniqueCode, copyMgnMode, copyInstIdType, 
                            instType='', instId='', copyMode='',copyTotalAmt='', copyAmt='',
                            copyRatio='', tpRatio='', slRatio='', slTotalAmt='', subPosCloseType=''):
        params = {
            'instType': instType,
            'uniqueCode': uniqueCode,
            'copyMgnMode': copyMgnMode,
            'copyInstIdType': copyInstIdType,
            'instId': instId,
            'copyMode': copyMode,
            'copyTotalAmt': copyTotalAmt,
            'copyAmt': copyAmt,
            'copyRatio': copyRatio,
            'tpRatio': tpRatio,
            'slRatio': slRatio,
            'slTotalAmt': slTotalAmt,
            'subPosCloseType': subPosCloseType,
            'tag': BROKER_ID
        }
        return self._request(POST, COPYTRADING_FIRST_COPY_SETTINGS, params)
    
    # Amend copy settings
    def set_copy_settings(self, uniqueCode, copyMgnMode, copyInstIdType, 
                          instType='', instId='', copyMode='',copyTotalAmt='',copyAmt='',
                          copyRatio='', tpRatio='', slRatio='', slTotalAmt='', subPosCloseType=''):
        params = {
            'uniqueCode': uniqueCode,
            'copyMgnMode': copyMgnMode,
            'copyInstIdType': copyInstIdType,
            'instType': instType,
            'instId': instId,
            'copyMode': copyMode,
            'copyTotalAmt': copyTotalAmt,
            'copyAmt': copyAmt,
            'copyRatio': copyRatio,
            'tpRatio': tpRatio,
            'slRatio': slRatio,
            'slTotalAmt': slTotalAmt,
            'subPosCloseType': subPosCloseType,
            'tag': BROKER_ID
        }
        return self._request(POST, COPYTRADING_AMEND_COPY_SETTINGS, params)
    
    # Stop copying
    def stop_copying(self, uniqueCode, subPosCloseType, instType=''):
        params = {
            'instType': instType,
            'uniqueCode': uniqueCode,
            'subPosCloseType': subPosCloseType,
        }
        return self._request(POST, COPYTRADING_STOP_COPY_TRADING, params)
    
    # Get copy settings
    def get_copy_settings(self, uniqueCode, instType=''):
        params = {
            'uniqueCode': uniqueCode,
            'instType': instType,
        }
        return self._request(GET, COPYTRADING_COPY_SETTINGS, params)
    
    # Get my lead traders
    def get_my_lead_traders(self, instType=''):
        params = { 'instType': instType }
        return self._request(GET, COPYTRADING_CURRENT_LEAD_TRADERS, params)
    
    # Get Copy trading configuration
    def get_public_config(self, instType=''):
        params = { 'instType': instType }
        return self._request(GET, COPYTRADING_PUBLIC_CONFIG, params)
    
    # Get Lead trader ranks
    def get_public_lead_traders(self, instType='', sortType='', state='', minLeadDays='', minAssets='', maxAssets='',
                                minAum='', maxAum='', dataVer='', page='', limit=''):
        params = {
            'instType': instType,
            'sortType': sortType,
            'state': state,
            'minLeadDays': minLeadDays,
            'minAssets': minAssets,
            'maxAssets': maxAssets,
            'minAum': minAum,
            'maxAum': maxAum,
            'dataVer': dataVer,
            'dataVer': dataVer,
            'page': page,
            'limit': limit,
        }
        return self._request(GET, COPYTRADING_PUBLIC_LEAD_TRADERS, params)
    
    # Get Lead trader weekly pnl
    def get_public_weekly_pnl(self, uniqueCode, instType=''):
        params = {
            'uniqueCode': uniqueCode,
            'instType': instType,
        }
        return self._request(GET, COPYTRADING_PUBLIC_WEEKLY_PNL, params)
    
    # Get Lead trader daily pnl
    def get_public_daily_pnl(self, uniqueCode, lastDays, instType=''):
        params = {
            'uniqueCode': uniqueCode,
            'instType': instType,
            'lastDays': lastDays,
        }
        return self._request(GET, COPYTRADING_PUBLIC_PNL, params)
    
    # Get Lead trader stats
    def get_public_stats(self, uniqueCode, lastDays, instType=''):
        params = {
            'uniqueCode': uniqueCode,
            'instType': instType,
            'lastDays': lastDays,
        }
        return self._request(GET, COPYTRADING_PUBLIC_STATS, params)
    
    # Get Lead trader currency preferences
    def get_public_preference_currency(self, uniqueCode, instType=''):
        params = {
            'uniqueCode': uniqueCode,
            'instType': instType,
        }
        return self._request(GET, COPYTRADING_PUBLIC_PREFERENCE_CURRENCY, params)
    
    # Get Lead trader current lead positions
    def get_public_current_subpositions(self, uniqueCode, instType='', after='', before='', limit=''):
        params = {
            'instType': instType,
            'uniqueCode': uniqueCode,
            'after': after,
            'before': before,
            'limit': limit,
        }
        return self._request(GET, COPYTRADING_PUBLIC_CURRENT_SUBPOSITIONS, params)
    
    # Get Lead trader lead position history
    def get_public_subpositions_history(self, uniqueCode, instType='', after='', before='', limit=''):
        params = {
            'instType': instType,
            'uniqueCode': uniqueCode,
            'after': after,
            'before': before,
            'limit': limit,
        }
        return self._request(GET, COPYTRADING_PUBLIC_SUBPOSITIONS_HISTORY, params)
    
    # Get Copy traders
    def get_public_copy_traders(self, uniqueCode, instType='', limit=''):
        params = {
            'instType': instType,
            'uniqueCode': uniqueCode,
            'limit': limit,
        }
        return self._request(GET, COPYTRADING_PUBLIC_COPY_TRADERS, params)
    