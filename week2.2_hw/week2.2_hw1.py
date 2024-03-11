"""
Given a nginx “sample.log” files (on classroom assignment)
Log format is:
<ip> - - <date-time> <request> <http code> <body size> <host> <user-agent>
Write a python function to read from this log file and print out this
information:
- Total of success (2xx) and failed (4xx, 5xx) requests.
- Output the client ip that has the most 4xx requests.
"""

import os
file_name = "sample.log"
current_dir = os.getcwd()
file_path = os.path.join(current_dir,file_name)

success_count = 0
failed_count = 0

with open(file_path,'r') as file:
    lines = file.readlines()


# tempfile_name = file_name + "temp"
# tempfile_path = os.path.join(current_dir,tempfile_name)
# with open (tempfile_path,'w') as open_file:
    for line in lines:
        parts = line.split(" ")
        print(parts[8:9])
        for i in parts[8:9]:
            # print(i)
            if 300 >= int(i) >= 200:
                success_count += 1
            else:
                failed_count += 1
        
print(f"Total of success with code 2xx: {success_count}")
print(f"Total of failed with code 4xx,5xx: {failed_count}")