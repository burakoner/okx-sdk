# OKX V5 API Python SDK

## Overview

**okx-sdk** is up-to-date, most-complete, well-organized, well-documented, easy-to-use OKX Exchange Rest and Websocket API SDK for Python.

### Links

Documentation: [https://www.okx.com/docs-v5/en](https://www.okx.com/docs-v5/en)  
Github: [https://github.com/burakoner/okx-sdk](https://github.com/burakoner/okx-sdk)  
PyPI: [https://pypi.org/project/okx-sdk](https://pypi.org/project/okx-sdk)

### Features

- Implementation of all Rest API endpoints.
- Private and Public Websocket implementation
- Testnet Support
- Websocket handling with reconnection and multiplexed connections

### Quick Start

#### Prerequisites

```python
python version>=3.9
```

#### Installation

Use your terminal to install okx-sdk

```python
pip install okx-sdk
```

#### Using Rest API

Import library as below

```python
from okx import *
# or
from okx import OkxRestClient
# or
from okx import OkxRestClient, OkxSocketClient
```

Build your API Client. You can use OKX API public endpoints without credentials. If you need to use private endpoints you need to provide credentials as below.

```python
api = OkxRestClient()
# or
api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
```

Call your request method

```python
api.public.get_tickers(instType="SPOT")
```

Here is a complete code example:

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
tickers = api.public.get_tickers(instType="SPOT")
print(tickers)

balances = api.account.get_account_balance()
print(balances)
```

There are several sections and hundreds of methods in Rest API Client. Please refer to all methods signatures list below for more information.

```python
api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.account.*       # Trading Account Client
api.funding.*       # Funding Account Client
api.subaccount.*    # Sub-Account Client
api.publicdata.*    # Public Data Client
api.marketdata.*    # Order Book Trading → Market Data Client
api.trade.*         # Order Book Trading → Trade Client
api.algotrade.*     # Order Book Trading → Algo Trading Client
api.gridtrade.*     # Order Book Trading → Grid Trading Client
api.signalbot.*     # Order Book Trading → Signal Bot Trading Client
api.recurring.*     # Order Book Trading → Recuring Buy Client
api.copytrade.*     # Order Book Trading → Copy Trading Client
api.blocktrade.*    # Block Trading Client
api.spreadtrade.*   # Spread Trading Client
api.rubik.*         # Trading Statistics Client
api.onchain_earn.*  # Financial Products → On-Chain Earn Client
api.eth_staking.*   # Financial Products → ETH Staking Client
api.sol_staking.*   # Financial Products → SOL Staking Client
api.simple_earn.*   # Financial Products → Simple Earn Flexible Client
api.flexible_loan.* # Financial Products → Flexible Loan Client
api.affiliate.*     # Affiliate Client
api.publicdata.*    # Status Endpoints are listed in PublicDataClient
api.publicdata.*    # Announcement Endpoints are listed in PublicDataClient
api.dmabroker.*     # DMA Broker Client
api.fdbroker.*      # Fully-Disclosed Broker Client
```

#### Using WebSocket API

Import library as below

```python
from okx import *
# or
from okx import OkxSocketClient
# or
from okx import OkxRestClient, OkxSocketClient
```

You can define WebScoket API Client as below

```python
ws = OkxSocketClient()
# or
ws = OkxSocketClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
```

There are 3 sections "public", "private" and "business" as described in [https://www.okx.com/docs-v5/en/#overview-production-trading-services](https://www.okx.com/docs-v5/en/#overview-production-trading-services). Every section has different streams. So you have to be sure that you are connecting right section.

```python
api = OkxSocketClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.public.*        # Public WebSocket Client
api.private.*       # Private WebSocket Client
api.business.*      # Business WebSocket Client
```

Prepare your callback method and subscribe

```python
ws = OkxSocketClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
await ws.public.start()
await ws.public.subscribe([{'channel': "tickers", 'instId': "BTC-USDT"}], callback=ws_handler)
```

Here is a fully working OKX WebSocket API Demo

```python
import asyncio
import json
from okx import *

def ws_handler(s):
    data = json.loads(s)

    if("event" in data):
        if(data["event"] == "subscribe"):
            print("Subscribed")
            return
        if(data["event"] == "unsubscribe"):
            print("Unsubscribed")
            return

    if("arg" in data and "channel" in data["arg"]):
        channel = data["arg"]["channel"]
        symbol = data["arg"]["instId"]
        if(channel == "tickers"):
            ticker = data["data"][0]
            print("[TICKER] Symbol:"+ ticker["instId"] +" Open:"+ ticker["open24h"] +" High:"+ ticker["high24h"] +" Low:"+ ticker["low24h"] +" Last:"+ ticker["last"] +" Volume:"+ ticker["vol24h"])
        elif(channel == "trades"):
            trade = data["data"][0]
            print("[TRADE] Symbol:"+ trade["instId"] +" Price:"+ trade["px"] + " Quantity:"+ trade["sz"])
        elif(channel.startswith("candle")):
            candle = data["data"][0]
            print("[CANDLE] Symbol:"+ symbol +" Open:"+ candle[1] +" High:"+ candle[2] +" Low:"+ candle[3] +" Close:"+ candle[4] +" Volume:"+ candle[5])
        else:
            print(f"[UNKNOWN] {text}")

async def tickers():
    ws = OkxSocketClient()
    await ws.public.start()
    await ws.public.subscribe([{'channel': "tickers", 'instId': "BTC-USDT"}], callback=ws_handler)

async def trades():
    ws = OkxSocketClient()
    await ws.public.start()
    await ws.public.subscribe([{'channel': "trades", 'instId': "BTC-USDT"}], callback=ws_handler)

async def multiple():
    ws = OkxSocketClient()
    await ws.public.start()
    await ws.public.subscribe([{'channel': "tickers", 'instId': "BTC-USDT"}, {'channel': "trades", 'instId': "BTC-USDT"}], callback=ws_handler)

async def candles():
    ws = OkxSocketClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
    await ws.business.start()
    await ws.business.subscribe([{'channel': "candle1H", 'instId': "BTC-USDT"}], callback=ws_handler)

asyncio.run(tickers())
# asyncio.run(trades())
# asyncio.run(candles())
# asyncio.run(multiple())
```

### Rest API Method Signatures

#### Trading Account Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.account.get_instruments(instType, instFamily='', instId=''):
api.account.get_balance(ccy=''):
api.account.get_positions(instType='', instId='', posId=''):
api.account.get_positions_history(instType='', instId='', mgnMode='', type='', posId='', after='', before='', limit=''):
api.account.get_position_risk(instType=''):
api.account.get_bills(instType='', instId='', ccy='', mgnMode='', ctType='', type='', subType='', after='', before='', begin='', end='', limit=''):
api.account.get_bills_archive(instType='', instId='', ccy='', mgnMode='', ctType='', type='', subType='', after='', before='', begin='', end='', limit=''):
api.account.apply_bills_history_archive(year, quarter):
api.account.get_bills_history_archive(year, quarter):
api.account.get_account_config(self):
api.account.set_position_mode(posMode):
api.account.set_leverage(lever, mgnMode, instId='', ccy='', posSide=''):
api.account.get_max_order_size(instId, tdMode, ccy='', px='', leverage='', tradeQuoteCcy=''):
api.account.get_max_avail_size(instId, tdMode, ccy='', reduceOnly='', px='', tradeQuoteCcy=''):
api.account.adjust_margin(instId, posSide, type, amt, ccy='')
api.account.get_leverage(mgnMode, instId='', ccy='')
api.account.get_leverage_estimated_info(instType, mgnMode, lever, instId='', ccy='', posSide='')
api.account.get_max_loan(mgnMode, instId, ccy='', mgnCcy='')
api.account.get_fee_rates(ruleType, instType, instId='', instFamily='')
api.account.get_interest_accrued(type='', ccy='', instId='', mgnMode='', after='', before='', limit='')
api.account.get_interest_rate(ccy='')
api.account.set_greeks(greeksType)
api.account.set_isolated_mode(isoMode, type)
api.account.get_max_withdrawal(ccy='')
api.account.get_account_risk_state()
api.account.get_interest_limits(type='', ccy='')
api.account.get_manual_borrow_repay(ccy, side, amt)
api.account.set_auto_repay(autoRepay)
api.account.get_borrow_repay_history(ccy='', type='', after='', before='', limit='')
api.account.position_builder(acctLv='', inclRealPosAndEq=True, lever='', simPos=[], simAsset=[], greeksType='', idxVol='')
api.account.position_builder_graph(inclRealPosAndEq='', simPos=[], simAsset=[], type='', mmrConfig={})
api.account.set_risk_offset_amount(ccy, clSpotInUseAmt)
api.account.get_greeks(ccy='')
api.account.get_position_tiers(instType='', instFamily='')
api.account.activate_option()
api.account.set_auto_loan(autoLoan=True):
api.account.preset_account_level_switch(acctLv, lever='')
api.account.precheck_account_level_switch(acctLv)
api.account.set_account_level(acctLv):
api.account.set_collateral_assets(type, collateralEnabled, ccyList)
api.account.get_collateral_assets(ccy, collateralEnabled)
api.account.reset_mmp_status(instFamily, instType='')
api.account.set_mmp_config(instFamily, timeInterval, frozenInterval, qtyLimit)
api.account.get_mmp_config(instFamily='')
api.account.move_positions(fromAcct, toAcct, legs, clientId)
api.account.get_move_positions_history(blockTdId='', clientId='', beginTs='', endTs='', limit='', state='')
api.account.set_auto_earn(ccy, action, apr='')
```

#### Funding Account Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.funding.get_currencies(ccy='')
api.funding.get_balances(ccy='')
api.funding.get_non_tradable_assets(ccy='')
api.funding.get_asset_valuation(ccy='')
api.funding.funds_transfer(ccy, amt, from_, to,  type='0', subAcct='', loanTrans=False, omitPosRisk=False, clientId='')
api.funding.get_transfer(transId, clientId='', type='')
api.funding.get_bills(ccy='', type='', clientId='', after='', before='', limit='', pagingType='1')
api.funding.get_bills_history(ccy='', type='', clientId='', after='', before='', limit='', pagingType='1')
api.funding.get_deposit_address(ccy)
api.funding.get_deposit_history(ccy='', depId='', fromWdId='', txId='', type='', state='', after='', before='', limit='')
api.funding.withdraw(ccy, amt, dest, toAddr, toAddrType='', chain='', areaCode='', rcvrInfo=None, clientId='')
api.funding.cancel_withdrawal(wdId='')
api.funding.get_withdrawal_history(ccy='', wdId='', clientId='', txId='', type='', state='', after='', before='', limit='')
api.funding.get_deposit_withdraw_status(wdId='', txId='', ccy='', to='', chain='')
api.funding.get_exchange_list()
api.funding.apply_monthly_statement(month)
api.funding.get_monthly_statement(month)
api.funding.get_convert_currencies()
api.funding.get_convert_currency_pair(fromCcy, toCcy)
api.funding.estimate_quote(baseCcy, quoteCcy, side, rfqSz, rfqSzCcy, clQReqId='')
api.funding.convert_trade(quoteId, baseCcy, quoteCcy, side, sz, szCcy, clTReqId='')
api.funding.get_convert_history(clTReqId='', after='', before='', limit='')
api.funding.get_fiat_deposit_payment_methods(ccy)
api.funding.get_fiat_withdrawal_payment_methods(ccy)
api.funding.fiat_withdraw(paymentAcctId, ccy, amt, paymentMethod, clientId)
api.funding.cancel_fiat_withdrawal(ordId)
api.funding.get_fiat_withdrawal_history(ccy='', paymentMethod='', state='', after='', before='', limit='')
api.funding.get_fiat_withdrawal_details(ordId)
api.funding.get_fiat_deposit_history(ccy='', paymentMethod='', state='', after='', before='', limit='')
api.funding.get_fiat_deposit_details(ordId)
api.funding.fiat_buy_sell_currencies()
api.funding.fiat_buy_sell_currency_pairs(fromCcy, toCcy)
api.funding.get_fiat_buy_sell_quote(side, fromCcy, toCcy, rfqAmt, rfqCcy)
api.funding.fiat_buy_sell_trade(quoteId, side, fromCcy, toCcy, rfqAmt, rfqCcy, paymentMethod, clOrdId)
api.funding.get_fiat_buy_sell_history(ordId='', clOrdId='', state='', begin='', end='', limit='')
```

#### Sub-Account Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.subaccount.get_subaccounts(enable='', subAcct='', after='', before='', limit='')
api.subaccount.create_subaccount(subAcct, type, label='', pwd='')
api.subaccount.create_apikey(subAcct, label, passphrase, perm='', ip='')
api.subaccount.get_apikey(subAcct, apiKey='')
api.subaccount.set_apikey(subAcct, apiKey, label='', perm='', ip='')
api.subaccount.delete_apikey(subAcct, apiKey)
api.subaccount.get_trading_balance(subAcct)
api.subaccount.get_funding_balance(subAcct='', ccy='')
api.subaccount.get_max_withdrawal(subAcct, ccy='')
api.subaccount.get_transfer_history(ccy='', type='', subAcct='', after='', before='', limit='')
api.subaccount.get_managed_transfer_history(ccy='', type='', subAcct='', subUid='', after='', before='', limit='')
api.subaccount.transfer(ccy, amt, from_, to, fromSubAccount, toSubAccount, loanTrans='false', omitPosRisk='false')
api.subaccount.set_permission_transfer_out(subAcct, canTransOut='')
api.subaccount.get_entrust_subaccounts(subAcct='')
```

#### Public Data Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient()
api.publicdata.get_time()
api.publicdata.get_status(state='')
api.publicdata.get_announcements(annType='', page='')
api.publicdata.get_announcement_types()
api.publicdata.get_instruments(instType, instId='', instFamily='')
api.publicdata.get_estimated_price(instId)
api.publicdata.get_delivery_exercise_history(instType, instFamily, after='', before='', limit='')
api.publicdata.get_estimated_settlement_info(instId)
api.publicdata.get_settlement_history(instFamily, after='', before='', limit='')
api.publicdata.get_funding_rate(instId)
api.publicdata.funding_rate_history(instId, after='', before='', limit='')
api.publicdata.get_open_interest(instType, instId='', instFamily='')
api.publicdata.get_price_limit(instId)
api.publicdata.get_option_summary(expTime='', instFamily='')
api.publicdata.discount_rate_interest_free_quota(ccy='')
api.publicdata.get_mark_price(instType, instId='', instFamily='')
api.publicdata.get_position_tiers(instType, tdMode, instFamily='', instId='', ccy='', tier='')
api.publicdata.get_interest_rate_loan_quota(payload)
api.publicdata.get_underlying(instType='')
api.publicdata.get_insurance_fund(instType='', type='', instFamily='', ccy='', before='', after='', limit='')
api.publicdata.unit_convert(type='', instId='', sz='', px='', unit='', opType='')
api.publicdata.get_option_tick_bands(instType, instFamily='')
api.publicdata.get_premium_history(instId, after='', before='', limit='')
api.publicdata.get_index_tickers(quoteCcy='', instId='')
api.publicdata.get_index_candlesticks(instId, bar='', after='', before='', limit='')
api.publicdata.get_index_candlesticks_history(instId, bar='', after='', before='', limit='')
api.publicdata.get_mark_price_candlesticks(instId, bar='', after='', before='', limit='')
api.publicdata.get_mark_price_candlesticks_history(instId, bar='', after='', before='', limit='')
api.publicdata.get_exchange_rate()
api.publicdata.get_index_components(index)
api.publicdata.get_economic_calendar(region='', importance='', before='', after='', limit='')
```

#### Market Data Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient()
api.marketdata.get_tickers(instType, instFamily='')
api.marketdata.get_ticker(instId)
api.marketdata.get_orderbook(instId, sz='')
api.marketdata.get_full_orderbook(instId, sz='')
api.marketdata.get_candlesticks(instId, bar='', after='', before='', limit='')
api.marketdata.get_history_candlesticks(instId,  bar='', after='', before='', limit='')
api.marketdata.get_trades(instId, limit='')
api.marketdata.get_trades_history(instId='', type='', after='', before='', limit='')
api.marketdata.get_option_trades_by_family(instFamily='')
api.marketdata.get_option_trades(instId='', instFamily='', optType='')
api.marketdata.get_volume()
api.marketdata.get_call_auction_details(instId)
```

#### Order Book Trading → Trade Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.trade.place_order(instId, tdMode, side, ordType, sz, ccy='', clOrdId='', posSide='', px='', pxUsd='', pxVol='', reduceOnly='', tgtCcy='', banAmend=False, tradeQuoteCcy='', stpMode='', attachAlgoOrds=None)
api.trade.place_multiple_orders(orders_data)
api.trade.cancel_order(instId, ordId='', clOrdId='')
api.trade.cancel_multiple_orders(orders_data)
api.trade.amend_order(instId, cxlOnFail='', ordId='', clOrdId='', reqId='', newSz='', newPx='', newPxUsd='', newPxVol='', attachAlgoOrds=None)
api.trade.amend_multiple_orders(orders_data)
api.trade.close_positions(instId, mgnMode, posSide='', ccy='', autoCxl='', clOrdId='')
api.trade.get_order(instId, ordId='', clOrdId='')
api.trade.get_order_list(instType='', instFamily='', instId='', ordType='', state='', after='', before='', limit='')
api.trade.get_orders_history(instType, instFamily='', instId='', ordType='', state='', category='', after='', before='', begin='', end='', limit='')
api.trade.get_orders_history_archive(instType, instFamily='', instId='', ordType='', state='', category='', after='', before='', begin='', end='', limit='')
api.trade.get_fills(instType='', instFamily='', instId='', ordId='', subType='', after='', before='',  begin='', end='', limit='')
api.trade.get_fills_history(instType, instFamily='', instId='', ordId='',  subType='', after='', before='', begin='', end='', limit='')
api.trade.get_easy_convert_currency_list(source='')
api.trade.easy_convert(fromCcy=[], toCcy='', source='')
api.trade.get_easy_convert_history(before='', after='', limit='')
api.trade.get_oneclick_repay_list(debtType='')
api.trade.oneclick_repay(debtCcy=[], repayCcy='')
api.trade.oneclick_repay_history(after='', before='', limit='')
api.trade.get_oneclick_repay_currency_list_v2()
api.trade.oneclick_repay_v2(debtCcy, repayCcyList)
api.trade.oneclick_repay_history_v2(after='', before='', limit='')
api.trade.cancel_all_orders(instType, instFamily, lockInterval='')
api.trade.cancel_all_after(timeOut)
api.trade.get_account_rate_limit()
api.trade.order_precheck(instId, tdMode, side, ordType, sz, px='', posSide='', reduceOnly='', tgtCcy='', attachAlgoOrds=[])
```

#### Order Book Trading → Algo Trading Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.algotrade.place_order(instId, tdMode, side, ordType, ccy='', posSide='', sz='', tgtCcy='', algoClOrdId='', closeFraction='', tradeQuoteCcy='')
api.algotrade.cancel_order(payload=[])
api.algotrade.amend_order(instId='', algoId='', algoClOrdId='', cxlOnFail='', reqId='', newSz='', newTpTriggerPx='', newTpOrdPx='', newSlTriggerPx='', newSlOrdPx='', newTpTriggerPxType='', newSlTriggerPxType='', newTriggerPx='', newOrdPx='', newTriggerPxType='', attachAlgoOrds=[])
api.algotrade.get_order(algoId='', algoClOrdId='')
api.algotrade.get_pending_orders(ordType='', algoId='', instType='', instId='', after='', before='', limit='')
api.algotrade.get_order_history(ordType, state='', algoId='', instType='', instId='', after='', before='', limit='')
```

#### Order Book Trading → Grid Trading Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.gridtrade.place_order(instId, algoOrdType, maxPx, minPx, gridNum, runType='', tpTriggerPx='', slTriggerPx='', algoClOrdId='', profitSharingRatio='', triggerParams=[], quoteSz='', baseSz='', sz='', direction='', lever='', basePos='', tpRatio='', slRatio='')
api.gridtrade.amend_order(algoId, instId, slTriggerPx='', tpTriggerPx='', tpRatio='', slRatio='', triggerParams=[])
api.gridtrade.stop_order(algoId, instId, algoOrdType, stopType)
api.gridtrade.close_position(algoId, mktClose, sz='', px='')
api.gridtrade.cancel_close_position_order(algoId, ordId)
api.gridtrade.instant_trigger_order(algoId)
api.gridtrade.get_pending_orders(algoOrdType='', algoId='', instId='', instType='', after='', before='', limit='')
api.gridtrade.get_orders_history(algoOrdType='', algoId='', instId='', instType='', after='', before='', limit='')
api.gridtrade.get_order_details(algoOrdType='', algoId='')
api.gridtrade.get_sub_orders(algoId='', algoOrdType='', type='', groupId='', after='', before='', limit='')
api.gridtrade.get_positions(algoOrdType, algoId)
api.gridtrade.withdraw_income(algoId)
api.gridtrade.compute_margin_balance(algoId, type, amt='')
api.gridtrade.adjust_margin_balance(algoId, type, amt='', percent='')
api.gridtrade.add_investment(algoId,  amt, allowReinvestProfit='')
api.gridtrade.get_ai_param(algoOrdType='', instId='', direction='', duration='')
api.gridtrade.compute_min_investment(instId, algoOrdType, maxPx, minPx, gridNum, runType, direction='', lever='', basePos='', investmentType='', triggerStrategy='', investmentData=[])
api.gridtrade.get_rsi_back_testing(instId, timeframe, thold, timePeriod, triggerCond='', duration='')
api.gridtrade.get_max_grid_quantity(instId, runType, algoOrdType, maxPx, minPx, lever='')
```

#### Order Book Trading → Signal Bot Trading Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.signalbot.create_signal(signalChanName, signalChanDesc='')
api.signalbot.get_signals(signalSourceType, signalChanId='', after='', before='', limit='')
api.signalbot.create(signalChanId, lever, investAmt, subOrdType, includeAll='', instIds='', ratio='', entrySettingParam={},exitSettingParam={})
api.signalbot.cancel(algoId)
api.signalbot.adjust_margin_balance(algoId, type, amt, allowReinvest=False)
api.signalbot.amend_tpsl(algoId, exitSettingParam={})
api.signalbot.set_instruments(algoId, instIds=[], includeAll=False)
api.signalbot.get_order(algoOrdType, algoId)
api.signalbot.get_active(algoOrdType, algoId, after='', before='', limit='')
api.signalbot.get_history(algoOrdType, algoId, after='', before='', limit='')
api.signalbot.get_positions(algoOrdType, algoId)
api.signalbot.get_position_history(algoId='', instId='', after='', before='', limit='')
api.signalbot.close_position(algoId, instId)
api.signalbot.place_sub_order(algoId, instId, side, ordType, sz, px='', reduceOnly=False)
api.signalbot.cancel_sub_order(algoId, instId, signalOrdId)
api.signalbot.get_sub_orders(algoId, algoOrdType, state='', signalOrdId='', after='', before='', begin='', end='', limit='',type='', clOrdId='')
api.signalbot.get_bot_events(algoId, after='', before='', limit='')
```

#### Order Book Trading → Recuring Buy Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.recurring.place_order(self, stgyName, recurringList, period, recurringDay='', recurringHour='',recurringTime='', timeZone='', amt='', investmentCcy='', tdMode='', algoClOrdId='')
api.recurring.amend_order(self, algoId='', stgyName='')
api.recurring.stop_order(self, algoId)
api.recurring.get_order_list(self, algoId='', after='', before='', limit='')
api.recurring.get_order_history(self, algoId='', after='', before='', limit='')
api.recurring.get_order_details(self, algoId)
api.recurring.get_sub_orders(self, algoId, ordId='', after='', before='', limit='')
```

#### Order Book Trading → Copy Trading Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.copytrade.get_current_subpositions(instType='', instId='', after='', before='', limit='')
api.copytrade.get_subpositions_history(instType='', instId='', after='', before='', limit='')
api.copytrade.place_order(subPosId, instType='', tpTriggerPx='', slTriggerPx='', tpOrdPx='', slOrdPx='', tpTriggerPxType='', slTriggerPxType='')
api.copytrade.close_subposition(subPosId, instType='', ordType='', px='')
api.copytrade.get_leading_instruments(instType='')
api.copytrade.set_leading_instruments(instId, instType='')
api.copytrade.get_profit_sharing_details(instType='', after='', before='', limit='')
api.copytrade.get_total_profit_sharing(instType='')
api.copytrade.get_unrealized_profit_sharing_details(instType='')
api.copytrade.get_total_unrealized_profit_sharing(instType='')
api.copytrade.set_profit_sharing_ratio(profitSharingRatio, instType='')
api.copytrade.get_account_configuration(self)
api.copytrade.first_copy_settings(uniqueCode, copyMgnMode, copyInstIdType,  instType='', instId='', copyMode='',copyTotalAmt='', copyAmt='', copyRatio='', tpRatio='', slRatio='', slTotalAmt='', subPosCloseType='')
api.copytrade.set_copy_settings(uniqueCode, copyMgnMode, copyInstIdType, instType='', instId='', copyMode='',copyTotalAmt='',copyAmt='', copyRatio='', tpRatio='', slRatio='', slTotalAmt='', subPosCloseType='')
api.copytrade.stop_copying(uniqueCode, subPosCloseType, instType='')
api.copytrade.get_copy_settings(uniqueCode, instType='')
api.copytrade.get_my_lead_traders(instType='')
api.copytrade.get_public_config(instType='')
api.copytrade.get_public_lead_traders(instType='', sortType='', state='', minLeadDays='', minAssets='', maxAssets='', minAum='', maxAum='', dataVer='', page='', limit='')
api.copytrade.get_public_weekly_pnl(uniqueCode, instType='')
api.copytrade.get_public_daily_pnl(uniqueCode, lastDays, instType='')
api.copytrade.get_public_stats(uniqueCode, lastDays, instType='')
api.copytrade.get_public_preference_currency(uniqueCode, instType='')
api.copytrade.get_public_current_subpositions(uniqueCode, instType='', after='', before='', limit='')
api.copytrade.get_public_subpositions_history(uniqueCode, instType='', after='', before='', limit='')
api.copytrade.get_public_copy_traders(uniqueCode, instType='', limit='')
```

#### Block Trading Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.blocktrade.get_counterparties(self)
api.blocktrade.create_rfq(counterparties=[], anonymous=False, clRfqId='', allowPartialExecution=False, legs=[])
api.blocktrade.cancel_rfq(rfqId='', clRfqId='')
api.blocktrade.cancel_batch_rfqs(rfqIds=[], clRfqIds=[])
api.blocktrade.cancel_all_rfqs(self)
api.blocktrade.execute_quote(rfqId='', quoteId='', legs=[])
api.blocktrade.get_quote_products(self)
api.blocktrade.set_quote_products(payload=[])
api.blocktrade.reset_mmp(self)
api.blocktrade.set_mmp_config(timeInterval, frozenInterval, countLimit)
api.blocktrade.get_mmp_config(timeInterval='', frozenInterval='', countLimit='', mmpFrozen='', mmpFrozenUntil='')
api.blocktrade.create_quote(rfqId='', clQuoteId='',anonymous=False,  quoteSide='', expiresIn='', legs=[])
api.blocktrade.cancel_quote(quoteId='', clQuoteId='', rfqId='')
api.blocktrade.cancel_batch_quotes(quoteIds=[], clQuoteIds=[])
api.blocktrade.cancel_all_quotes(self)
api.blocktrade.cancel_all_after(timeOut)
api.blocktrade.get_rfqs(rfqId='', clRfqId='', state='', beginId='', endId='', limit='')
api.blocktrade.get_quotes(rfqId='', clRfqId='', quoteId='', clQuoteId='', state='', beginId='', endId='', limit='')
api.blocktrade.get_trades(rfqId='', clRfqId='', quoteId='', blockTdId='', clQuoteId='', beginId='', endId='', beginTs='', endTs='', limit='', isSuccessful=False)
api.blocktrade.get_block_tickers(instType, instFamily='')
api.blocktrade.get_block_ticker(instId)
api.blocktrade.get_public_trades(beginId='', endId='', limit='')
api.blocktrade.get_public_block_trades(instId)
```

#### Spread Trading Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.spreadtrade.place_order(sprdId, side, ordType, sz, px, clOrdId='')
api.spreadtrade.cancel_order(ordId='', clOrdId='')
api.spreadtrade.cancel_all_orders(sprdId='')
api.spreadtrade.amend_order(ordId='', clOrdId='', reqId='', newSz='', newPx='')
api.spreadtrade.get_order_details(ordId='', clOrdId='')
api.spreadtrade.get_active_orders(sprdId='', ordType='', state='', beginId='', endId='', limit='')
api.spreadtrade.get_orders_history(sprdId='', ordType='', state='', beginId='', endId='', begin='', end='', limit='')
api.spreadtrade.get_orders_archive(sprdId='', ordType='', state='', instType='', instFamily='', beginId='', endId='', begin='', end='', limit='')
api.spreadtrade.get_trades(sprdId='', tradeId='', ordId='', beginId='', endId='', begin='', end='', limit='')
api.spreadtrade.get_spreads(baseCcy='', instId='', sprdId='', state='')
api.spreadtrade.get_order_book(sprdId, sz='')
api.spreadtrade.get_ticker(sprdId)
api.spreadtrade.get_public_trades(sprdId='')
api.spreadtrade.get_candles(sprdId, bar='', after='', before='', limit='')
api.spreadtrade.get_candles_history(sprdId, bar='', after='', before='', limit='')
api.spreadtrade.cancel_all_after(timeOut)
```

#### Trading Statistics Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.rubik.get_support_coin()
api.rubik.get_open_interest_history(instId, period='', begin='', end='', limit='')
api.rubik.get_taker_volume(ccy, instType, period='', begin='', end='')
api.rubik.get_contract_taker_volume(instId, period='', unit='', begin='', end='', limit='')
api.rubik.get_margin_loan_ratio(ccy, period='', begin='', end='')
api.rubik.get_top_traders_contracts_long_short_ratio_by_account(instId, period='', begin='', end='', limit='')
api.rubik.get_top_traders_contracts_long_short_ratio_by_position(instId, period='', begin='', end='', limit='')
api.rubik.get_contracts_long_short_ratio(instId, period='', begin='', end='', limit='')
api.rubik.get_long_short_ratio(ccy, period='', begin='', end='')
api.rubik.get_contracts_interest_volume(ccy, period='', begin='', end='')
api.rubik.get_options_interest_volume(ccy, period='')
api.rubik.get_put_call_ratio(ccy, period='')
api.rubik.get_interest_volume_expiry(ccy, period='')
api.rubik.get_interest_volume_strike(ccy, expTime, period='')
api.rubik.get_taker_block_volume(ccy, period='')
```

#### Financial Products → On-Chain Earn Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.onchain_earn.get_offers(productId='', protocolType='', ccy='')
api.onchain_earn.purchase(productId, investData, term='')
api.onchain_earn.redeem(ordId, protocolType, allowEarlyRedeem=False)
api.onchain_earn.cancel(ordId, protocolType)
api.onchain_earn.get_active_orders(productId='', protocolType='', ccy='', state='')
api.onchain_earn.get_orders_history(productId='', protocolType='', ccy='', after='', before='', limit='')
```

#### Financial Products → ETH Staking Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.eth_staking.product_info(self)
api.eth_staking.purchase(amt)
api.eth_staking.redeem(amt)
api.eth_staking.get_balance(self)
api.eth_staking.get_purchase_redeem_history(type='', status='', after='', before='', limit='')
api.eth_staking.apy_history(days)
```

#### Financial Products → SOL Staking Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.sol_staking.product_info(self)
api.sol_staking.purchase(amt)
api.sol_staking.redeem(amt)
api.sol_staking.get_balance(self)
api.sol_staking.get_purchase_redeem_history(type='', status='', after='', before='', limit='')
api.sol_staking.apy_history(days)
```

#### Financial Products → Simple Earn Flexible Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.simple_earn.get_balance(ccy='')
api.simple_earn.purchase_redemption(ccy, amt, side, rate='')
api.simple_earn.set_lending_rate(ccy, rate)
api.simple_earn.get_lending_history(ccy='', after='', before='', limit='')
api.simple_earn.get_public_borrow_info(ccy='')
api.simple_earn.get_public_borrow_history(ccy='', after='', before='', limit='')
```

#### Financial Products → Flexible Loan Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.flexible_loan.get_currencies(self)
api.flexible_loan.get_collateral_assets(ccy='')
api.flexible_loan.get_max_loan(borrowCcy, supCollateral=[])
api.flexible_loan.get_max_collateral_redeem_amount(ccy)
api.flexible_loan.get_adjust_collateral(type, collateralCcy, collateralAmt)
api.flexible_loan.get_loan_info(self)
api.flexible_loan.get_loan_history(type='', after='', before='', limit='')
api.flexible_loan.get_interest_accrued(ccy='', after='', before='', limit='')
```

#### Affiliate Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.affiliate.get_invitee_details(uid):
```

#### DMA Broker Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.dmabroker.get_subaccount_list(subAcct='', uid='', page='', limit='')
api.dmabroker.get_subaccount_fee_rates(subAcct='', uid='', page='', limit='')
api.dmabroker.create_subaccount_apikey(subAcct, label, passphrase, ip='', perm='')
api.dmabroker.get_subaccount_apikey(subAcct, apiKey='')
api.dmabroker.get_trading_data_link(type, begin='', end='')
api.dmabroker.generate_trades_download_link(begin='', end='')
```

#### Fully-Disclosed Broker Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.fdbroker.get_rebate_details_download_link(type='', begin='', end='')
api.fdbroker.generate_rebate_details_download_link(begin='', end='')
api.fdbroker.get_users_broker_rebate_information(apiKey, brokerType)
```
