"""
Giving url = "https://tel4vn.edu.vn/course/python-for-devops/"
Split the string to get:
The protocol "https"
3 parts of domain ["tel4vn", "edu", "vn"]
2 parts of path ["course", "python-for-devops"]
"""
url = "https://tel4vn.edu.vn/course/python-for-devops/"
protocol = url.split(":")
print(f"The protocol '{protocol[0]}'")
a = protocol[1].split("/")
domain = a[2].split(".")
print(f"3 parts of domain :{domain}")
print(f"2 parts of path :{a[3:5]}")


# protocol = url.split("://")[0]

# domain_path = url.split("://")[1]

# domain = domain_path.split('/')[0]

# domain_parts = domain.split('.')

# paths = domain_path.split('/')[1:] # slice from 1 to end
# if not paths[-1]: #if empty
#     paths.pop()
# print(protocol)
# print(domain_parts)
# print(paths)