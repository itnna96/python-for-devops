import os
#os.walk('./buoi3')
def path_walk(parent_path):
    for current_dir,_,files in os.walk(parent_path):   
        print(f"I am at:{current_dir}:")
        for file_name in files:
            file_path = os.path.join(current_dir,file_name)
            #print (file_path)
            size = os.path.getsize(file_path)
            print(f"File:{files} - Size:{size}B")

path_walk('./buoi3')

# text1=os.path.dirname(current_dir)
# text2=os.path.basename(current_dir)
# print(text1)