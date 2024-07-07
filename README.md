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

There are 17 sections and hundreds of methods in Rest API Client. Please refer to all methods signatures list below for more information.

```python
api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.account.*       # Trading Account Client
api.funding.*       # Funding Account Client
api.subaccount.*    # Sub-Account Client
api.public.*        # Single Client for both "Public Data" and "Market Data"
api.market.*        # Alias of "public". You can use both sections "api.public.*" and "api.market.*"
api.trade.*         # Order Book Trading → Trade Client
api.algotrade.*     # Order Book Trading → Algo Trading Client
api.copytrade.*     # Order Book Trading → Copy Trading Client
api.gridtrade.*     # Order Book Trading → Grid Trading Client
api.recurringbuy.*  # Order Book Trading → Recuring Buy Client
api.signaltrade.*   # Order Book Trading → Signal Bot Trading Client
api.blocktrade.*    # Block Trading Client
api.spreadtrade.*   # Spread Trading Client
api.finance.*       # Financial Products Client
api.rubik.*         # Trading Statistics Client
api.ndbroker.*      # Non-Disclosed Broker Client
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

### All Rest API Method Signatures

#### Trading Account Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.account.get_account_balance(ccy='')
api.account.get_positions(instType='', instId='')
api.account.get_positions_history(instType='', instId='', mgnMode='', type='', posId='', after='', before='', limit='')
api.account.get_position_risk(instType='')
api.account.get_account_bills(instType='', ccy='', mgnMode='', ctType='', type='', subType='', after='', before='', limit='')
api.account.get_account_bills_archive(instType='', ccy='', mgnMode='', ctType='', type='', subType='', after='', before='', limit='')
api.account.get_account_config()
api.account.set_position_mode(posMode)
api.account.set_leverage(lever, mgnMode, instId='', ccy='', posSide='')
api.account.get_max_order_size(instId, tdMode, ccy='', px='')
api.account.get_max_avail_size(instId, tdMode, ccy='', reduceOnly='', unSpotOffset='', quickMgnType='')
api.account.adjust_margin(instId, posSide, type, amt, loanTrans='')
api.account.get_leverage(instId, mgnMode)
api.account.get_leverage_estimated_info(instType, mgnMode, lever, instId='', ccy='', posSide='')
api.account.get_max_loan(instId, mgnMode, mgnCcy)
api.account.get_fee_rates(instType, instId='', uly='', category='', instFamily='')
api.account.get_interest_accrued(instId='', ccy='', mgnMode='', after='', before='', limit='')
api.account.get_interest_rate(ccy='')
api.account.set_greeks(greeksType)
api.account.set_isolated_mode(isoMode, type)
api.account.get_max_withdrawal(ccy='')
api.account.get_account_position_risk()
api.account.quick_margin_borrow_repay(instId, ccy, side, amt)
api.account.get_quick_margin_borrow_repay_history(instId='', ccy='', side='', after='', before='', begin='', end='', limit='')
api.account.borrow_repay(ccy='', side='', amt='', ordId='')
api.account.get_borrow_repay_history(ccy='', after='', before='', limit='')
api.account.get_VIP_interest_accrued_data(ccy='', ordId='', after='', before='', limit='')
api.account.get_vip_interest_deducted_data(ccy='', ordId='', after='', before='', limit='')
api.account.get_vip_loan_order_list(ordId='', state='', ccy='', after='', before='', limit='')
api.account.get_vip_loan_order_detail(ccy='', ordId='', after='', before='', limit='')
api.account.get_interest_limits(type='', ccy='')
api.account.simulated_margin(instType='', inclRealPos=True, spotOffsetType='', simPos=[])
api.account.position_builder(inclRealPosAndEq=True, spotOffsetType='', simPos=[])
api.account.get_greeks(ccy='')
api.account.get_account_position_tiers(instType='', uly='', instFamily='')
api.account.set_risk_offset_typel(type='')
api.account.activate_option()
api.account.set_auto_loan(autoLoan='')
api.account.set_account_mode(acctLv)
api.account.reset_mmp_status(instFamily, instType='')
api.account.set_mmp_config(instFamily, timeInterval, frozenInterval, qtyLimit)
api.account.get_mmp_config(instFamily='')
api.account.get_the_invitee_details(uid='')
api.account.get_the_user_affiliate_rebate_information(apiKey='')
```

#### Funding Account Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.funding.get_currencies(ccy='')
api.funding.get_balances(ccy='')
api.funding.get_non_tradable_assets(ccy='')
api.funding.get_asset_valuation(ccy='')
api.funding.funds_transfer(ccy, amt, from_, to, type='0', subAcct='', instId='', toInstId='', loanTrans='')
api.funding.transfer_state(transId, type='')
api.funding.get_bills(ccy='', type='', after='', before='', limit='')
api.funding.get_deposit_lightning(ccy, amt, to="")
api.funding.get_deposit_address(ccy)
api.funding.get_deposit_history(ccy='', state='', after='', before='', limit='', txId='', depId='', fromWdId='')
api.funding.withdrawal(ccy, amt, dest, toAddr, fee, chain='', areaCode='', clientId='')
api.funding.withdrawal_lightning(ccy, invoice, memo='')
api.funding.cancel_withdrawal(wdId='')
api.funding.get_withdrawal_history(ccy='', wdId='', state='', after='', before='', limit='', txId='')
api.funding.get_deposit_withdraw_status(wdId='', txId='', ccy='', to='', chain='')
api.funding.convert_dust_assets(ccy=[])
api.funding.get_exchange_list()
api.funding.apply_monthly_statement(month)
api.funding.get_monthly_statement(month)
api.funding.get_convert_currencies()
api.funding.get_convert_currency_pair(fromCcy='', toCcy='')
api.funding.estimate_quote(baseCcy='', quoteCcy='', side='', rfqSz='', rfqSzCcy='', clQReqId='')
api.funding.convert_trade(quoteId='', baseCcy='', quoteCcy='', side='', sz='', szCcy='', clTReqId='')
api.funding.get_convert_history(after='', before='', limit='', tag='')
```

#### Sub-Account Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.subaccount.get_subaccount_list(enable='', subAcct='', after='', before='', limit='')
api.subaccount.reset_subaccount_apikey(subAcct, apiKey, label='', perm='', ip='')
api.subaccount.get_trading_balance(subAcct)
api.subaccount.get_funding_balance(subAcct='', ccy='')
api.subaccount.get_max_withdrawal(subAcct, ccy='')
api.subaccount.get_transfer_history(ccy='', type='', subAcct='', after='', before='', limit='')
api.subaccount.get_managed_transfer_history(ccy='', type='', subAcct='', subUid='', after='', before='', limit='')
api.subaccount.transfer_between_sub_accounts(ccy, amt, froms, to, fromSubAccount, toSubAccount, loanTrans='false', omitPosRisk='false')
api.subaccount.set_permission_transfer_out(subAcct='', canTransOut='')
api.subaccount.get_entrust_subaccount_list(subAcct='')
api.subaccount.set_sub_accounts_VIP_loan(enable='', alloc=[])
api.subaccount.get_sub_account_borrow_interest_and_limit(subAcct='', ccy='')
```

#### Public Data and Market Data Client Methods

OKX-SDK merges Public and Market Data sections into one client only. You can use both "**api.public**" or "**api.market**" section for your requests.

```python
from okx import OkxRestClient

api = OkxRestClient()
api.public.get_system_time()
api.public.status(state='')
api.public.get_instruments(instType, uly='', instId='', instFamily='')
api.public.get_delivery_exercise_history(instType, uly='', after='', before='', limit='', instFamily='')
api.public.get_open_interest(instType, uly='', instId='', instFamily='')
api.public.get_funding_rate(instId)
api.public.funding_rate_history(instId, after='', before='', limit='')
api.public.get_price_limit(instId)
api.public.get_opt_summary(uly='', expTime='', instFamily='')
api.public.get_estimated_price(instId)
api.public.discount_interest_free_quota(ccy='')
api.public.get_mark_price(instType, uly='', instId='', instFamily='')
api.public.get_position_tiers(instType, tdMode, uly='', instFamily='', instId='', ccy='', tier='')
api.public.get_interest_rate_loan_quota()
api.public.get_vip_interest_rate_loan_quota()
api.public.get_underlying(instType='')
api.public.get_insurance_fund(instType='', type='', uly='', ccy='', before='', after='', limit='', instFamily='')
api.public.unit_convert(type='', instId='', sz='', px='', unit='')
api.public.get_option_tickBands(instType='', instFamily='')
api.public.get_index_tickers(quoteCcy='', instId='')
api.public.get_index_candlesticks(instId, after='', before='', bar='', limit='')
api.public.get_index_candlesticks_history(instId, after='', before='', bar='', limit='')
api.public.get_mark_price_candlesticks(instId, after='', before='', bar='', limit='')
api.public.get_mark_price_candlesticks_history(instId, after='', before='', bar='', limit='')
api.public.get_oracle()
api.public.get_exchange_rate()
api.public.get_index_components(index='')
api.public.get_block_tickers(instType='', uly='', instFamily='')
api.public.get_block_ticker(instId='')
api.public.get_block_trades(instId='')
api.public.get_economic_calendar(region='', importance='', before='', after='', limit='')
api.public.get_tickers(instType, uly='', instFamily='')
api.public.get_ticker(instId)
api.public.get_orderbook(instId, sz='')
api.public.get_full_orderbook(instId, sz='')
api.public.get_candlesticks(instId, after='', before='', bar='', limit='')
api.public.get_history_candlesticks(instId, after='', before='', bar='', limit='')
api.public.get_trades(instId, limit='')
api.public.get_history_trades(instId='', type='', after='', before='', limit='')
api.public.get_option_trades_by_family(instFamily='')
api.public.get_option_trades(instId='', instFamily='', optType='')
api.public.get_volume()
```

```python
from okx import OkxRestClient

api = OkxRestClient()
api.market.get_system_time()
api.market.status(state='')
api.market.get_instruments(instType, uly='', instId='', instFamily='')
api.market.get_delivery_exercise_history(instType, uly='', after='', before='', limit='', instFamily='')
api.market.get_open_interest(instType, uly='', instId='', instFamily='')
api.market.get_funding_rate(instId)
api.market.funding_rate_history(instId, after='', before='', limit='')
api.market.get_price_limit(instId)
api.market.get_opt_summary(uly='', expTime='', instFamily='')
api.market.get_estimated_price(instId)
api.market.discount_interest_free_quota(ccy='')
api.market.get_mark_price(instType, uly='', instId='', instFamily='')
api.market.get_position_tiers(instType, tdMode, uly='', instFamily='', instId='', ccy='', tier='')
api.market.get_interest_rate_loan_quota()
api.market.get_vip_interest_rate_loan_quota()
api.market.get_underlying(instType='')
api.market.get_insurance_fund(instType='', type='', uly='', ccy='', before='', after='', limit='', instFamily='')
api.market.unit_convert(type='', instId='', sz='', px='', unit='')
api.market.get_option_tickBands(instType='', instFamily='')
api.market.get_index_tickers(quoteCcy='', instId='')
api.market.get_index_candlesticks(instId, after='', before='', bar='', limit='')
api.market.get_index_candlesticks_history(instId, after='', before='', bar='', limit='')
api.market.get_mark_price_candlesticks(instId, after='', before='', bar='', limit='')
api.market.get_mark_price_candlesticks_history(instId, after='', before='', bar='', limit='')
api.market.get_oracle()
api.market.get_exchange_rate()
api.market.get_index_components(index='')
api.market.get_block_tickers(instType='', uly='', instFamily='')
api.market.get_block_ticker(instId='')
api.market.get_block_trades(instId='')
api.market.get_economic_calendar(region='', importance='', before='', after='', limit='')
api.market.get_tickers(instType, uly='', instFamily='')
api.market.get_ticker(instId)
api.market.get_orderbook(instId, sz='')
api.market.get_full_orderbook(instId, sz='')
api.market.get_candlesticks(instId, after='', before='', bar='', limit='')
api.market.get_history_candlesticks(instId, after='', before='', bar='', limit='')
api.market.get_trades(instId, limit='')
api.market.get_history_trades(instId='', type='', after='', before='', limit='')
api.market.get_option_trades_by_family(instFamily='')
api.market.get_option_trades(instId='', instFamily='', optType='')
api.market.get_volume()
```

#### Order Book Trading → Trade Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.trade.place_order(instId, tdMode, side, ordType, sz, 
    ccy='', clOrdId='', posSide='', px='', reduceOnly='', 
    tgtCcy='', tpTriggerPx='', tpOrdPx='', slTriggerPx='', slOrdPx='', tpTriggerPxType='', slTriggerPxType='', quickMgnType='', stpId='', stpMode='',
    attachAlgoOrds=None)
api.trade.place_multiple_orders(orders_data)
api.trade.cancel_order(instId, ordId='', clOrdId='')
api.trade.cancel_multiple_orders(orders_data)
api.trade.amend_order(instId, cxlOnFail='', ordId='', clOrdId='', reqId='', 
    newSz='', newPx='', newTpTriggerPx='', newTpOrdPx='', newSlTriggerPx='', 
    newSlOrdPx='', newTpTriggerPxType='', newSlTriggerPxType='', attachAlgoOrds='')
api.trade.amend_multiple_orders(orders_data)
api.trade.close_positions(instId, mgnMode, posSide='', ccy='', autoCxl='', clOrdId='')
api.trade.get_order(instId, ordId='', clOrdId='')
api.trade.get_order_list(instType='', uly='', instId='', ordType='', state='', after='', before='', limit='', instFamily='')
api.trade.get_orders_history(instType, uly='', instId='', ordType='', state='', after='', before='', begin='', end='', limit='', instFamily='')
api.trade.get_orders_history_archive(instType, uly='', instId='', ordType='', state='', after='', before='', begin='', end='', limit='', instFamily='')
api.trade.get_fills(instType='', uly='', instId='', ordId='', after='', before='', limit='', instFamily='')
api.trade.get_fills_history(instType, uly='', instId='', ordId='', after='', before='', limit='', instFamily='')
api.trade.apply_fills_archive(year, quarter)
api.trade.get_fills_archive(year, quarter)
api.trade.get_easy_convert_currency_list()
api.trade.easy_convert(fromCcy=[], toCcy='')
api.trade.get_easy_convert_history(before='', after='', limit='')
api.trade.get_oneclick_repay_list(debtType='')
api.trade.oneclick_repay(debtCcy=[], repayCcy='')
api.trade.oneclick_repay_history(after='', before='', limit='')
api.trade.cancel_all_orders(instType, instFamily)
api.trade.cancel_all_after(timeOut)
api.trade.get_account_rate_limit()
```

#### Order Book Trading → Algo Trading Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.algotrade.place_algo_order(instId='', tdMode='', side='', ordType='', sz='', 
    ccy='', posSide='', reduceOnly='', tpTriggerPx='', tpOrdPx='', 
    slTriggerPx='', slOrdPx='', triggerPx='', orderPx='', tgtCcy='', 
    pxVar='', pxSpread='', szLimit='', pxLimit='', timeInterval='', 
    tpTriggerPxType='', slTriggerPxType='', callbackRatio='', callbackSpread='', activePx='', triggerPxType='', closeFraction='', quickMgnType='', algoClOrdId='')
api.algotrade.cancel_algo_order(params)
api.algotrade.amend_algo_order(instId='', algoId='', algoClOrdId='', cxlOnFail='', reqId='',
    newSz='', newTpTriggerPx='', newTpOrdPx='', newSlTriggerPx='', newSlOrdPx='', newTpTriggerPxType='', newSlTriggerPxType='')
api.algotrade.cancel_advance_algos(params)
api.algotrade.get_algo_order_details(algoId='', algoClOrdId='')
api.algotrade.order_algos_list(ordType='', algoId='', instType='', instId='', after='', before='', limit='', algoClOrdId='')
api.algotrade.order_algos_history(ordType, state='', algoId='', instType='', instId='', after='', before='', limit='')
```

#### Order Book Trading → Copy Trading Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.copytrade.get_existing_leading_positions(instId='')
api.copytrade.get_leading_position_history(instId='', after='', before='', limit='')
api.copytrade.place_leading_stop_order(subPosId='', tpTriggerPx='', slTriggerPx='', tpTriggerPxType='', slTriggerPxType='')
api.copytrade.close_leading_position(subPosId='')
api.copytrade.get_leading_instruments()
api.copytrade.amend_leading_instruments(instId='')
api.copytrade.get_profit_sharing_details(after='', before='', limit='')
api.copytrade.get_total_profit_sharing()
api.copytrade.get_unrealized_profit_sharing_details()
api.copytrade.get_total_unrealized_profit_sharing(instType='')
api.copytrade.apply_lead_trading(instId, instType='')
api.copytrade.stop_lead_trading(instType='')
api.copytrade.amend_profit_sharing_ratio(profitSharingRatio, instType='')
api.copytrade.get_account_configuration()
api.copytrade.first_copy_settings(instType, uniqueCode, copyMgnMode, copyInstIdType, instId='', copyMode='',copyTotalAmt='',copyAmt='', copyRatio='', tpRatio='', slRatio='', slTotalAmt='', subPosCloseType='')
api.copytrade.amend_copy_settings(instType, uniqueCode, copyMgnMode, copyInstIdType, instId='', copyMode='',copyTotalAmt='',copyAmt='', copyRatio='', tpRatio='', slRatio='', slTotalAmt='', subPosCloseType='')
api.copytrade.stop_copying(instType, uniqueCode, subPosCloseType)
api.copytrade.get_copy_settings(instType, uniqueCode)
api.copytrade.get_multiple_leverages(mgnMode, uniqueCode, instId='')
api.copytrade.set_multiple_leverages(mgnMode, lever, instId='')
api.copytrade.get_my_lead_traders(instType='')
api.copytrade.get_my_history_lead_traders(instType='', after='', before='', limit='')
api.copytrade.get_public_config(instType='')
api.copytrade.get_public_lead_traders(instType='', sortType='', state='', minLeadDays='', minAssets='', maxAssets='', minAum='', maxAum='', dataVer='', page='', limit='')
api.copytrade.get_public_weekly_pnl(instType, uniqueCode)
api.copytrade.get_public_daily_pnl(instType, uniqueCode, lastDays)
api.copytrade.get_public_stats(instType, uniqueCode, lastDays)
api.copytrade.get_public_preference_currency(instType, uniqueCode)
api.copytrade.get_public_current_subpositions(instType, uniqueCode, after='', before='', limit='')
api.copytrade.get_public_subpositions_history(instType, uniqueCode, after='', before='', limit='')
api.copytrade.get_public_copy_traders(instType, uniqueCode, limit='')
api.copytrade.get_lead_traders(instType='', sortType='', state='', minLeadDays='', minAssets='', maxAssets='', minAum='', maxAum='', dataVer='', page='', limit='')
api.copytrade.get_weekly_pnl(instType, uniqueCode)
api.copytrade.get_daily_pnl(instType, uniqueCode, lastDays)
api.copytrade.get_stats(instType, uniqueCode, lastDays)
api.copytrade.get_preference_currency(instType, uniqueCode)
api.copytrade.get_performance_current_subpositions(instType, uniqueCode, after='', before='', limit='')
api.copytrade.get_performance_subpositions_history(instType, uniqueCode, after='', before='', limit='')
api.copytrade.get_copy_traders(instType, uniqueCode, limit='')
```

#### Order Book Trading → Grid Trading Client Methods

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.gridtrade.place_order(instId, algoOrdType, maxPx, minPx, gridNum, runType='', tpTriggerPx='', slTriggerPx='', quoteSz='', baseSz='', sz='', direction='', lever='', basePos='')
api.gridtrade.amend_order(algoId, instId, slTriggerPx='', tpTriggerPx='')
api.gridtrade.stop_order(algoId, instId, algoOrdType, stopType)
api.gridtrade.close_position(algoId, mktClose, sz='', px='')
api.gridtrade.cancel_close_position_order(algoId, ordId)
api.gridtrade.get_pending_orders(algoOrdType='', algoId='', instId='', instType='', after='', before='', limit='', instFamily='')
api.gridtrade.get_orders_history(algoOrdType='', algoId='', instId='', instType='', after='', before='', limit='', instFamily='')
api.gridtrade.get_orders_details(algoOrdType='', algoId='')
api.gridtrade.get_sub_orders(algoId='', algoOrdType='', type='', groupId='', after='', before='', limit='')
api.gridtrade.get_positions(algoOrdType='', algoId='')
api.gridtrade.withdraw_income(algoId='')
api.gridtrade.compute_margin_balance(algoId='', type='', amt='')
api.gridtrade.adjust_margin_balance(algoId='', type='', amt='', percent='')
api.gridtrade.get_ai_param(algoOrdType='', instId='', direction='', duration='')
api.gridtrade.compute_min_investment(instId, algoOrdType, maxPx, minPx, gridNum, runType, direction='', lever='', basePos='', investmentData=[])
api.gridtrade.get_rsi_back_testing(instId, timeframe, thold, timePeriod, triggerCond='', duration='')
```

#### Order Book Trading → Recuring Buy Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.recurringbuy.place_recurring_buy_order(stgyName='', recurringList=[], period='', recurringDay='', recurringTime='', timeZone='', amt='', investmentCcy='', tdMode='', algoClOrdId='')
api.recurringbuy.amend_recurring_buy_order(algoId='', stgyName='')
api.recurringbuy.stop_recurring_buy_order(orders_data)
api.recurringbuy.get_recurring_buy_order_list(algoId='', after='', before='', limit='')
api.recurringbuy.get_recurring_buy_order_history(algoId='', after='', before='', limit='')
api.recurringbuy.get_recurring_buy_order_details(algoId='')
api.recurringbuy.get_recurring_buy_sub_orders(algoId='', ordId='', after='', before='', limit='')
```

#### Order Book Trading → Signal Bot Trading Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.signaltrade.create_signal(signalChanName, signalChanDesc='')
api.signaltrade.get_signals(signalSourceType, signalChanId='', after='', before='', limit='')
api.signaltrade.create(signalChanId, lever, investAmt, subOrdType, includeAll='', instIds='', ratio='', entrySettingParam={},exitSettingParam={})
api.signaltrade.cancel(algoId)
api.signaltrade.adjust_margin_balance(algoId, type, amt, allowReinvest=False)
api.signaltrade.amend_tpsl(algoId, exitSettingParam={})
api.signaltrade.set_instruments(algoId, instIds=[], includeAll=False)
api.signaltrade.get_order(algoOrdType, algoId)
api.signaltrade.get_active(algoOrdType, algoId, after='', before='', limit='')
api.signaltrade.get_history(algoOrdType, algoId, after='', before='', limit='')
api.signaltrade.get_positions(algoOrdType, algoId)
api.signaltrade.get_position_history(algoId='', instId='', after='', before='', limit='')
api.signaltrade.close_position(algoId, instId)
api.signaltrade.place_sub_order(algoId, instId, side, ordType, sz, px='', reduceOnly=False)
api.signaltrade.cancel_sub_order(algoId, instId, signalOrdId)
api.signaltrade.get_sub_orders(algoId, algoOrdType, type='', clOrdId='', state='', signalOrdId='', after='', before='', begin='', end='', limit='')
api.signaltrade.get_bot_events(algoId, after='', before='', limit='')
```

#### Block Trading Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.blocktrade.counterparties()
api.blocktrade.create_rfq(counterparties=[], anonymous='false', clRfqId='', allowPartialExecution='false', legs=[])
api.blocktrade.cancel_rfq(rfqId='', clRfqId='')
api.blocktrade.cancel_batch_rfqs(rfqIds=[], clRfqIds=[])
api.blocktrade.cancel_all_rfqs()
api.blocktrade.execute_quote(rfqId='', quoteId='', legs=[])
api.blocktrade.get_quote_products()
api.blocktrade.set_marker_instrument(params=[])
api.blocktrade.reset_mmp()
api.blocktrade.set_mmp_config(timeInterval, frozenInterval, countLimit)
api.blocktrade.get_mmp_config(timeInterval='', frozenInterval='', countLimit='', mmpFrozen='', mmpFrozenUntil='')
api.blocktrade.create_quote(rfqId='', clQuoteId='', quoteSide='', legs=[], anonymous=False, expiresIn='')
api.blocktrade.cancel_quote(quoteId='', clQuoteId='')
api.blocktrade.cancel_batch_quotes(quoteIds='', clQuoteIds='')
api.blocktrade.cancel_all_quotes()
api.blocktrade.get_rfqs(rfqId='', clRfqId='', state='', beginId='', endId='', limit='')
api.blocktrade.get_quotes(rfqId='', clRfqId='', quoteId='', clQuoteId='', state='', beginId='', endId='', limit='')
api.blocktrade.get_trades(rfqId='', clRfqId='', quoteId='', clQuoteId='', state='', beginId='', endId='', beginTs='', endTs='', limit='')
api.blocktrade.get_public_trades(beginId='', endId='', limit='')
api.blocktrade.get_block_tickers(instType='', uly='', instFamily='')
api.blocktrade.get_block_ticker(instId='')
api.blocktrade.get_block_trades(instId='')
```

#### Spread Trading Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.spreadtrade.place_order(sprdId='', clOrdId='', side='', ordType='', sz='', px='')
api.spreadtrade.cancel_order(ordId='', clOrdId='')
api.spreadtrade.cancel_all_orders(sprdId='')
api.spreadtrade.amend_order(ordId='', clOrdId='', reqId='', newSz='', newPx='')
api.spreadtrade.get_order_details(ordId='', clOrdId='')
api.spreadtrade.get_active_orders(sprdId='', ordType='', state='', beginId='', endId='', limit='')
api.spreadtrade.get_orders_history(sprdId='', ordType='', state='', beginId='', endId='', begin='', end='', limit='')
api.spreadtrade.get_orders_archive(sprdId='', ordType='', state='', instType='', instFamily='', beginId='', endId='', begin='', end='', limit='')
api.spreadtrade.get_trades(sprdId='', tradeId='', ordId='', beginId='', endId='', begin='', end='', limit='')
api.spreadtrade.get_spreads(baseCcy='', instId='', sprdId='', state='')
api.spreadtrade.get_order_book(sprdId='', sz='')
api.spreadtrade.get_ticker(sprdId='')
api.spreadtrade.get_public_trades(sprdId='')
```

#### Financial Products Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.finance.earn_get_offers(productId='', protocolType='', ccy='')
api.finance.earn_purchase(productId='', investData=[], term='')
api.finance.earn_redeem(ordId='', protocolType='', allowEarlyRedeem='')
api.finance.earn_cancel(ordId='', protocolType='')
api.finance.earn_get_active_orders(productId='', protocolType='', ccy='', state='')
api.finance.earn_get_orders_history(productId='', protocolType='', ccy='', after='', before='', limit='')
api.finance.eth_purchase(amt)
api.finance.eth_redeem(amt)
api.finance.eth_get_balance()
api.finance.eth_get_purchase_redeem_history(type, status='', after='', before='', limit='')
api.finance.eth_apy_history(days)
api.finance.savings_get_saving_balance(ccy='')
api.finance.savings_purchase_redemption(ccy='', amt='', side='', rate='')
api.finance.savings_set_lending_rate(ccy='', rate='')
api.finance.savings_get_lending_history(ccy='', after='', before='', limit='')
api.finance.savings_get_public_borrow_info(ccy='')
api.finance.savings_get_public_borrow_history(ccy='', after='', before='', limit='')
```

#### Trading Statistics Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.rubik.get_support_coin()
api.rubik.get_taker_volume(ccy, instType, begin='', end='', period='')
api.rubik.get_margin_lending_ratio(ccy, begin='', end='', period='')
api.rubik.get_long_short_ratio(ccy, begin='', end='', period='')
api.rubik.get_contracts_interest_volume(ccy, begin='', end='', period='')
api.rubik.get_options_interest_volume(ccy, period='')
api.rubik.get_put_call_ratio(ccy, period='')
api.rubik.get_interest_volume_expiry(ccy, period='')
api.rubik.get_interest_volume_strike(ccy, expTime, period='')
api.rubik.get_taker_block_volume(ccy, period='')
```

#### Non-Disclosed Broker Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.ndbroker.get_broker_info()
api.ndbroker.create_subaccount(subAcct='', label='')
api.ndbroker.delete_subaccount(subAcct='')
api.ndbroker.get_subaccount_info(subAcct='', page='', limit='')
api.ndbroker.create_subaccount_apikey(subAcct='', label='', passphrase='', ip='', perm='')
api.ndbroker.get_subaccount_apikey(subAcct='', apiKey='')
api.ndbroker.reset_subaccount_apikey(subAcct='', apiKey='', label='', perm='', ip='')
api.ndbroker.delete_subaccount_apikey(subAcct='', apiKey='')
api.ndbroker.set_subaccount_level(subAcct='', acctLv='')
api.ndbroker.set_subaccount_fee_rate(subAcct='', instType='', chgType='', chgTaker='', chgMaker='', effDate='')
api.ndbroker.create_subaccount_deposit_address(subAcct='', ccy='', chain='', addrType='', to='')
api.ndbroker.reset_subaccount_deposit_address(subAcct='', ccy='', chain='', addr='', to='')
api.ndbroker.get_subaccount_deposit_address(subAcct='', ccy='')
api.ndbroker.get_subaccount_deposit_history(subAcct='', ccy='', txId='', state='', after='', before='', limit='')
api.ndbroker.get_subaccount_withdrawal_history(subAcct='', ccy='', wdId='', clientId='', txId='', type='', state='', before='', limit='')
api.ndbroker.get_rebate_daily(subAcct='', begin='', end='', page='', limit='')
api.ndbroker.get_rebate_details_download_link(type='', begin='', end='')
api.ndbroker.generate_rebate_details_download_link(begin='', end='')
api.ndbroker.get_dcd_products(ccy, alternativeCcy, optType, tag)
api.ndbroker.request_dcd_quote(notional, notionalCcy, productId, tag, markUp='', clReqId='')
api.ndbroker.exec_dcd_order(quoteId, clReqId='')
api.ndbroker.get_dcd_order(ordId='', clReqId='')
api.ndbroker.get_dcd_orders(productId='', uly='', state='', beginId='', endId='', begin='', end='', limit='')
api.ndbroker.set_subaccount_asset(subAcct, ccy)
api.ndbroker.report_subaccount_ip(subAcct, clientIP)
api.ndbroker.get_rebate_info(apiKey='', uid='', subAcct='')
```

#### Fully-Disclosed Broker Client

```python
from okx import OkxRestClient

api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
api.fdbroker.get_rebate_details_download_link(type='', begin='', end='')
api.fdbroker.generate_rebate_details_download_link(begin='', end='')
api.fdbroker.get_users_broker_rebate_information(apiKey, brokerType)
```
