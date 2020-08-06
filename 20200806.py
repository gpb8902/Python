print("백문이 불여일견\n백견이 불여일타")

print("저는 \"李登鉼(이등병)\" 입니다.")

print("C:\\Users\\Nadocoding\\Destop\\PythonWorkspace>")

print("Red apple\rPine")

print("Redd\bapple")

print("Red\tApple")

url = "http://naver.com"
my_str = url.replace("http://","")
#print(my_str)
my_str = my_str[:my_str.index(".")] 
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀 번호는 {1}입니다.".format(url, password))