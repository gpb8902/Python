#import glob
#print(glob.glob("*.py"))

#import os
#print(os.getcwd())

#folder = "ICE_dir"

#if os.path.exists(folder):
#    print("이미 존재하는 폴더 입니다.")
#    os.rmdir(folder)
#    print(folder, "폴더를 삭제했습니다.")

#else:
#    os.makedirs(folder)
#    print(folder, "폴더를 생성하였습니다.")
#print(os.listdir())

#import time
#print(time.localtime())
#print(time.strftime("   %Y - %m - %d\n     %H : &M : &S"))

import datetime
#print("오늘 날짜는", datetime.date.today())

today = datetime.date.today()
td =  datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td)