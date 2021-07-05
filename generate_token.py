# Attempt to implement this https://api.lulu.com/docs/#section/Getting-Started/Generate-a-Token
import requests
from private_info import Base64 # obtained from https://api.sandbox.lulu.com/user-profile/api-keys

url = 'https://api.sandbox.lulu.com/auth/realms/glasstree/protocol/openid-connect/token'
data = {"grant_type":"client_credentials"}
headers = {'Authorization':Base64}
response = requests.post(url=url, data=data, headers=headers)
json_data = response.json()
print(json_data)