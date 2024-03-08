# OKX V5 API Python SDK

## Overview

**okx-sdk** is up-to-date, most-complete, well-organized, well-documented, easy-to-use OKX Exchange Rest and Websocket API SDK for Python.

### Links

Documentation: [https://www.okx.com/docs-v5/en](https://www.okx.com/docs-v5/en)  
Github: [https://github.com/burakoner/okx-sdk](https://github.com/burakoner/okx-sdk)  
PyPI: [https://pypi.org/project/okx-sdk/](https://pypi.org/project/okx-sdk/)  

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

- Use your terminal to install okx-sdk

```python
pip install okx-sdk
```

#### Using Rest API

- Import library as below

```python
from okx import *
```

or

```python
from okx import OkxRestClient
```

- Build your API Client. You can use OKX API public endpoints without credentials. If you need to use private endpoints you need to provide credentials as below.

```python
api = OkxRestClient()
```

or

```python
api = OkxRestClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
```

- Make request

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
```

or

```python
from okx import OkxSocketClient
```

You can define WebScoket API Client as below

```python
ws = OkxSocketClient()
```

or

```python
ws = OkxSocketClient('---API-KEY---', '---API-SECRET---', '---PASS-PHRASE---')
```

to be continued...

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
