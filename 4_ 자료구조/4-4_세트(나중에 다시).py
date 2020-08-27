#---------------------------------------------------------------------집합 (set)-------------------------------------------------------------------------------
#중복 안됨, 순서 없음
my_set = {1,2, 3, 3, 3} #my_set이 1,2,3,3,3으로 지정된다.
print(my_set) #1,2,3이 출력된다.

java = {"유재석", "양세형", "하도권", "하하"} #java가 유재석, 양세형, 하도권, 하하로 지정된다
python = set(["유재석", "김종국"]) #python이 유재석, 김종국이로 지정된다

#Java, Python을 모두 할 수 있는 개발자
print(java & python) #유재석이 출력된다
print(java.intersection(python)) #유재석이 출력된다.

print(java | python) #java, python이 같이 출력된다.(|는 \키와 Shift키를 동시에 누르면 나온다)
print(java.union(python)) ##java, python이 같이 출력된다
 
print(java - python) #java에서 python을 뺀다(java랑 겹치는 사람만 뺌)
print(java.difference(python)) #
print(python - java) #
print(python.difference(java)) #

python.add("양세형", "하하") #
print(python) #

java.remove("하하") #
print(java) #