# Attempt to implement this https://api.lulu.com/docs/#section/Getting-Started/Generate-a-Token
import requests
from private_info import Client_key, Client_secret, Base64 # obtained from https://api.sandbox.lulu.com/user-profile/api-keys
url = 'https://api.lulu.com/auth/realms/glasstree/protocol/openid-connect/token'
data = {
    "grant_type":"client_credentials",
    }
params = {
    'client_key':Client_key,
    'client_secret':Client_secret,
}
headers = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Authorization':Base64,
    }
r = requests.post(url=url, data=data, headers=headers,params=params)
print(r.json())