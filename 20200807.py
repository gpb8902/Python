#subway1 = 15
#subway2 = 25
#subway3 = 35

subway = [15, 25, 35]
print(subway)

subway = ["유재석", "김종국", "양세찬"]
print(subway)

print(subway.index("유재석"))

subway.append("하하")

print(subway)

subway.insert(2, "송지효")
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석")
subway.append("유재석")
subway.append("유재석")

print(subway.count("유재석"))

num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

mix_list = ["김종국", 40, True]
print(mix_list)

num_list.extend(mix_list)
print(num_list)

#-----------------------문자열 자료형----------------------------------------------------------------

print('풍선') #'풍선'이라고 출력된다. 하지만, '풍선'에서 ''<=이것
#은 생략된 채로 출력된다.

print(132) #'132'라고 출력됨, 하지만 1,2,0,3...와 같은 정수를 출력할 때 큰 따옴표나 작은 따옴표는 생략한다.

print("12" + "12")
#1212라고 출력된다.
a = 2 #변수로 ex: print(a *(곱하기임)3)을 출력하면 6으로 출력된다.
print(a*3)