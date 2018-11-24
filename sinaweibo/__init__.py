from requests import Session
from requests import exceptions

from sinaweibo.exc import RequestError


class Client:

    def __init__(self,
                 app_key,
                 app_secret,
                 redirect_uri,
                 session=Session(),
                 access_token_url="https://api.weibo.com/oauth2/access_token",
                 authorize_url="https://api.weibo.com/oauth2/authorize",
                 token_info_url="https://api.weibo.com/oauth2/get_token_info",
                 revoke_oauth2_url="https://api.weibo.com/oauth2/revokeoauth2"):
        self.app_key = app_key
        self.app_secret = app_secret
        self.redirect_uri = redirect_uri
        self.session = session
        self.access_token_url = access_token_url
        self.authorize_url = authorize_url
        self.token_info_url = token_info_url
        self.revoke_oauth2_url= revoke_oauth2_url

    def authorize(self,
                  scope=None,
                  state=None,
                  display="default",
                  forcelogin=None,
                  language=None):
        """
            {
                "code": String,
                "state": String
            }
        """
        response = self.session.post(
            self.authorize_url,
            data={
                "client_id": self.app_key,
                "redirect_uri": self.redirect_uri,
                "scope": scope,
                "state": state,
                "display": display,
                "forcelogin": forcelogin,
                "language": language
            })
        if response.status_code != 200:
            raise RequestError(response.text())
        else:
            return response.json()

    def get_access_token(self, code, grant_type='authorization_code'):
        """
            {
                "access_token": "ACCESS_TOKEN",
                "expires_in": 1234,
                "uid":"12341234"
            }
        """
        response = self.session.post(
            self.access_token_url,
            data={
                "grant_type": grant_type,
                "code": code,
                "redirect_uri": self.redirect_uri
            })
        if response.status_code != 200:
            raise RequestError(response.text())
        else:
            return response.json()

    def get_token_info(self, access_token):
        """
            {
                "uid": 1073880650,
                "appkey": 1352222456,
                "scope": null,
                "create_at": 1352267591,
                "expire_in": 157679471
            }
        """
        response = self.session.post(
            self.token_info_url, data={"access_token": access_token})
        if response.status_code != 200:
            raise RequestError(response.text())
        else:
            return response.json()

    def revoke_oauth2(self, access_token):
        response = self.session.post(
            self.revoke_oauth2_url,
            data={'access_token': self.access_token_url})
        if response.status_code != 200:
            raise RequestError(response.text())
        else:
            return response.json()
