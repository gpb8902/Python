def profile(name, age, job, country, language, school):
    print("이름 : {0}\t 나이 : {1}\t 직업 : {2}\t 국적 : {3}\t 이용 가능 언어 : {4}\t학교경력 : {5}".format(name, age, job, country, language, school))
profile("박정환", 26, "유튜버", "한국", "한국어, 영어, 스페인어, 포르투갈어, 프랑스어", "광주 월봉초, 광주 봉산중, 광주 숭덕고, SKY, 하버드, 옥스포드")
profile("Muchim Doraji", 22, "배우", "아랍 에메리트", "아랍어", "아랍초, 아랍중, 아랍고, 아랍대, 토론토대")

def profile(name, age, *language):
    print("이름 : {0}\t 나이 : {1}\t ". format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
        print()

profile("Nochi", 36, "English, French, Spanish")
profile("Jeb", 39, "English, French, Spanish, Korean, Chinese, Arab")