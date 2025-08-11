from .BaseClient import OkxBaseClient
from ..constants import *


class AffiliateClient(OkxBaseClient):

    def __init__(self, apikey='', apisecret='', passphrase='',
                 use_server_time=False, simulation=False, domain=API_URL, debug=False, proxy=None):
        OkxBaseClient.__init__(self, apikey, apisecret, passphrase,
                               use_server_time, simulation, domain, debug, proxy)
    
    # Get the invitee's detail
    def get_invitee_details(self, uid):
        params = {'uid': uid}
        return self._request(GET, AFFILIATE_INVITEE_DETAIL, params)