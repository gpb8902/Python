#jumin = "200314-2315031" # 주민번호가 200...로 지정된다.

#if (jumin[7] == 1): #만약 주민번호자리 7(컴퓨터상에서 순서(현실에선 8))이 1이면 남자로, 아니면 여자로 출력된다.
   # sex = "남자"
#elif (jumin[7] == 2):
    #sex = "여자"

#print("성별 : " + sex) # 성별 : sex(변수)로 출력된다.
#print("연 : " + jumin[0:2]) #0~1로 출력되는데 2라고 한 이유는 :으로 하면, 마지막에다가 1을 더해서 넣어야 0~1까지의 수로 출력되기 때문이다.
#print("월 : "+ jumin[2:4]) #2~3로 출력되는데 4라고 한 이유는 :으로 하면, 마지막에다가 1을 더해서 넣어야 2~3까지의 수로 출력되기 때문이다.
#print("일 : " + jumin[4:6]) #4~5로 출력되는데 6라고 한 이유는 :으로 하면, 마지막에다가 1을 더해서 넣어야 4~5까지의 수로 출력되기 때문이다.
#print("생년월일 : " + jumin[:6]) #0~5자리의 수를 출력한다.
#print("출생지역조합번호 : " + jumin[8:12]) #8~11로 출력되는데 12라고 한 이유는 :으로 하면, 마지막에다가 1을 더해서 넣어야 8~11까지의 수로 출력되기 때문이다.
#print("출생지역의 같은 성씨 출생 신고순번 : " + jumin[12]) #주민번호의 12번째자리를 출력한다.
#print("오류검증번호 : " + jumin[13]) #주민번호의 13번째자리를 출력한다.

python = "Python is Amazing" #python은 "Python is Amazing"으로 지정된다. 
print(python.lower()) #"Python is Amazing"이 소문자로 출력된다.
print(python.upper()) #"Python is Amazing"이 대문자로 출력된다.
print(python[0].isupper()) #"Python is Amazing"에서 0번째(현실에선 1번째)가 대문자인지 아닌지를 확인한다.(맞으면 True, 아니면 False로 나타낸다.)
print(len(python))  #"Python is Amazing"이 몇글자인지(띄어쓰기 포함) 알려준다.
print(python.replace("Python", "Minecraft")) #"Python is Amazing"에서 Python을 Minecraft로 바꾼다.

index = python.index("n") #"Python is Amazing"이라는 문장에서 n이 몇번째 자리에 있는지를 알려준다.
print(index) #5로 출력된다.
index = python.index("n", index +1) #또다른 n이 몇번째 자리에 있는지를 알려준다.
print(index) #15로 출력된다.

print(python.find("Java"))  #있으면 0, 없으면 -1

#print(python.index("Python"))  #파이썬으로 하면 오류가 안나고 Java로하면 substring not found 오류가 뜸

print(python.count("n")) #"Python is Amazing"에서 n이 몇개 있는지를 알려준다.