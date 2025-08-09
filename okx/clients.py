import logging
from .constants import *
from .restapi import *
from .wsapi import *


class OkxRestClient:

    def __init__(self, apikey='', apisecret='', passphrase='', 
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):

        # Trading Account
        self.account = AccountClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        
        # Order Book Trading
        self.trade = TradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.algotrade = AlgoTradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.gridtrade = GridTradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.signaltrade = SignalTradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.recurringbuy = RecurringBuyClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.copytrade = CopyTradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.market = PublicDataClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

        # Block Trading
        self.blocktrade = BlockTradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

        # Spread Trading
        self.spreadtrade = SpreadTradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        
        # Public Data
        self.public = PublicDataClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

        # Trading Statistics        
        self.rubik = RubikClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

        # Funding Account
        self.funding = FundingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

        # Sub-account
        self.subaccount = SubAccountClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

        # Financial Product
        self.finance = FinanceClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        
        # TODO: Affiliate
        # TODO: Status
        # TODO: Announcement

        # Broker
        self.dmabroker = DmaBrokerClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.fdbroker = FullyDisclosedBrokerClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

class OkxSocketClient:

    def __init__(self, apikey='', apisecret='', passphrase='', public_url=WS_URL_PUBLIC, private_url=WS_URL_PRIVATE, business_url=WS_URL_BUSINESS, use_server_time=False, loglevel=logging.INFO):
        self.public = PublicAsyncClient(public_url, loglevel)
        self.private = PrivateAsyncClient(apikey, apisecret, passphrase, private_url, use_server_time, loglevel)
        self.business = PrivateAsyncClient(apikey, apisecret, passphrase, business_url, use_server_time, loglevel)
        