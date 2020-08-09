cabinet = {3:"유재석", 100: "양세찬"}
#print(cabinet[3])
#print(cabinet[100])

#print(cabinet.get(3))
#print(cabinet[5])
print(cabinet.get(5, "사용가능"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False


cabinet = {"A-3": "유재석", "B-100": "양세찬"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "차도권"
print(cabinet)

del cabinet["A-3"]
print(cabinet)
print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)

#-----------------불리언---------------------------------------------------------------------------

banana = 7 #banana라는 변수가 7이랑 같다. 

print(5<10)#10은 5보다 크므로 True 라고 출력된다.
print(5>10)#5는 10보다 작은데 여기선 크다고 나와있어 False로 출력된다.

print("크림이" == "크림이")#==은 같다라는 뜻이고 크림이 == 크림이는 참이므로 True가 출력된다.

print(banana == 7)#변수는 따옴표를 붙이지 않고, banana라는 변수는 7과 같기 때문에 True라고 출력된다.