#!/usr/bin/env python3
import os, argparse ,json ,requests

BASE_URL = "https://api.github.com"
API_KEY = os.environ.get('GITHUB_API_KEY')

if not API_KEY:
    print("Please provide GITHUB_API_KEY")
    exit(1)

list_branches = BASE_URL + "/repos/itnna96/toya_week04/branches/feature/abc/rename"
#/repos/{owner}/{repo}/branches/{branch}/rename
headers = {
    #Authorization: Bearer <YOUR-TOKEN>" 
    "Authorization": "Bearer " + API_KEY
}

payload ={
    "new_name":"feature/xyz"
}

response = requests.post(list_branches,headers=headers, json=payload)
if response.status_code == 201:
    print(response.text)
# response = requests.get(list_branches,headers=headers)
# print(response.status_code)
# print(response.text)

