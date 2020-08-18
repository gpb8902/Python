from random import * #랜덤 라이브러리 활성화

print(random()) #0.1~1.0미만의 임의의 값 생성
print(random()* 10) #0.1~10.0 미만의 임의의 값 생성
print(int(random()* 10)) #0~10미만의 임의의 값 생성
print(int(random()* 10 + 1)) #0~10미만의 임의의 값에서 1을 더한 임의의 값 생성

print(randrange(1, 101)) #1부터 101미만의 임의의 값 생성

print(randint(1, 45)) #1~45 이하의 임의의 값 생성
print(randint(1, 45)) #"(==같다)
print(randint(1, 45)) #"
print(randint(1, 45)) #"
print(randint(1, 45)) #"
print(randint(1, 45)) #"