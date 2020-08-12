jumin = "200314-2315031"

if (jumin[7] == 1):
    sex = "남자"
elif (jumin[7] == 2):
    sex = "여자"

print("성별 : " + sex)
print("연 : " + jumin[0:2])
print("월 : "+ jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("출생지역조합번호 : " + jumin[8:12])
print("출생지역의 같은 성씨 출생 신고순번 : " + jumin[12])
print("오류검증번호 : " + jumin[13])

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))  #띄어쓰기 포함
print(python.replace("Python", "Minecraft"))

index = python.index("n")
print(index)
index = python.index("n", index +1)
print(index)

print(python.find("Java"))  #있으면 0, 없으면 -1

#print(python.index("Python"))  #파이썬으로 하면 오류가 안나고 Java로하면 substring not found 오류가 뜸

print("hi")

print(python.count("n"))