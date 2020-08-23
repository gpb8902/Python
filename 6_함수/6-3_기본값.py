#def profile(name, age, main_lang):
#    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" \
#    .format(name, age, main_lang))

#profile("Muchim Doraji", 26, "영어, 스페인어, 프랑스어, 한국어")
#profile("Muchim Gaji", 25, "아랍어, 벵골어, 헝가리어, 러시아어")

def profile(name, age=14, classnum=2, todaysubject="정보, 기술, 수학B, 영어A, 국어A, 동아리, 동아리"):
    print("이름: {0}\t나이 : {1}\t반 : {2}\t오늘수업 : {3}" \
    .format(name, age, classnum, todaysubject))


profile("Muchim Doraji")
profile("Muchim Gaji")