# Url
API_URL = 'https://www.okx.com'
WS_URL_PUBLIC = 'wss://ws.okx.com:8443/ws/v5/public'
WS_URL_PRIVATE = 'wss://ws.okx.com:8443/ws/v5/private'
WS_URL_BUSINESS = 'wss://ws.okx.com:8443/ws/v5/business'

# Methods
GET = "GET"
POST = "POST"

# Headers
CONTENT_TYPE = 'Content-Type'
APPLICATION_JSON = 'application/json'

# Headers
OK_ACCESS_KEY = 'OK-ACCESS-KEY'
OK_ACCESS_SIGN = 'OK-ACCESS-SIGN'
OK_ACCESS_TIMESTAMP = 'OK-ACCESS-TIMESTAMP'
OK_ACCESS_PASSPHRASE = 'OK-ACCESS-PASSPHRASE'

# Broker Id
BROKER_ID = '538a3965e538BCDE'

# Trading Account Endpoints
# /api/v5/account/instruments
ACCOUNT_BALANCE = '/api/v5/account/balance'
ACCOUNT_POSITIONS = '/api/v5/account/positions'
ACCOUNT_POSITIONS_HISTORY = '/api/v5/account/positions-history'
ACCOUNT_ACCOUNT_POSITION_RISK = '/api/v5/account/account-position-risk'
ACCOUNT_BILLS = '/api/v5/account/bills'
ACCOUNT_BILLS_ARCHIVE = '/api/v5/account/bills-archive'
# /api/v5/account/bills-history-archive
# /api/v5/account/bills-history-archive
ACCOUNT_CONFIG = '/api/v5/account/config'
ACCOUNT_SET_POSITION_MODE = '/api/v5/account/set-position-mode'
ACCOUNT_SET_LEVERAGE = '/api/v5/account/set-leverage'
ACCOUNT_MAX_SIZE = '/api/v5/account/max-size'
ACCOUNT_MAX_AVAIL_SIZE = '/api/v5/account/max-avail-size'
ACCOUNT_POSITION_MARGIN_BALANCE = '/api/v5/account/position/margin-balance'
ACCOUNT_LEVERAGE_INFO = '/api/v5/account/leverage-info'
ACCOUNT_ADJUST_LEVERAGE_INFO = '/api/v5/account/adjust-leverage-info'
ACCOUNT_MAX_LOAN = '/api/v5/account/max-loan'
ACCOUNT_TRADE_FEE = '/api/v5/account/trade-fee'
ACCOUNT_INTEREST_ACCRUED = '/api/v5/account/interest-accrued'
ACCOUNT_INTEREST_RATE = '/api/v5/account/interest-rate'
ACCOUNT_SET_GREEKS = '/api/v5/account/set-greeks'
ACCOUNT_ISOLATED_MODE = '/api/v5/account/set-isolated-mode'
ACCOUNT_MAX_WITHDRAWAL = '/api/v5/account/max-withdrawal'
ACCOUNT_RISK_STATE = '/api/v5/account/risk-state'
ACCOUNT_INTEREST_LIMITS = '/api/v5/account/interest-limits'
# /api/v5/account/spot-manual-borrow-repay
# /api/v5/account/set-auto-repay
# /api/v5/account/spot-borrow-repay-history
ACCOUNT_POSITION_BUILDER = '/api/v5/account/position-builder'
# /api/v5/account/position-builder-graph
# /api/v5/account/set-riskOffset-amt
ACCOUNT_GREEKS = '/api/v5/account/greeks'
ACCOUNT_POSITION_TIERS = '/api/v5/account/position-tiers'
ACCOUNT_ACTIVATE_OPTION = '/api/v5/account/activate-option'
ACCOUNT_SET_AUTO_LOAN = '/api/v5/account/set-auto-loan'
# /api/v5/account/account-level-switch-preset
# /api/v5/account/set-account-switch-precheck
ACCOUNT_SET_ACCOUNT_LEVEL = '/api/v5/account/set-account-level'
# api/v5/account/set-collateral-assets
# /api/v5/account/collateral-assets
ACCOUNT_MMP_RESET = '/api/v5/account/mmp-reset'
ACCOUNT_SET_MMP_CONFIG = '/api/v5/account/mmp-config'
ACCOUNT_GET_MMP_CONFIG = '/api/v5/account/mmp-config'
# /api/v5/account/move-positions
# /api/v5/account/move-positions-history
# /api/v5/account/set-auto-earn

# Order Book Trading >> Trade Endpoints
TRADE_PLACE_ORDER = '/api/v5/trade/order'
TRADE_BATCH_ORDERS = '/api/v5/trade/batch-orders'
TRADE_CANCEL_ORDER = '/api/v5/trade/cancel-order'
TRADE_CANCEL_BATCH_ORDERS = '/api/v5/trade/cancel-batch-orders'
TRADE_AMEND_ORDER = '/api/v5/trade/amend-order'
TRADE_AMEND_BATCH_ORDER = '/api/v5/trade/amend-batch-orders'
TRADE_CLOSE_POSITION = '/api/v5/trade/close-position'
TRADE_GET_ORDER = '/api/v5/trade/order'
TRADE_ORDERS_PENDING = '/api/v5/trade/orders-pending'
TRADE_ORDERS_HISTORY = '/api/v5/trade/orders-history'
TRADE_ORDERS_HISTORY_ARCHIVE = '/api/v5/trade/orders-history-archive'
TRADE_FILLS = '/api/v5/trade/fills'
TRADE_FILLS_HISTORY = '/api/v5/trade/fills-history'
TRADE_EASY_CONVERT_CURRENCY_LIST = '/api/v5/trade/easy-convert-currency-list'
TRADE_EASY_CONVERT = '/api/v5/trade/easy-convert'
TRADE_CONVERT_EASY_HISTORY = '/api/v5/trade/easy-convert-history'
TRADE_ONE_CLICK_REPAY_CURRENCY_LIST = '/api/v5/trade/one-click-repay-currency-list'
TRADE_ONE_CLICK_REPAY = '/api/v5/trade/one-click-repay'
TRADE_ONE_CLICK_REPAY_HISTORY = '/api/v5/trade/one-click-repay-history'
# /api/v5/trade/one-click-repay-currency-list-v2
# /api/v5/trade/one-click-repay-v2
# /api/v5/trade/one-click-repay-history-v2
TRADE_MASS_CANCEL = '/api/v5/trade/mass-cancel'
TRADE_CANCEL_ALL_AFTER = '/api/v5/trade/cancel-all-after'
TRADE_ACCOUNT_RATE_LIMIT = '/api/v5/trade/account-rate-limit'
# /api/v5/trade/order-prechec

# Order Book Trading >> Algo Trading Endpoints
TRADE_PLACE_ALGO_ORDER = '/api/v5/trade/order-algo'
TRADE_CANCEL_ALGOS = '/api/v5/trade/cancel-algos'
TRADE_AMEND_ALGOS = '/api/v5/trade/amend-algos'
TRADE_GET_ALGO_ORDER = '/api/v5/trade/order-algo'
TRADE_ORDERS_ALGO_PENDING = '/api/v5/trade/orders-algo-pending'
TRADE_ORDERS_ALGO_HISTORY = '/api/v5/trade/orders-algo-history'

# Order Book Trading >> Grid Trading Endpoints
GRID_ORDER_ALGO = '/api/v5/tradingBot/grid/order-algo'
GRID_AMEND_ORDER_ALGO = '/api/v5/tradingBot/grid/amend-order-algo'
GRID_STOP_ORDER_ALGO = '/api/v5/tradingBot/grid/stop-order-algo'
GRID_CLOSE_POSITION = '/api/v5/tradingBot/grid/close-position'
GRID_CANCEL_CLOSE_ORDER = '/api/v5/tradingBot/grid/cancel-close-order'
GRID_ORDER_INSTANT_TRIGGER = '/api/v5/tradingBot/grid/order-instant-trigger'
GRID_ORDERS_ALGO_PENDING = '/api/v5/tradingBot/grid/orders-algo-pending'
GRID_ORDERS_ALGO_HISTORY = '/api/v5/tradingBot/grid/orders-algo-history'
GRID_ORDERS_ALGO_DETAILS = '/api/v5/tradingBot/grid/orders-algo-details'
GRID_SUB_ORDERS = '/api/v5/tradingBot/grid/sub-orders'
GRID_POSITIONS = '/api/v5/tradingBot/grid/positions'
GRID_WITHDRAW_INCOME = '/api/v5/tradingBot/grid/withdraw-income'
GRID_COMPUTE_MARGIN_BALANCE = '/api/v5/tradingBot/grid/compute-margin-balance'
GRID_MARGIN_BALANCE = '/api/v5/tradingBot/grid/margin-balance'
GRID_AI_PARAM = '/api/v5/tradingBot/grid/ai-param'
GRID_MIN_INVESTMENT = '/api/v5/tradingBot/grid/min-investment'
GRID_RSI_BACK_TESTING = '/api/v5/tradingBot/public/rsi-back-testing'
GRID_QUANTITY = '/api/v5/tradingBot/grid/grid-quantity'

# Order Book Trading >> Signal Trading Endpoints
SIGNAL_CREATE_SIGNAL = '/api/v5/tradingBot/signal/create-signal'
SIGNAL_SIGNALS = '/api/v5/tradingBot/signal/signals'
SIGNAL_ORDER_ALGO = '/api/v5/tradingBot/signal/order-algo'
SIGNAL_STOP_ORDER_ALGO = '/api/v5/tradingBot/signal/stop-order-algo'
SIGNAL_MARGIN_BALANCE = '/api/v5/tradingBot/signal/margin-balance'
SIGNAL_AMEND_TPSL = '/api/v5/tradingBot/signal/amendTPSL'
SIGNAL_SET_INSTRUMENTS = '/api/v5/tradingBot/signal/set-instruments'
SIGNAL_ORDERS_ALGO_DETAILS = '/api/v5/tradingBot/signal/orders-algo-details'
SIGNAL_ORDERS_ALGO_HISTORY = '/api/v5/tradingBot/signal/orders-algo-history'
SIGNAL_POSITIONS = '/api/v5/tradingBot/signal/positions'
SIGNAL_POSITIONS_HISTORY = '/api/v5/tradingBot/signal/positions-history'
SIGNAL_CLOSE_POSITION = '/api/v5/tradingBot/signal/close-position'
SIGNAL_SUB_ORDER = '/api/v5/tradingBot/signal/sub-order'
SIGNAL_CANCEL_SUB_ORDER = '/api/v5/tradingBot/signal/cancel-sub-order'
SIGNAL_SUB_ORDERS = '/api/v5/tradingBot/signal/sub-orders'
SIGNAL_EVENT_HISTORY = '/api/v5/tradingBot/signal/event-history'

# Order Book Trading >> Recurring Buy Endpoints
RECURRING_ORDER_ALGO = '/api/v5/tradingBot/recurring/order-algo'
RECURRING_AMEND_ORDER_ALGO = '/api/v5/tradingBot/recurring/amend-order-algo'
RECURRING_STOP_ORDER_ALGO = '/api/v5/tradingBot/recurring/stop-order-algo'
RECURRING_ORDERS_ALGO_PENDING = '/api/v5/tradingBot/recurring/orders-algo-pending'
RECURRING_ORDERS_ALGO_HISTORY = '/api/v5/tradingBot/recurring/orders-algo-history'
RECURRING_ORDERS_ALGO_DETAILS = '/api/v5/tradingBot/recurring/orders-algo-details'
RECURRING_SUB_ORDERS = '/api/v5/tradingBot/recurring/sub-orders'

# Order Book Trading >> Copy Trading Endpoints
COPYTRADING_CURRENT_SUBPOSITIONS = '/api/v5/copytrading/current-subpositions'
COPYTRADING_SUBPOSITIONS_HISTORY = '/api/v5/copytrading/subpositions-history'
COPYTRADING_ALGO_ORDER = '/api/v5/copytrading/algo-order'
COPYTRADING_CLOSE_SUBPOSITION = '/api/v5/copytrading/close-subposition'
COPYTRADING_INSTRUMENTS = '/api/v5/copytrading/instruments'
COPYTRADING_SET_INSTRUMENTS = '/api/v5/copytrading/set-instruments'
COPYTRADING_PROFIT_SHARING_DETAILS = '/api/v5/copytrading/profit-sharing-details'
COPYTRADING_TOTAL_PROFIT_SHARING = '/api/v5/copytrading/total-profit-sharing'
COPYTRADING_UNREALIZED_PROFIT_SHARING_DETAILS = '/api/v5/copytrading/unrealized-profit-sharing-details'
COPYTRADING_TOTAL_UNREALIZED_PROFIT_SHARING = '/api/v5/copytrading/total-unrealized-profit-sharing'
COPYTRADING_AMEND_PROFIT_SHARING_RATIO = '/api/v5/copytrading/amend-profit-sharing-ratio'
COPYTRADING_CONFIG = '/api/v5/copytrading/config'
COPYTRADING_FIRST_COPY_SETTINGS = '/api/v5/copytrading/first-copy-settings'
COPYTRADING_AMEND_COPY_SETTINGS = '/api/v5/copytrading/amend-copy-settings'
COPYTRADING_STOP_COPY_TRADING = '/api/v5/copytrading/stop-copy-trading'
COPYTRADING_COPY_SETTINGS = '/api/v5/copytrading/copy-settings'
COPYTRADING_CURRENT_LEAD_TRADERS = '/api/v5/copytrading/current-lead-traders'
COPYTRADING_PUBLIC_CONFIG = '/api/v5/copytrading/public-config'
COPYTRADING_PUBLIC_LEAD_TRADERS = '/api/v5/copytrading/public-lead-traders'
COPYTRADING_PUBLIC_WEEKLY_PNL = '/api/v5/copytrading/public-weekly-pnl'
COPYTRADING_PUBLIC_PNL = '/api/v5/copytrading/public-pnl'
COPYTRADING_PUBLIC_STATS = '/api/v5/copytrading/public-stats'
COPYTRADING_PUBLIC_PREFERENCE_CURRENCY = '/api/v5/copytrading/public-preference-currency'
COPYTRADING_PUBLIC_CURRENT_SUBPOSITIONS = '/api/v5/copytrading/public-current-subpositions'
COPYTRADING_PUBLIC_SUBPOSITIONS_HISTORY = '/api/v5/copytrading/public-subpositions-history'
COPYTRADING_PUBLIC_COPY_TRADERS = '/api/v5/copytrading/public-copy-traders'

# Market Data Endpoints
MARKET_TICKERS = '/api/v5/market/tickers'
MARKET_TICKER = '/api/v5/market/ticker'
MARKET_BOOKS = '/api/v5/market/books'
MARKET_BOOKS_FULL = '/api/v5/market/books-full'
MARKET_CANDLES = '/api/v5/market/candles'
MARKET_HISTORY_CANDLES = '/api/v5/market/history-candles'
MARKET_TRADES = '/api/v5/market/trades'
MARKET_HISTORY_TRADES = '/api/v5/market/history-trades'
MARKET_OPTION_INSTRUMENT_FAMILY_TRADES = '/api/v5/market/option/instrument-family-trades'
PUBLIC_OPTION_TRADES = '/api/v5/public/option-trades'
MARKET_PLATFORM_24_VOLUME = '/api/v5/market/platform-24-volume'
# /api/v5/market/call-auction-details

# Block Trading Endpoints
RFQ_COUNTERPARTIES = '/api/v5/rfq/counterparties'
RFQ_CREATE_RFQ = '/api/v5/rfq/create-rfq'
RFQ_CANCEL_RFQ = '/api/v5/rfq/cancel-rfq'
RFQ_CANCEL_BATCH_RFQS = '/api/v5/rfq/cancel-batch-rfqs'
RFQ_CANCEL_ALL_RSQS = '/api/v5/rfq/cancel-all-rfqs'
RFQ_EXECUTE_QUOTE = '/api/v5/rfq/execute-quote'
RFQ_GET_MARKER_INSTRUMENT_SETTING = '/api/v5/rfq/maker-instrument-settings'
RFQ_SET_MARKER_INSTRUMENT_SETTING = '/api/v5/rfq/maker-instrument-settings'
RFQ_MMP_RESET = '/api/v5/rfq/mmp-reset'
RFQ_SET_MMP_CONFIG = '/api/v5/rfq/mmp-config'
RFQ_GET_MMP_CONFIG = '/api/v5/rfq/mmp-config'
RFQ_CREATE_QUOTE = '/api/v5/rfq/create-quote'
RFQ_CANCEL_QUOTE = '/api/v5/rfq/cancel-quote'
RFQ_CANCEL_BATCH_QUOTES = '/api/v5/rfq/cancel-batch-quotes'
RFQ_CANCEL_ALL_QUOTES = '/api/v5/rfq/cancel-all-quotes'
# /api/v5/rfq/cancel-all-after
RFQ_RFQS = '/api/v5/rfq/rfqs'
RFQ_QUOTES = '/api/v5/rfq/quotes'
RFQ_TRADES = '/api/v5/rfq/trades'
# /api/v5/market/block-tickers
# /api/v5/market/block-ticker
RFQ_PUBLIC_TRADES = '/api/v5/rfq/public-trades'
# /api/v5/public/block-trades

# Spread Trading Endpoints
SPREAD_PLACE_ORDER = '/api/v5/sprd/order'
SPREAD_CANCEL_ORDER = '/api/v5/sprd/cancel-order'
SPREAD_MASS_CANCEL = '/api/v5/sprd/mass-cancel'
SPREAD_AMEND_ORDER = '/api/v5/sprd/amend-order'
SPREAD_GET_ORDER = '/api/v5/sprd/order'
SPREAD_ORDERS_PENDING = '/api/v5/sprd/orders-pending'
SPREAD_ORDERS_HISTORY = '/api/v5/sprd/orders-history'
SPREAD_ORDERS_HISTORY_ARCHIVE = '/api/v5/sprd/orders-history-archive'
SPREAD_TRADES = '/api/v5/sprd/trades'
SPREAD_SPREADS = '/api/v5/sprd/spreads'
SPREAD_BOOKS = '/api/v5/sprd/books'
SPREAD_TICKER = '/api/v5/sprd/ticker'
SPREAD_PUBLIC_TRADES = '/api/v5/sprd/public-trades'
# /api/v5/market/sprd-candles
# /api/v5/market/sprd-history-candles
# /api/v5/sprd/cancel-all-after

# Public Data Endpoints
PUBLIC_INSTRUMENTS = '/api/v5/public/instruments'
PUBLIC_ESTIMATED_PRICE = '/api/v5/public/estimated-price'
PUBLIC_DELIVERY_EXERCISE_HISTORY = '/api/v5/public/delivery-exercise-history'
# /api/v5/public/estimated-settlement-info
# /api/v5/public/settlement-history
PUBLIC_FUNDING_RATE = '/api/v5/public/funding-rate'
PUBLIC_FUNDING_RATE_HISTORY = '/api/v5/public/funding-rate-history'
PUBLIC_OPEN_INTEREST = '/api/v5/public/open-interest'
PUBLIC_PRICE_LIMIT = '/api/v5/public/price-limit'
PUBLIC_OPT_SUMMARY = '/api/v5/public/opt-summary'
PUBLIC_DISCOUNT_RATE_INTETEST_FREE_QUOTA = '/api/v5/public/discount-rate-interest-free-quota'
PUBLIC_MARK_PRICE = '/api/v5/public/mark-price'
PUBLIC_POSITION_TIERS = '/api/v5/public/position-tiers'
PUBLIC_INTEREST_RATE_LOAN_QUOTA = '/api/v5/public/interest-rate-loan-quota'
PUBLIC_UNDERLYING = '/api/v5/public/underlying'
PUBLIC_INSURANCE_FUND = '/api/v5/public/insurance-fund'
PUBLIC_CONVERT_CONTRACT_COIN = '/api/v5/public/convert-contract-coin'
PUBLIC_INSTRUMENT_TICK_BANDS = '/api/v5/public/instrument-tick-bands'
# /api/v5/public/premium-history
MARKET_INDEX_TICKERS = '/api/v5/market/index-tickers'
MARKET_INDEX_CANDLES = '/api/v5/market/index-candles'
MARKET_HISTORY_INDEX_CANDLES = '/api/v5/market/history-index-candles'
MARKET_MARK_PRICE_CANDLES = '/api/v5/market/mark-price-candles'
MARKET_HISTORY_MARK_PRICE_CANDLES = '/api/v5/market/history-mark-price-candles'
MARKET_EXCHANGE_RATE = '/api/v5/market/exchange-rate'
MARKET_INDEX_COMPONENTS = '/api/v5/market/index-components'
PUBLIC_ECONOMIC_CALENDAR = '/api/v5/public/economic-calendar'

# System Endpoints
SYSTEM_TIME = '/api/v5/public/time'
SYSTEM_STATUS = '/api/v5/system/status'

# Trading Statistics Endpoints
RUBIK_STAT_TRADING_DATA_SUPPORT_COIN = '/api/v5/rubik/stat/trading-data/support-coin'
# /api/v5/rubik/stat/contracts/open-interest-history
RUBIK_STAT_TAKER_VOLUME = '/api/v5/rubik/stat/taker-volume'
# /api/v5/rubik/stat/taker-volume-contract
RUBIK_STAT_MARGIN_LOAN_RATIO = '/api/v5/rubik/stat/margin/loan-ratio'
# /api/v5/rubik/stat/contracts/long-short-account-ratio-contract-top-trader
# /api/v5/rubik/stat/contracts/long-short-position-ratio-contract-top-trader
# /api/v5/rubik/stat/contracts/long-short-account-ratio-contract
RUBIK_STAT_CONTRACTS_LONG_SHORT_RATIO = '/api/v5/rubik/stat/contracts/long-short-account-ratio'
RUBIK_STAT_CONTRACTS_INTEREST_VOLUME = '/api/v5/rubik/stat/contracts/open-interest-volume'
RUBIK_STAT_OPTION_OPEN_INTEREST_VOLUME = '/api/v5/rubik/stat/option/open-interest-volume'
RUBIK_STAT_OPTION_OPEN_INTEREST_RATIO = '/api/v5/rubik/stat/option/open-interest-volume-ratio'
RUBIK_STAT_OPTION_OPEN_INTEREST_VOLUME_EXPIRY = '/api/v5/rubik/stat/option/open-interest-volume-expiry'
RUBIK_STAT_OPTION_OPEN_INTEREST_VOLUME_STRIKE = '/api/v5/rubik/stat/option/open-interest-volume-strike'
RUBIK_STAT_OPTION_TAKER_BLOCK_VOLUME = '/api/v5/rubik/stat/option/taker-block-volume'

# Funding Account Endpoints
ASSET_CURRENCIES = '/api/v5/asset/currencies'
ASSET_BALANCES = '/api/v5/asset/balances'
ASSET_NON_TRADABLE_ASSETS = '/api/v5/asset/non-tradable-assets'
ASSET_ASSET_VALUATION = '/api/v5/asset/asset-valuation'
ASSET_TRANSFER = '/api/v5/asset/transfer'
ASSET_TRANSFER_STATE = '/api/v5/asset/transfer-state'
ASSET_BILLS = '/api/v5/asset/bills'
# /api/v5/asset/bills-history
ASSET_DEPOSIT_ADDRESS = '/api/v5/asset/deposit-address'
ASSET_DEPOSIT_HISTORY = '/api/v5/asset/deposit-history'
ASSET_WITHDRAWAL = '/api/v5/asset/withdrawal'
ASSET_CANCEL_WITHDRAWAL = '/api/v5/asset/cancel-withdrawal'
ASSET_WITHDRAWAL_HISTORY = '/api/v5/asset/withdrawal-history'
ASSET_DEPOSIT_WITHDRAW_STATUS = '/api/v5/asset/deposit-withdraw-status'
ASSET_EXCHANGE_LIST = '/api/v5/asset/exchange-list'
ASSET_MONTHLY_STATEMENT_APPLY = '/api/v5/asset/monthly-statement'
ASSET_MONTHLY_STATEMENT_RETRIEVE = '/api/v5/asset/monthly-statement'
ASSET_CONVERT_CURRENCIES = '/api/v5/asset/convert/currencies'
ASSET_CONVERT_CURRENCY_PAIR = '/api/v5/asset/convert/currency-pair'
ASSET_CONVERT_ESTIMATE_QUOTE = '/api/v5/asset/convert/estimate-quote'
ASSET_CONVERT_TRADE = '/api/v5/asset/convert/trade'
ASSET_CONVERT_HISTORY = '/api/v5/asset/convert/history'
# /api/v5/fiat/deposit-payment-methods
# /api/v5/fiat/withdrawal-payment-methods
# /api/v5/fiat/create-withdrawal
# /api/v5/fiat/cancel-withdrawal
# /api/v5/fiat/withdrawal-order-history
# /api/v5/fiat/withdrawal
# /api/v5/fiat/deposit-order-history
# /api/v5/fiat/deposit
# /api/v5/fiat/buy-sell/currencies
# /api/v5/fiat/buy-sell/currency-pair
# /api/v5/fiat/buy-sell/quote
# /api/v5/fiat/buy-sell/trade
# /api/v5/fiat/buy-sell/history

# SubAccount Endpoints
USERS_SUBACCOUNT_LIST = '/api/v5/users/subaccount/list'
# /api/v5/users/subaccount/create-subaccount
# /api/v5/users/subaccount/apikey
# /api/v5/users/subaccount/apikey
USERS_SUBACCOUNT_MODIFY_APIKEY = '/api/v5/users/subaccount/modify-apikey'
# /api/v5/users/subaccount/delete-apikey
ACCOUNT_SUBACCOUNT_BALANCES = '/api/v5/account/subaccount/balances'
ASSET_SUBACCOUNT_BALANCES = '/api/v5/asset/subaccount/balances'
ACCOUNT_SUBACCOUNT_MAX_WITHDRAWAL = '/api/v5/account/subaccount/max-withdrawal'
ASSET_SUBACCOUNT_BILLS = '/api/v5/asset/subaccount/bills'
ASSET_SUBACCOUNT_MANAGED_SUBACCOUNT_BILLS = '/api/v5/asset/subaccount/managed-subaccount-bills'
ASSET_SUBACCOUNT_TRANSFER = '/api/v5/asset/subaccount/transfer'
USERS_SUBACCOUNT_SET_TRANSFER_OUT = '/api/v5/users/subaccount/set-transfer-out'
USERS_ENTRUST_SUBACCOUNT_LIST = '/api/v5/users/entrust-subaccount-list'
# ACCOUNT_SUBACCOUNT_SET_LOAN_ALLOCATION = '/api/v5/account/subaccount/set-loan-allocation'
# ACCOUNT_SUBACCOUNT_INTEREST_LIMITS = '/api/v5/account/subaccount/interest-limits'

# On-chain Earn
FINANCE_STACKING_DEFI_OFFERS = '/api/v5/finance/staking-defi/offers'
FINANCE_STACKING_DEFI_PURCHASE = '/api/v5/finance/staking-defi/purchase'
FINANCE_STACKING_DEFI_REDEEM = '/api/v5/finance/staking-defi/redeem'
FINANCE_STACKING_DEFI_CANCEL = '/api/v5/finance/staking-defi/cancel'
FINANCE_STACKING_DEFI_ORDERS_ACTIVE = '/api/v5/finance/staking-defi/orders-active'
FINANCE_STACKING_DEFI_ORDERS_HISTORY = '/api/v5/finance/staking-defi/orders-history'

# ETH Staking
# /api/v5/finance/staking-defi/eth/product-info
FINANCE_STACKING_DEFI_ETH_PURCHASE = '/api/v5/finance/staking-defi/eth/purchase'
FINANCE_STACKING_DEFI_ETH_REDEEM = '/api/v5/finance/staking-defi/eth/redeem'
FINANCE_STACKING_DEFI_ETH_BALANCE = '/api/v5/finance/staking-defi/eth/balance'
FINANCE_STACKING_DEFI_ETH_PURCHASE_REDEEM_HISTORY = '/api/v5/finance/staking-defi/eth/purchase-redeem-history'
FINANCE_STACKING_DEFI_ETH_APY_HISTORY = '/api/v5/finance/staking-defi/eth/apy-history'

# SOL Staking
# /api/v5/finance/staking-defi/sol/product-info
# /api/v5/finance/staking-defi/sol/purchase
# /api/v5/finance/staking-defi/sol/redeem
# /api/v5/finance/staking-defi/sol/balance
# /api/v5/finance/staking-defi/sol/purchase-redeem-history
# /api/v5/finance/staking-defi/sol/apy-history

# Simple Earn Flexible
FINANCE_SAVINGS_BALANCE = '/api/v5/finance/savings/balance'
FINANCE_SAVINGS_PURCHASE_REDEMPT = '/api/v5/finance/savings/purchase-redempt'
FINANCE_SAVINGS_SET_LENDING_RATE = '/api/v5/finance/savings/set-lending-rate'
FINANCE_SAVINGS_LENDING_HISTORY = '/api/v5/finance/savings/lending-history'
FINANCE_SAVINGS_LENDING_RATE_SUMMARY = '/api/v5/finance/savings/lending-rate-summary'
FINANCE_SAVINGS_LENDING_RATE_HISTORY = '/api/v5/finance/savings/lending-rate-history'

# Flexible Loan
# /api/v5/finance/flexible-loan/borrow-currencies
# /api/v5/finance/flexible-loan/collateral-assets
# /api/v5/finance/flexible-loan/max-loan
# /api/v5/finance/flexible-loan/max-collateral-redeem-amount
# /api/v5/finance/flexible-loan/adjust-collateral
# /api/v5/finance/flexible-loan/loan-info
# /api/v5/finance/flexible-loan/loan-history
# /api/v5/finance/flexible-loan/interest-accrued

# Affiliate
AFFILIATE_INVITEE_DETAIL = '/api/v5/affiliate/invitee/detail'

# DMA Broker
BROKER_DMA_SUBACCOUNT_INFO = '/api/v5/broker/dma/subaccount-info'
BROKER_DMA_SUBACCOUNT_TRADE_FEE = '/api/v5/broker/dma/subaccount-trade-fee'
BROKER_DMA_ADD_SUBACCOUNT_APIKEY = '/api/v5/broker/dma/subaccount/apikey'
BROKER_DMA_GET_SUBACCOUNT_APIKEY = '/api/v5/broker/dma/subaccount/apikey'
BROKER_DMA_REBATE_PER_ORDERS = '/api/v5/broker/dma/rebate-per-orders'
BROKER_DMA_TRADES = '/api/v5/broker/dma/trades'

# Fully-Disclosed Broker Endpoints
BROKER_FD_GET_REBATE_PER_ORDERS = '/api/v5/broker/fd/rebate-per-orders'
BROKER_FD_GEN_REBATE_PER_ORDERS = '/api/v5/broker/fd/rebate-per-orders'
BROKER_FD_IF_REBATE = '/api/v5/broker/fd/if-rebate'
