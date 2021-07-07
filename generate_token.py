# Attempt to implement this https://api.lulu.com/docs/#section/Getting-Started/Generate-a-Token
# For help use
#  https://github.com/minireference/lulu-api-client/blob/358395d21685245f75a60094c2f7d80b6b3dddb1/luluapi.py#L67
import requests
from cost_calc import cost_payload
from datetime import datetime
from private_info import Base64 # obtained from https://api.sandbox.lulu.com/user-profile/api-keys
from order_data import order_json 

# Define CONSTANT variables
SANDBOX_BASE_URL = "https://api.sandbox.lulu.com"
data = {"grant_type":"client_credentials"}
headers = {'Authorization':Base64}

# Generate token
TOKEN_ENDPOINT = SANDBOX_BASE_URL + "/auth/realms/glasstree/protocol/openid-connect/token"
response = requests.post(url=TOKEN_ENDPOINT, data=data, headers=headers)
access_json = response.json()
access_token = access_json['access_token'] # https://api.lulu.com/docs/#:~:text=that%20contains%20an-,access_token,-key%3A

# Make authenticated requests
Authorization = f'Bearer {access_token}'
print('Authorization')
print(Authorization)

# headers["Content-Type"] = "application/json" # Seems unnecessary despite https://api.lulu.com/docs/#:~:text=Bearer%20%7Baccess_token%7D%27%20%5C%0A%20%20-H%20%27-,Content,--Type%3A%20application/json
headers["Authorization"] = Authorization

# Get print jobs
PRINTJOBS_ENDPOINT = SANDBOX_BASE_URL + "/print-jobs"
response = requests.get(PRINTJOBS_ENDPOINT, headers=headers)
print_jobs_json = response.json()
print("print_jobs_json")
print(print_jobs_json)

# Add print job
response = requests.post(PRINTJOBS_ENDPOINT, json=order_json, headers=headers)
add_print_job_json = response.json()
print("add_print_job_json")
print(add_print_job_json)

# Get print jobs
response = requests.get(PRINTJOBS_ENDPOINT, data=data, headers=headers)
print_jobs_json = response.json()
print("print_jobs_json")
print(print_jobs_json)

COST_CALC_URL = SANDBOX_BASE_URL + "/print-job-cost-calculations/"
headers["Cache-Control"] = 'no-cache'

response = requests.post(COST_CALC_URL, data=cost_payload, headers=headers)

print(response.text)

pass