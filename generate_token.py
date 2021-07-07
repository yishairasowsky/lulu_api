import requests
from constants import SANDBOX_BASE_URL, data, headers
# Generate token
TOKEN_ENDPOINT = SANDBOX_BASE_URL + "/auth/realms/glasstree/protocol/openid-connect/token"
response = requests.post(url=TOKEN_ENDPOINT, data=data, headers=headers)
access_json = response.json()
access_token = access_json['access_token'] # https://api.lulu.com/docs/#:~:text=that%20contains%20an-,access_token,-key%3A

# Make authenticated requests
Authorization = f'Bearer {access_token}'
print('Authorization')
print(Authorization)
