"""
Given a template text file “template.txt” (on classroom assignment)
Ask user to input:
- Name
- A place
- An action
Replace inputs in the template file with NAME, PLACE and ACTION. Then
write the output to a text file “output.txt”
Example:
template.txt:
NAME walkes to the PLACE and then he VERB.
NAME asks another person to VERB too.
"""

file_name = "template.txt"
out_put = "output.txt"
name = input("Pl input a name : ")
place = input("Pl input a place : ")
verb = input("Pl input a verb : ")

output_file = open(out_put , 'w')
with open (file_name,'r') as open_file:
    lines = open_file.readlines()
    for line in lines:
        data = line.replace("NAME", name).replace("PLACE", place).replace("VERB", verb)
        output_file.write(data)
output_file.close()
# with open(file_name) as open_file:
#     data = open_file.read()
#     data = data.replace("NAME", name).replace("PLACE", place).replace("VERB", verb)
#     # data.replace("NAME",name).replace("PLACE",place).replace("VERB",verb)
#     print(data)

# with open(out_put,'w') as op:
#     op.write(data)

print("Done !")
# with open(file_path,'r') as file:
#     lines = file.readlines()

# tempfile_name = file_name + "temp"
# tempfile_path = os.path.join(current_dir,tempfile_name)

# with open (tempfile_path,'w') as open_file:
#     for line in lines:
#         parts = line.split(" ")
#         if parts[0] == "NAME":
#             parts.pop(0)
#             parts.insert(0,input())
#     print(parts)

