#!/usr/bin/env python3
#regexr.com

import re
email_list= """
ngocanh123@gmail.com
ngoc.anh.nguyen@gmail.com
nguyen ngoc anh@gmail.com
minhanh@gmail
ngocanh@outlook.com
anhnguyen@tel4vn.edu.vn
anhnguyen@tel4vn.edu.org
"""

# match= re.search(r'(\w|\.)+@\w+\.\w+(\.\w+)*',email_list)
# if not match:
#     print("No valid email in string.")
# else:
#     print("There is at least 1 valid email")


match= re.search(r'(\w+)@(\w+)\.(\w+)',email_list)
if not match:
    print("No valid email in string.")
else:
    username = match.group(1)
# print(match)

"""
\w word
\w+ nhiều từ với số
\s dấu space
(\.\w+)* có thể có hoặc không
\d+: Ký tự đặc biệt
\d: số
"""