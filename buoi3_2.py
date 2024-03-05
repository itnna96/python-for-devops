# Open file voi with để khỏi cần close khi thêm nội dung vào file
# với r,w,r+,w+,a+.
import os
file_name = "sample.txt"
current_dir = os.getcwd()
file_path = os.path.join(current_dir, file_name)

with open(file_path,'r') as open_file:
    text = open_file.read()
    print(f"File has {len(text)} chars. And here is the content:")
    print(text)