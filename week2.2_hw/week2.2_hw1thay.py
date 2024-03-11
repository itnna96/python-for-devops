import os
file_name = 'sample.log'
cwd = os.getcwd()
file_path = os.path.join(cwd,file_name)

with open(file_path,'r') as data:
    text = data.read()
    lines = text.split('\n')

ips = []
http_codes = []
total_success = 0
total_fail = 0

for line in lines:
    if not line: # if line is empty
        continue
    after_request = line.split('"')[2]
    # print(after_request)
    http_code = int(after_request.split()[0])
    http_codes.append(http_code)
    ip = line.split()[0]
    # print(ip)
    ips.append(ip)

    if http_code >= 200 and http_code <= 399:
        total_success += 1
    elif http_code >= 400 and http_code <= 599:
        total_fail += 1
# print(ip)

# print("Total sucess", total_success)
# print("Total sucess", total_fail)

ips_fails = []
i = 0
#print(range(len(ips))) #range(0,11)
for i in range(len(ips)):
    exist = False
    # print(http_codes[i])
    # print(http_codes)
    if http_codes[i] > 499 or http_codes[i] <400:
        continue

    for _ip, _num in ips_fails:
        # print(f"_ip :{_ip}")
        if _ip == ips[i]:
            #_num += 1 Sai
            ips_fails.remove((_ip,_num))
            ips_fails.append((_ip,_num +1 ))
            exist = True

    if exist == False: 
    #    print(f"ips {ips[i]}")
       ips_fails.append((ips[i],1))
print(ips_fails)

max = 0
ans = ''

for _ip, _num in ips_fails:
    if _num > max:
        ans = _ip
        max = _num
print(f"{ans} is the most 4xx fails")