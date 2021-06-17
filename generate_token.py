import requests

url = 'https://api.lulu.com/auth/realms/glasstree/protocol/openid-connect/token'

data = 'grant_type=client_credentials'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    }

x = requests.post(url=url, data=data, headers=headers)

print(x.json())

pass