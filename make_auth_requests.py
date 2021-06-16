import requests

url = 'https://api.lulu.com/'

access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkI'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
    }

x = requests.post(url=url, headers=headers)

print(x)