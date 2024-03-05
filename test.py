import os
current_dir = os.getcwd()
print(current_dir)
os.path.dirname(current_dir)
os.path.basename(current_dir)
print(os.path.dirname(current_dir))
print(os.path.basename(current_dir))

file_name = "sample.txt"
hihi = os.path.join(current_dir,"sample.txt")
print(len(hihi)) 
#54 cung cấp độ dài của chuỗi đường dẫn file (bao gồm dấu phân cách)
print(type(hihi))
#print(os.path.getsize(hihi))
with open(hihi,'r') as open_file:
    text=open_file.read()
    print(len(text))
    print(text)
    #cung cấp số lượng ký tự trong nội dung file
    print(type(text))

print(os.path.getsize(hihi))    