import os
os.walk('.')
for current_dir, directories , files in os.walk('.'):
    print(f"Current directory is:{current_dir}")
    print(f"Thís directory have sub-dris:{directories}")
    print(f"Thís directory have files :{files}")
    print("--------")
os.path.getsize('buoi3.py')
print(os.path.getsize('buoi3.py'))