# Attempt to implement this https://api.lulu.com/docs/#section/Getting-Started/Generate-a-Token
# For help use
#  https://github.com/minireference/lulu-api-client/blob/358395d21685245f75a60094c2f7d80b6b3dddb1/luluapi.py#L67
import requests
from private_info import Base64 # obtained from https://api.sandbox.lulu.com/user-profile/api-keys

SANDBOX_BASE_URL = "https://api.sandbox.lulu.com/"
TOKEN_ENDPOINT = SANDBOX_BASE_URL + "auth/realms/glasstree/protocol/openid-connect/token"

# url = 'https://api.sandbox.lulu.com/auth/realms/glasstree/protocol/openid-connect/token'
data = {"grant_type":"client_credentials"}
headers = {'Authorization':Base64}
post_response = requests.post(url=TOKEN_ENDPOINT, data=data, headers=headers)
post_json_data = post_response.json()
access_token = post_json_data['access_token']

Auth = f'Bearer {access_token}'
headers = {'Authorization':Auth, 'Content-Type':'application/json'}
TEST_ENDPOINT = SANDBOX_BASE_URL + "print-jobs/"  
get_response = requests.get(url=TEST_ENDPOINT, headers=headers)
get_json_data = get_response.json()
print(get_json_data)