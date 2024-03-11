import subprocess
subprocess.run(['ls','-l'])

# # output=subprocess.run(['ls','-l'],capture_output=True)
# output = subprocess.run(['ls', 'non-exist-file'], capture_output=True)
# # print(output)
# print(f"Return code: {output.returncode}")
"""
Lỗi cú pháp:
Python: returncode 2
Bash: returncode 1
Lỗi hệ thống:
Python: returncode 3
Bash: returncode 127

"""
# print(f"Output: {output.stdout.decode()}")
# print(f"Error: {output.stderr.decode()}")

output = subprocess.run(
['ls', 'non-exist-file'],
capture_output=True,
text=True,
check=True
)
print(output)
print(f"Output: {output.stdout}")