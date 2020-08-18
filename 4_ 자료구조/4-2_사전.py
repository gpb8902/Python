cabinet = {3:"유재석", 100: "양세찬"} #cabinet 3:"유재석", 100:"양세찬"으로 지정된다.
#print(cabinet[3]) #유재석이 출력된다.
#print(cabinet[100]) #양세찬이 출력된다.

#print(cabinet.get(3)) #유재석이 출력된다.
#print(cabinet[5]) #cabinet중에 없는 값
print(cabinet.get(5, "사용가능")) #사용가능이라고 출력된다.
print("hi") #hi라고 출력된다.

print(3 in cabinet) # True로 출력된다
print(5 in cabinet) # False로 출력된다.


cabinet = {"A-3": "유재석", "B-100": "양세찬"} #A-3: 유재석, B-100:양세찬으로 지정된다.
print(cabinet["A-3"]) #유재석 으로 출력된다
print(cabinet["B-100"]) #양세찬으로 출력된다.
 
print(cabinet) #지금 cabinet
cabinet["A-3"] = "김종국" #A-3이 유재석에서 김종국으로 바뀐다.
cabinet["C-20"] = "차도권" #C-20이 차도권으로 지정된다.
print(cabinet) #김종국, 양세찬, 차도권으로 출력된다.

del cabinet["A-3"] #cabinet에 있는 A-3을 지운다.
print(cabinet) #양세찬, 차도권으로 출력된다.
print(cabinet.keys()) #key인 B-100, C-20이 출력된다.

print(cabinet.values()) #value인 양세찬, 차도권이 출력된다.

print(cabinet.items()) #쌍으로 출력

cabinet.clear()#cabinet에 있는 값 전체 제거
print(cabinet) #아무것도 없이 출력