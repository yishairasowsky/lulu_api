# Attempt to implement this https://api.lulu.com/docs/#section/Getting-Started/Generate-a-Token
# For help use https://github.com/minireference/lulu-api-client/blob/358395d21685245f75a60094c2f7d80b6b3dddb1/luluapi.py#L67

import requests
from cost_calc import cost_payload
from order_data import order_json 
from constants import headers, PRINTJOBS_ENDPOINT, COST_CALC_URL
from generate_token import Authorization

headers["Authorization"] = Authorization

def show_print_jobs(PRINTJOBS_ENDPOINT, headers):
    response = requests.get(PRINTJOBS_ENDPOINT, headers=headers)
    print_jobs_json = response.json()
    print("print_jobs_json")
    print(print_jobs_json)

def add_print_job(PRINTJOBS_ENDPOINT, order_json, headers):
    response = requests.post(PRINTJOBS_ENDPOINT, json=order_json, headers=headers)
    add_print_job_json = response.json()
    print("add_print_job_json")
    print(add_print_job_json)

def cost_calc(COST_CALC_URL, cost_payload, headers):
    response = requests.post(COST_CALC_URL, data=cost_payload, headers=headers)
    cost_calc_json = response.json()
    print("cost_calc_json")
    print(cost_calc_json)

show_print_jobs(PRINTJOBS_ENDPOINT,headers)
add_print_job(PRINTJOBS_ENDPOINT, order_json, headers)
show_print_jobs(PRINTJOBS_ENDPOINT,headers)
cost_calc(COST_CALC_URL, cost_payload, headers)
