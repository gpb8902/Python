#def profile(name, age, main_lang): #profile(name, age, main_lang)라는 함수가 생성된다.
#    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" \ #이름, 나이, 주 사용언어가 출력되고 \는 탈출문자다
#    .format(name, age, main_lang))

#profile("Muchim Doraji", 26, "영어, 스페인어, 프랑스어, 한국어") #profile이 Muchim Doraji", 26, "영어, 스페인어, 프랑스어, 한국어로 지정된다.
#profile("Muchim Gaji", 25, "아랍어, 벵골어, 헝가리어, 러시아어") #profile이 Muchim Gaji", 25, "아랍어, 벵골어, 헝가리어, 러시아어로 지정된다.

def profile(name, age=14, classnum=2, todaysubject="정보, 기술, 수학B, 영어A, 국어A, 동아리, 동아리"): #age가 14, classnum이 2, todaysubject가 정보, 기술, 수학B...로 지정되낟.
    print("이름: {0}\t나이 : {1}\t반 : {2}\t오늘수업 : {3}" \
    .format(name, age, classnum, todaysubject)) #이름, 나이, 반 오늘수업이 출력된다.


profile("Muchim Doraji") #1번이 이름:Muchim Doraji, 나이 :14 반 :2 오늘수업 : 정보, 기술, 수학B, 영어A, 국어A, 동아리, 동아리가 된다.
profile("Muchim Gaji") #2번이 이름:Muchim Gaji, 나이 :14 반 :2 오늘수업 : 정보, 기술, 수학B, 영어A, 국어A, 동아리, 동아리가 된다.