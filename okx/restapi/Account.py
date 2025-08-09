from .BaseClient import OkxBaseClient
from ..constants import *


class AccountClient(OkxBaseClient):

    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase,
                               use_server_time, simulation, domain, debug, proxy)

        # Get instruments
    def get_account_instruments(self, instType, instFamily='', instId=''):
        params = {
            'instType': instType,
            'instFamily': instFamily,
            'instId': instId
        }
        return self._request(GET, ACCOUNT_INSTRUMENTS, params)

    # Get Balance
    def get_account_balance(self, ccy=''):
        params = {}
        if ccy:
            params['ccy'] = ccy
        return self._request(GET, ACCOUNT_BALANCE, params)

    # Get Positions
    def get_positions(self, instType='', instId=''):
        params = {'instType': instType, 'instId': instId}
        return self._request(GET, ACCOUNT_POSITIONS, params)

    # Get positions history
    def get_positions_history(self, instType='', instId='', mgnMode='', type='', posId='', after='', before='', limit=''):
        params = {
            'instType': instType,
            'instId': instId,
            'mgnMode': mgnMode,
            'type': type,
            'posId': posId,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request(GET, ACCOUNT_POSITIONS_HISTORY, params)

    # Get account and position risk
    def get_position_risk(self, instType=''):
        params = {}
        if instType:
            params['instType'] = instType
        return self._request(GET, ACCOUNT_ACCOUNT_POSITION_RISK, params)

    # Get Bills Details (recent 7 days)
    def get_account_bills(self, instType='', ccy='', mgnMode='', ctType='', type='', subType='', after='', before='',
                          limit=''):
        params = {'instType': instType, 'ccy': ccy, 'mgnMode': mgnMode, 'ctType': ctType, 'type': type,
                  'subType': subType, 'after': after, 'before': before,
                  'limit': limit}
        return self._request(GET, ACCOUNT_BILLS, params)

    # Get Bills Details (recent 3 months)
    def get_account_bills_archive(self, instType='', ccy='', mgnMode='', ctType='', type='', subType='', after='',
                                  before='', limit=''):
        params = {'instType': instType, 'ccy': ccy, 'mgnMode': mgnMode, 'ctType': ctType, 'type': type,
                  'subType': subType, 'after': after, 'before': before,
                  'limit': limit}
        return self._request(GET, ACCOUNT_BILLS_ARCHIVE, params)
    
    # Apply bills details (since 2021)
    def apply_bills_history_archive(self, year, quarter):
        params = {'year': year, 'quarter': quarter}
        return self._request(POST, ACCOUNT_GEN_BILLS_HISTORY_ARCHIVE, params)

    # Get bills details (since 2021)
    def get_bills_history_archive(self, year, quarter):
        params = {'year': year, 'quarter': quarter}
        return self._request(GET, ACCOUNT_GET_BILLS_HISTORY_ARCHIVE, params)

    # Get Account Configuration
    def get_account_config(self):
        return self._request(GET, ACCOUNT_CONFIG)

    # Set position mode
    def set_position_mode(self, posMode):
        params = {'posMode': posMode}
        return self._request(POST, ACCOUNT_SET_POSITION_MODE, params)

    # Set leverage
    def set_leverage(self, lever, mgnMode, instId='', ccy='', posSide=''):
        params = {'lever': lever, 'mgnMode': mgnMode,
                  'instId': instId, 'ccy': ccy, 'posSide': posSide}
        return self._request(POST, ACCOUNT_SET_LEVERAGE, params)

    # Get maximum buy/sell amount or open amount
    def get_max_order_size(self, instId, tdMode, ccy='', px=''):
        params = {'instId': instId, 'tdMode': tdMode, 'ccy': ccy, 'px': px}
        return self._request(GET, ACCOUNT_MAX_SIZE, params)

    # Get maximum available tradable amount
    def get_max_avail_size(self, instId, tdMode, ccy='', reduceOnly='', unSpotOffset='', quickMgnType=''):
        params = {'instId': instId, 'tdMode': tdMode, 'ccy': ccy, 'reduceOnly': reduceOnly,
                  'unSpotOffset': unSpotOffset, 'quickMgnType': quickMgnType}
        return self._request(GET, ACCOUNT_MAX_AVAIL_SIZE, params)

    # Increase/decrease margin
    def adjust_margin(self, instId, posSide, type, amt, loanTrans=''):
        params = {'instId': instId, 'posSide': posSide,
                  'type': type, 'amt': amt, 'loanTrans': loanTrans}
        return self._request(POST, ACCOUNT_POSITION_MARGIN_BALANCE, params)

    # Get leverage
    def get_leverage(self, instId, mgnMode):
        params = {'instId': instId, 'mgnMode': mgnMode}
        return self._request(GET, ACCOUNT_LEVERAGE_INFO, params)

    # Get leverage estimated info
    def get_leverage_estimated_info(self, instType, mgnMode, lever, instId='', ccy='', posSide=''):
        params = {'instType': instType, 'mgnMode': mgnMode, 'lever': lever, 'instId': instId,
                  'ccy': ccy, 'posSide': posSide}
        return self._request(GET, ACCOUNT_ADJUST_LEVERAGE_INFO, params)

    # Get the maximum loan of instrument
    def get_max_loan(self, instId, mgnMode, mgnCcy):
        params = {'instId': instId, 'mgnMode': mgnMode, 'mgnCcy': mgnCcy}
        return self._request(GET, ACCOUNT_MAX_LOAN, params)

    # Get Fee Rates
    def get_fee_rates(self, instType, instId='', uly='', category='', instFamily=''):
        params = {'instType': instType, 'instId': instId, 'uly': uly,
                  'category': category, 'instFamily': instFamily}
        return self._request(GET, ACCOUNT_TRADE_FEE, params)

    # Get interest accrued data
    def get_interest_accrued(self, instId='', ccy='', mgnMode='', after='', before='', limit=''):
        params = {'instId': instId, 'ccy': ccy, 'mgnMode': mgnMode,
                  'after': after, 'before': before, 'limit': limit}
        return self._request(GET, ACCOUNT_INTEREST_ACCRUED, params)

    # Get interest rate
    def get_interest_rate(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, ACCOUNT_INTEREST_RATE, params)

    # Set greeks (PA/BS)
    def set_greeks(self, greeksType):
        params = {'greeksType': greeksType}
        return self._request(POST, ACCOUNT_SET_GREEKS, params)

    # Isolated margin trading settings
    def set_isolated_mode(self, isoMode, type):
        params = {'isoMode': isoMode, 'type': type}
        return self._request(POST, ACCOUNT_ISOLATED_MODE, params)

    # Get maximum withdrawals
    def get_max_withdrawal(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, ACCOUNT_MAX_WITHDRAWAL, params)

    # Get account risk state
    def get_account_position_risk(self):
        return self._request(GET, ACCOUNT_RISK_STATE)

    # Get borrow interest and limit
    def get_interest_limits(self, type='', ccy=''):
        params = {'type': type, 'ccy': ccy}
        return self._request(GET, ACCOUNT_INTEREST_LIMITS, params)

    # Manual borrow / repay
    def get_manual_borrow_repay(self, ccy, side, amt):
        params = {'ccy': ccy, 'side': side, 'amt': amt}
        return self._request(GET, ACCOUNT_SPOT_MANUAL_BORROW_REPAY, params)

    # Set auto repay
    def set_auto_repay(self, autoRepay):
        params = {'autoRepay': autoRepay}
        return self._request(POST, ACCOUNT_SET_AUTO_REPAY, params)

    # Get borrow/repay history
    def get_borrow_repay_history(self, ccy='', type='', after='', before='', limit=''):
        params = {'ccy': ccy, 'type': type, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, ACCOUNT_SPOT_BORROW_REPAY_HISTORY, params)

    # Position builder (new)
    def position_builder(self, inclRealPosAndEq=True, spotOffsetType='', simPos=[]):
        params = {'inclRealPosAndEq': inclRealPosAndEq,
                  'spotOffsetType': spotOffsetType, 'simPos': simPos}
        return self._request(POST, ACCOUNT_POSITION_BUILDER, params)

    # Position builder trend graph
    def position_builder_graph(self, inclRealPosAndEq='', simPos=[], simAsset=[], type='', mmrConfig={}):
        params = {'inclRealPosAndEq': inclRealPosAndEq, 'simPos': simPos, 'simAsset': simAsset, 'type': type, 'mmrConfig': mmrConfig}
        return self._request(POST, ACCOUNT_POSITION_BUILDER_GRAPH, params)

    # Set risk offset amount
    def set_risk_offset_amount(self, ccy, clSpotInUseAmt):
        params = {'ccy': ccy, 'clSpotInUseAmt': clSpotInUseAmt}
        return self._request(POST, ACCOUNT_SET_RISK_OFFSET_AMT, params)

    # Get  Greeks
    def get_greeks(self, ccy=''):
        params = {'ccy': ccy}
        return self._request(GET, ACCOUNT_GREEKS, params)

    # Get PM position limitation
    def get_account_position_tiers(self, instType='', uly='', instFamily=''):
        params = {
            'instType': instType,
            'uly': uly,
            'instFamily': instFamily
        }
        return self._request(GET, ACCOUNT_POSITION_TIERS, params)

    # Activate option
    def activate_option(self):
        return self._request(POST, ACCOUNT_ACTIVATE_OPTION)

    # Set auto loan
    def set_auto_loan(self, autoLoan=''):
        params = {'autoLoan': autoLoan}
        return self._request(POST, ACCOUNT_SET_AUTO_LOAN, params)

    # Preset account mode switch
    def preset_account_level_switch(self, acctLv, lever=''):
        params = {'acctLv': acctLv, 'lever': lever}
        return self._request(POST, ACCOUNT_LEVEL_SWITCH_PRESET, params)

    # Precheck account mode switch
    def precheck_account_level_switch(self, acctLv):
        params = {'acctLv': acctLv }
        return self._request(POST, ACCOUNT_SET_ACCOUNT_SWITCH_PRECHECK, params)

    # Set account level
    def set_account_level(self, acctLv):
        params = {'acctLv': acctLv}
        return self._request(POST, ACCOUNT_SET_ACCOUNT_LEVEL, params)

    # Set collateral assets
    def set_collateral_assets(self, type, collateralEnabled, ccyList):
        params = {'type': type, 'collateralEnabled': collateralEnabled, 'ccyList': ccyList}
        return self._request(POST, ACCOUNT_SET_COLLATERAL_ASSETS, params)

    # Get collateral assets
    def get_collateral_assets(self, ccy, collateralEnabled):
        params = {'ccy': ccy, 'collateralEnabled': collateralEnabled}
        return self._request(GET, ACCOUNT_GET_COLLATERAL_ASSETS, params)

    # Reset MMP Status
    def reset_mmp_status(self, instFamily, instType=''):
        params = {'instFamily': instFamily, 'instType': instType}
        return self._request(POST, ACCOUNT_MMP_RESET, params)

    # Set MMP
    def set_mmp_config(self, instFamily, timeInterval, frozenInterval, qtyLimit):
        params = {'instFamily': instFamily, 'timeInterval': timeInterval,
                  'frozenInterval': frozenInterval, 'qtyLimit': qtyLimit}
        return self._request(POST, ACCOUNT_SET_MMP_CONFIG, params)

    # GET MMP Config
    def get_mmp_config(self, instFamily=''):
        params = {'instFamily': instFamily}
        return self._request(GET, ACCOUNT_GET_MMP_CONFIG, params)

    # Get the invitee's detail
    def get_the_invitee_details(self, uid=''):
        params = {'uid': uid}
        return self._request(GET, AFFILIATE_INVITEE_DETAIL, params)
    
    # Move positions
    def move_positions(self, fromAcct, toAcct, legs, clientId):
        params = {
            'fromAcct': fromAcct,
            'toAcct': toAcct,
            'legs': legs,
            'clientId': clientId
        }
        return self._request(POST, ACCOUNT_MOVE_POSITIONS, params)

    # Get move positions history
    def get_move_positions_history(self, blockTdId='', clientId='', beginTs='', endTs='', limit='', state=''):
        params = {'blockTdId': blockTdId, 'clientId': clientId, 'beginTs': beginTs, 'endTs': endTs, 'limit': limit, 'state': state}
        return self._request(GET, ACCOUNT_MOVE_POSITIONS_HISTORY, params)

    # Set auto earn
    def set_auto_earn(self, ccy, action, apr=''):
        params = {'ccy': ccy, 'action': action, 'apr': apr}
        return self._request(POST, ACCOUNT_SET_AUTO_EARN, params)