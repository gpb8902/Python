#import glob
#print(glob.glob("*.py"))

#import os
#print(os.getcwd())

folder = "ICE_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더 입니다.")

else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")