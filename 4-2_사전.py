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

