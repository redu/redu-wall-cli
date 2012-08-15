from rauth.service import OAuth2Service
import requests
import simplejson


class HttpClient(object):

    def __init__(self, consumer_key, consumer_secret):
        self.redu = OAuth2Service(
        name='redu',
        authorize_url='http://redu.com.br/oauth/authorize',
        access_token_url='http://redu.com.br/oauth/token',
        consumer_key=consumer_key,
        consumer_secret=consumer_secret)

    def getAuthorizeUrl(self):
        return self.redu.get_authorize_url()

    def initClient(self, pin):
        data = dict(code=pin,
            grant_type="authorization_code",
            redirect_uri="")
        access_token = self.redu.get_access_token("POST",
            data=data).content["access_token"]
        self.client = requests.session(params={"oauth_token": access_token},
            headers={"Content-type": "application/json"})

    def getLink(self, url):
        r = self.client.get(url).content
        return simplejson.loads(r)
