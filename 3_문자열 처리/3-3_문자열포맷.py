print("I'm a Korean, and I can speak %d of languages like Spanish, Korean, Arab, Chinese, English, and Portuguese, Bengal , French, German, Maori, Mongolian, Russian, Turkish, and Vietnamese." % 50) #%d는 정수에 쓰인다. ...speak %d of...에서 %d = 50이므로 ...speak 50 of.. 로 출력된다.
print("And I study them %s" % "myself") #문자열 할때 %s
print("My favorite game is %s" %"Minecraft") #1글자 문자열 할때 %c
print("Apple 은 %c로 시작해요" % "A") #1글자 문자열 할때 %c
print("España empieza con una %c" %"E") #1글자 문자열 할때 %c
print("나는 {}살 입니다.".format(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)) # format뒤에 있는 문자열, 정수가 {}안으로 출력한다.    
print("저는 %s색과 %s색을 좋아해요." %("파란", "다이아몬드")) #두개 이상은 뒤에 ()를 쳐서 "a", "b"로 친다.
print("나는 {}와 {}과목을 좋아해요.".format("영어", "수학")) #순서대로 출력된다.
print("나는 {0}와 {1}과목을 좋아해요.".format("영어", "수학")) #순서대로 출력된다.
print("나는 {1}과 {0}과목을 좋아해요.".format("영어", "수학")) #순서가 바뀐 상태로 출력된다.

print("나는 {age}살이며, {game}와 {game1}를 좋아합니다.".format (age = 5435, game = 1, game1 = 2)) #뒤에 age라는 변수가 5435, game이라는 변수가 1, game1이라는 변수가 2로 지정된 상태로 출력된다.
#print("나는 {age}살이며, {color}색을 좋아해요."format(color="빨간", age=20)) #"(==같다)
#print("나는 {age}살이며, {game1}와 {game2}를 좋아해요.".format(age = 14, game1="마인크래프트", game2="카트라이더")) #"

print("나는 %d살 입니다." % 15)    #정수 할때 %d 
game = "마인크래프트" #
print("나는 %s를 좋아해요." % game) #문자열 할때 %s
print("나는 %c 로 시작해요" % "나") #1글자 문자열 할때 %c

print("나는 %s와 %s를 배우고 싶다. 왜냐하면 많은 나라에서 그 언어들을 많이 쓰기 때문이다." % ("스페인어",  "포르투갈어")) #"(두개 이상은 뒤에 ()를 쳐서 "a", "b"로 친다.)

print("나는 {0}와 {1}를 배우고 싶다. 왜냐하면 많은 나라에서 그 언어들을 많이 쓰기 때문이다.".format ("스페인어",  "포르투갈어")) #순서대로 출력된다.
print("나는 {1}와 {0}를 배우고 싶다. 왜냐하면 많은 나라에서 그 언어들을 많이 쓰기 때문이다.".format ("스페인어",  "포르투갈어")) #순서가 바뀐 상태로 출력된다.
print("나는 {age}살이고, {language1}와 {language2}를 배우고 싶어해요.".format(age = 13, language1 = "스페인어", language2 = "포르투갈어")) #뒤에 age라는 변수가 13, language 라는 변수가 "스페인어", language2라는 변수가 "포르투갈어로 지정된 상태로 출력된다.
#아래는 파이썬 버전 3.6부터 가능
age = 13 #age라는 변수가 13으로 지정된다.
language1 = "스페인어" #language1라는 변수가 "스페인어"가 된다.
language2 = "포르투갈어" #language2라는 변수가 "포르투갈어"가 된다.

print(f"나는 {age}살이고, {language1}랑 {language2}를 배우고 싶어해요") #"나는 13살이고, 스페인어랑 포르투갈어를..."이 출력된다.