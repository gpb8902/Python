from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")

sentence = '나는 내일 전역하는 개꿀빤 입대한지 7일된 이등병, 李燈昞(오얏나무처럼 크고 등잔처럼 밝아라 라는 뜻의 이등병) 입니다.'
print(sentence)
sentence2 = "니넨 전역까지 몇일 남았냐~~~? ㅋㅋㅋ"
print(sentence2)
sentence3 = """
고구마호박이 아니라,
호박고구마에요
"""
print(sentence3)

jumin = "000000-111111"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : "+ jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("출생지혁조합번호 : " + jumin[8:12])
print("출생지역의 같은 성씨 출생 신고순번 : " + jumin[12])
print("오류검증번호 : " + jumin[13])

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Minecraft"))

index = python.index("n")
print(index)
index = python.index("n", index +1)
print(index)

print(python.find("Java"))
#print(pythonindex("Java"))
print("hi")

print(python.count("n"))