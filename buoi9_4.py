import requests,time

start_time = time.time()
response = requests.get('https://www.google.com/')
response_time = round(time.time()-start_time,3)
print(f'Response: {response_time}ms')