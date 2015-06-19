import urllib2
import urllib
import json

from sportcourts import settings


def build_login_link(redirect_uri, host='', scope=''):
    raw_link = 'https://oauth.vk.com/authorize?client_id={appid}&scope={scope}&redirect_uri=http://{host}{redirect_uri}&response_type=code&v=5.27'
    if not host:
        host = settings.CURRENT_HOST
    if not redirect_uri.startswith('/'):
        redirect_uri = '/' + redirect_uri
    raw_link = raw_link.format(scope=scope, host=host, redirect_uri=redirect_uri, appid=settings.VKONTAKTE['APPID'])
    return raw_link