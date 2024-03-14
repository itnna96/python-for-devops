#!usr/bin/env python

import requests
from json.decoder import JSONDecodeError
BASE_URL = "https://api.upcitemdb.com/"

url = BASE_URL + 'pro/trial/lookup'
parameters = {
    'upc': '190199267992'
}
response = requests.get(url,params=parameters)
print(response.status_code) # 1xx-5xx
try:
    data = response.json()
    print(data)
except JSONDecodeError as e:
    print("Respone message cant be parsed to json.")
# if response.status_code == 200:
#     # data = json.loads(response.text)
#     data = response.json() # data duoi dang dictionary
#     print(data['items'][0]['title'])