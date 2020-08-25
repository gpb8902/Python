#---------------------------------------------------------------------집합 (set)-------------------------------------------------------------------------------
#중복 안됨, 순서 없음
my_set = {1,2, 3, 3, 3}
print(my_set)

java = {"유재석", "양세형", "하도권", "하하"}
python = set(["유재석", "김종국"])

#Java, Python을 모두 할 수 있는 개발자
print(java & python)
print(java.intersection(python))

print(java | python)
print(java.union(python))

print(java - python)
print(java.difference(python))
print(python - java)
print(python.difference(java))

python.add("양세형", "하하")
print(python)

java.remove("하하")
print(java)