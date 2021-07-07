from private_info import Base64 # obtained from https://api.sandbox.lulu.com/user-profile/api-keys

# Define CONSTANT variables
SANDBOX_BASE_URL = "https://api.sandbox.lulu.com"
PRINTJOBS_ENDPOINT = SANDBOX_BASE_URL + "/print-jobs"
COST_CALC_URL = SANDBOX_BASE_URL + "/print-job-cost-calculations/"
data = {"grant_type":"client_credentials"}
headers = {'Authorization':Base64}

