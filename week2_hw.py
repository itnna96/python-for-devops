import os
file_name = "sample.txt"
current_dir=os.getcwd()
file_path = os.path.join(current_dir,file_name)

"""
- Open file A ,read mode
- Open file A_temp, write mode
- close file A_temp ,A
- Check A_temp: compare length # file size or sum
- If OK -> delete A ,rename A_tmp -> A
"""

with open(file_path,'r') as file:
    lines = file.readlines()

tempfile_name = file_name + "temp"
tempfile_path = os.path.join(current_dir,tempfile_name)
with open (tempfile_path,'w') as open_file:
    for line in lines: # line = "line 1\n"
        if line[0] == "T":
            print(line[0])
            line += "1: T"
            #line = line 
     #print(lines)