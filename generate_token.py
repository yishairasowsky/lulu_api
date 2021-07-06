# Attempt to implement this https://api.lulu.com/docs/#section/Getting-Started/Generate-a-Token
# For help use
#  https://github.com/minireference/lulu-api-client/blob/358395d21685245f75a60094c2f7d80b6b3dddb1/luluapi.py#L67
import requests
import datetime
from private_info import Base64 # obtained from https://api.sandbox.lulu.com/user-profile/api-keys

SANDBOX_BASE_URL = "https://api.sandbox.lulu.com/"
TOKEN_ENDPOINT = SANDBOX_BASE_URL + "auth/realms/glasstree/protocol/openid-connect/token"

# url = 'https://api.sandbox.lulu.com/auth/realms/glasstree/protocol/openid-connect/token'
data = {"grant_type":"client_credentials"}
headers = {'Authorization':Base64}
post_response = requests.post(url=TOKEN_ENDPOINT, data=data, headers=headers)
post_json_data = post_response.json()

access_token = post_json_data['access_token'] # https://api.lulu.com/docs/#:~:text=that%20contains%20an-,access_token,-key%3A
Auth = f'Bearer {access_token}'

headers = {'Authorization':Auth, 'Content-Type':'application/json'}
TEST_ENDPOINT = SANDBOX_BASE_URL + "print-jobs/"  
get_response = requests.get(url=TEST_ENDPOINT, headers=headers)
get_json_data = get_response.json()
print(get_json_data)

book = {
   "external_id": "test-line-item",
   "title": "My Book",
   "cover_source_url": "<online URL where to get the PDF of book's one-piece cover>",
   "interior_source_url": "<online URL where to get the PDF of interior>",
   "pod_package_id": "0550X0850BWSTDPB060UW444GXX",
   "quantity": 1,
}
external_id = "printjob-" + datetime.now().strftime("%Y%m%d__%H%M")
books = [book]
# Prepare line items from book order info in `books` list
line_items = []
for book in books:
    if "external_id" in book:
        item_external_id = book["external_id"]
    else:
        item_external_id = "item-" + datetime.now().strftime("%Y%m%d__%H%M")
    line_item = {
        "external_id": item_external_id,
        "printable_normalization": {
            "cover": { "source_url": book["cover_source_url"] },
            "interior": { "source_url": book["interior_source_url"] },
            "pod_package_id": book["pod_package_id"],
        },
        "quantity": book["quantity"],
        "title": book["title"],
    }
    line_items.append(line_item)

# POST data
address = '32/1 Kaf hachaim street'
data = {
    "contact_email": 'myname@somesite.com',
    "external_id": external_id,
    "line_items": line_items,
    "production_delay": 30,
    "shipping_address": address, # continue here https://github.com/minireference/lulu-api-client/blob/358395d21685245f75a60094c2f7d80b6b3dddb1/luluapi.py#:~:text=self%2C%20address%2C%20books-,%2C,-shipping_level%2C%20external_id%3DNone
    "shipping_level": shipping_level,
}
headers = self.get_headers()
response = requests.post(PRINTJOBS_ENDPOINT, json=data, headers=headers)
response_data = response.json()
