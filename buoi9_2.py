#!/usr/bin/env python3
#regexr.com

import re

log='66.249.65.158 - - [05/Oct/2022:19:10:38 +0600] "GET /sample HTTP/1.1" 404 177 "https://example.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"'

request = re.search(r'\"\s(\d+)\s(\d+)\s\"',log).group(1) 
# request = re.search(r'\"\s(?P<status>\d+)\s(?P<size>\d+)\s\"',log) 
# hoặc sử dụng cách trên có thể request.group('status') or request.group('size')
ip = re.search(r'\d+\.\d+\.+\d+\.\d+',log).group(0)
print(ip)
print(request)