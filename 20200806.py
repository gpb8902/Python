print("백문이 불여일견\n백견이 불여일타")   # \n -> 다음줄(엔터)

print("저는 \"李登鉼(이등병)\" 입니다.") #따옴표 표시

print("C:\\Users\\Nadocoding\\Destop\\PythonWorkspace>")    # \\ -> \ 로 표시됨

print("Red apple\rPine") #첫번째 단어가 \r 다음에 있는 단어로 바뀜

print("Redd\bapple")    #마지막 글자를 \r 다음에 있는 글자로 바꿈

print("Red\tApple"8)9 #탭 한번
 
url = "http://naver.com"    #URL이라는 변수에 네이버 사이트 주소를 지정함
my_str = url.replace("http://","")  #http:// 를 ""안에 있는 문자로 변경(지움)
#print(my_str)
my_str = my_str[:my_str.index(".")] #. 뒤에 있는걸 삭제
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀 번호는 {1}입니다.".format(url, password))