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