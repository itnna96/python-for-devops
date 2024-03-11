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

counter = 0
line_number = 1
tempfile_name = file_name + "temp"
tempfile_path = os.path.join(current_dir,tempfile_name)
if not lines:
    print (f"File '{file_name}' is empty.")
    #print("File '{}' is empty.".format(file_name))
with open (tempfile_path,'w') as open_file:
    for line in lines: # line = "line 1\n"
        if line.strip(): # Check for empty lines (including those with whitespace)
        #if len(line[0]) != "": # có thể dùng cho mọi trường hợp 
        # có thể dùng if line.startswith("T") kiểm tra chữ cái đầu tiên
            print(line[0])
            line = f"{line_number}: {line}"
            line_number += 1
        open_file.write(line)
        counter += len(line)

if counter != 0:
    if counter == os.path.getsize(tempfile_path):
        print("File write success !")
        os.remove(file_path)
        os.rename(tempfile_path,file_path)
        print(file_path,file_name)
"""
file_path được tạo dựa trên file_name ban đầu.
Sau khi đổi tên, tempfile_path mới trỏ đến file mới.
Cập nhật file_path giúp đảm bảo nó trỏ đến file chính xác sau thao tác đổi tên.

Biến file_name giữ nguyên giá trị sau khi đổi tên vẫn là "sample.txt"
Cần cập nhật file_path nếu muốn nó trỏ đến file mới.
Việc cập nhật file_path đảm bảo tính chính xác và truy cập file dễ  dàng hơn.
"""