import os ,requests
from json.decoder import JSONDecodeError
import time

BASE_URL = "htpps://maps.googleapis.com/"
GOOGLE_API_KEY = "jdqwkdjqwkldqw-djijdi2jdi2"
#Thông thường sẽ sử dụng biến môi trương export GOOGLE_API_KEY = "jdqwkdjqwkldqw-djijdi2jdi2" không nên ghi KEY vào trực tiếp file tránh lộ KEY
#GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

if not GOOGLE_API_KEY:
    print('There is not google api key.')
    exit(1)
my_url = BASE_URL + 'maps/api/place/nearbysearch/json'
while True:
    from time import sleep
    sleep(5)
    #Cu 5s vong lap chay lai 1 lan
    query = {
        'location': '10.7853351,106.5701181,14.87',
        'keyword': 'tel4vn',
        'radius': '15000',
        'key': GOOGLE_API_KEY
    }

    start_time = time.time()
    response = requests.get(my_url,params=query)
    response_time = round(time.time() - start_time,3)
    if response.status_code == 200 and response_time < 2:
        print(response_time)
        continue
    print('not oke')



# place_id = response.json()['results'][0]['place_id']
# # print(response.status_code) # 1xx-5xx

# detail_url = BASE_URL+ 'maps/api/place/details/json'
# parameters = {
#     'place_id': place_id,
#     'key': GOOGLE_API_KEY,
#     'fields': 'formatted_address,name' #chon thong tin can lay
# }
# response = requests.get(detail_url,params=parameters)
# print(response.status_code)
# print(response.json)

