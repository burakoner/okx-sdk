from .constants import *
from .restapi import *


class OkxRestApiClient:

    def __init__(self, apikey='', apisecret='', passphrase='', 
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):

        self.account = AccountClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.funding = FundingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.subaccount = SubAccountClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

        self.public = PublicDataClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.market = PublicDataClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        
        self.trade = TradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.algotrade = AlgoTradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.blocktrade = BlockTradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.copytrade = CopyTradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.gridtrade = GridTradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.signaltrade = SignalTradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.spreadtrade = SpreadTradingClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.recurringbuy = RecurringBuyClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        
        self.finance = FinanceClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.rubik = RubikClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        
        self.ndbroker = NonDisclosedBrokerClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)
        self.fdbroker = FullyDisclosedBrokerClient(apikey, apisecret, passphrase, use_server_time, simulation, domain, debug, proxy)

