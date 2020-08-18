#subway1 = 15 #subway1에 15명이 있다.
#subway2 = 25 #subway2에 25명이 있다.
#subway3 = 35 #subway3에 35명이 있다.

subway = [15, 25, 35] #subway가 15, 25,35로 지정된다.
print(subway) #15 , 25, 35가 출력된다.

subway = ["유재석", "김종국", "양세찬"] #subway가 유재석, 김종국, 양세찬으로 지정된다.
print(subway) #유재석, 김종국, 양세찬이 출력된다.

print(subway.index("유재석")) #유재석이 몇번째 칸에 탔는지를 알려줌

subway.append("하하") #맨 뒤에 하하를 추가함

print(subway) #유재석, 김종국, 양세찬, 하하가 출력된다.

subway.insert(2, "송지효") #김종국과 양세찬 사이에 송지효를 추가함
print(subway) #유재석, 김종국, 송지효, 양세찬 하하가 출력된다.

print(subway.pop()) #하하를 뺀다.
print(subway) #유재석, 김종국, 송지효, 양세찬으로 출력된다.

print(subway.pop()) #양세찬을 뺀다.
print(subway) #유재석, 김종국, 송지효으로 출력된다.

print(subway.pop()) #송지효를 뺀다.
print(subway) #유재석, 김종국으로 출력된다.

subway.append("유재석") #맨 뒤에 하하를 추가함
subway.append("유재석") #맨 뒤에 하하를 추가함
subway.append("유재석") #맨 뒤에 하하를 추가함

print(subway.count("유재석")) #유재석이 몇명 있는지를 샌다.

num_list = [5, 2, 4, 3, 1] # num_list가 5,2,4,3,1로 된다.
num_list.sort() #num_list정렬시킨다.
print(num_list) #1,2,3,4,5가 출력된다.

num_list.reverse() #num_list를 뒤집는다.
print(num_list) #5,4,3,2,1이 출력된다.

num_list.clear() #num_list안에 있는 수들을 지운다.
print(num_list) #[]가 출력된다.

mix_list = ["김종국", 40, True] #mix_list가 김종국, 40, True로 된다.
print(mix_list) #김종국, 40, True가 출력된다.

num_list.extend(mix_list) #num_list와 mix_list를 합한다.
print(num_list) #5,2,4,3,1, 김종국, 40, True가 출력된다.