from .BaseClient import OkxBaseClient
from ..constants import *


class AccountClient(OkxBaseClient):

    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

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
    def get_positions_history(self, instType='', instId='', mgnMode='', type='', posId='', after='', before='',
                              limit=''):
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

    # Get Account Configuration
    def get_account_config(self):
        return self._request(GET, ACCOUNT_CONFIG)

    # Set position mode
    def set_position_mode(self, posMode):
        params = {'posMode': posMode}
        return self._request(POST, ACCOUNT_SET_POSITION_MODE, params)

    # Set leverage
    def set_leverage(self, lever, mgnMode, instId='', ccy='', posSide=''):
        params = {'lever': lever, 'mgnMode': mgnMode, 'instId': instId, 'ccy': ccy, 'posSide': posSide}
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
        params = {'instId': instId, 'posSide': posSide, 'type': type, 'amt': amt, 'loanTrans': loanTrans}
        return self._request(POST, ACCOUNT_POSITION_MARGIN_BALANCE, params)

    # Get leverage
    def get_leverage(self, instId, mgnMode):
        params = {'instId': instId, 'mgnMode': mgnMode}
        return self._request(GET, ACCOUNT_LEVERAGE_INFO, params)

    # TODO: Get leverage estimated info

    # Get the maximum loan of instrument
    def get_max_loan(self, instId, mgnMode, mgnCcy):
        params = {'instId': instId, 'mgnMode': mgnMode, 'mgnCcy': mgnCcy}
        return self._request(GET, ACCOUNT_MAX_LOAN, params)

    # Get Fee Rates
    def get_fee_rates(self, instType, instId='', uly='', category='', instFamily=''):
        params = {'instType': instType, 'instId': instId, 'uly': uly, 'category': category, 'instFamily': instFamily}
        return self._request(GET, ACCOUNT_TRADE_FEE, params)

    # Get interest accrued data
    def get_interest_accrued(self, instId='', ccy='', mgnMode='', after='', before='', limit=''):
        params = {'instId': instId, 'ccy': ccy, 'mgnMode': mgnMode, 'after': after, 'before': before, 'limit': limit}
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

    # TODO: Manual borrow and repay in Quick Margin Mode
    # TODO: Get borrow and repay history in Quick Margin Mode

    # VIP loans borrow and repay
    def borrow_repay(self, ccy='', side='', amt='', ordId=''):
        params = {'ccy': ccy, 'side': side, 'amt': amt, 'ordId': ordId}
        return self._request(POST, ACCOUNT_BORROW_REPAY, params)

    # Get borrow and repay history for VIP loans
    def get_borrow_repay_history(self, ccy='', after='', before='', limit=''):
        params = {'ccy': ccy, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, ACCOUNT_BORROW_REPAY_HISTORY, params)

    # Get VIP interest accrued data
    def get_VIP_interest_accrued_data(self, ccy='', ordId='', after='', before='', limit=''):
        params = {'ccy': ccy, 'ordId': ordId, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, ACCOUNT_VIP_INTEREST_ACCRUED, params)

    # Get VIP interest deducted data
    def get_vip_interest_deducted_data(self, ccy='', ordId='', after='', before='', limit=''):
        params = {'ccy': ccy, 'ordId': ordId, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, ACCOUNT_VIP_INTEREST_DEDUCTED, params)

    # Get VIP loan order list
    def get_vip_loan_order_list(self, ordId='', state='', ccy='', after='', before='', limit=''):
        params = {'ordId': ordId, 'state': state, 'ccy': ccy, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, ACCOUNT_VIP_LOAN_ORDER_LIST, params)

    # Get VIP loan order detail
    def get_vip_loan_order_detail(self, ccy='', ordId='', after='', before='', limit=''):
        params = {'ccy': ccy, 'ordId': ordId, 'after': after, 'before': before, 'limit': limit}
        return self._request(GET, ACCOUNT_VIP_LOAN_ORDER_DETAIL, params)

    # Get borrow interest and limit
    def get_interest_limits(self, type='', ccy=''):
        params = {'type': type, 'ccy': ccy}
        return self._request(GET, ACCOUNT_INTEREST_LIMITS, params)

    # Position builder
    def get_simulated_margin(self, instType='', inclRealPos=True, spotOffsetType='', simPos=[]):
        params = {'instType': instType, 'inclRealPos': inclRealPos, 'spotOffsetType': spotOffsetType, 'simPos': simPos}
        return self._request(POST, ACCOUNT_SIMULATED_MARGIN, params)

    # TODO: Position builder (new)

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

    # Set risk offset type
    def set_risk_offset_typel(self, type=''):
        params = {'type': type}
        return self._request(POST, ACCOUNT_SET_RISK_OFFSET_TYPE, params)

    # Activate option
    def activate_option(self):
        return self._request(POST, ACCOUNT_ACTIVATE_OPTION)

    # Set auto loan
    def set_auto_loan(self, autoLoan=''):
        params = {'autoLoan': autoLoan}
        return self._request(POST, ACCOUNT_SET_AUTO_LOAN, params)

    # TODO: Set account mode
    # TODO: Reset MMP Status
    # TODO: Set MMP
    # TODO: GET MMP Config

    # Get the invitee's detail
    def get_the_invitee_details(self, uid=''):
        params = {'uid': uid}
        return self._request(GET, AFFILIATE_INVITEE_DETAIL, params)

    # Get the user's affiliate rebate information
    def get_the_user_affiliate_rebate_information(self, apiKey=''):
        params = {'apiKey': apiKey}
        return self._request(GET, USERS_PARTNER_IF_REBATE, params)
