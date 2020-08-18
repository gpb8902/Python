print(1+2+3) #1+2+3=6, 6으로 출력된다.
print(-2+66) #-2 + 64 = 62, 62로 출력된다.
print(2**10) #2의 10제곱인 1024가 출력된다.
print(6%4) #6/4의 나머지인 2가 출력된다.
print(5 == 3-(-9)) #5 = 3+9, 5 = 12는 거짓이므로 False로 출력된다.
print(3**4) #3의 4제곱인 81이 출력된다.
print(9//5)#9/5의 몫이 출력된다.
if ('C' == 'C'):
    print('You are right!') #만약 C == C가 참이라면 You are right가 출력된다.
else:
    print('Are You stupid?') #만약 C == C가 거짓이라면 Are you stupid?가 출력된다.

print(29<-100) #29>-100이 참이지만 반대로 되어있어 False로 출력된다.
print(9<=9) #<=는 오른쪽 정수가 왼쪽에 있는 정수랑 같거나 크다는 뜻으로, 9<=9는 참이므로, True가 출력된다.
print(20 <=-30) #14번째 줄이랑 같은 내용이다. 하지만 잘못되어있어서 False로 출력된다.
print((20>19) & (30<10000)) #20>19는 True, 30<10000은 True이므로 True라고 출력된다.
print((5>0) or (20<21)) #5>0이나, 20<21이나 True로 True라고 출력된다.
print(2 + 3 * 8) #3*8=24, 2 + 24 = 26이므로, 26으로 출력된다.
print((2 +3) * 8) #2+3 = 5, 5*8 = 40이므로, 40으로 출력된다.
number = 2**2 #number이라는 변수는 2의 제곱인 4와 같다.
print(number) #4가 출력된다.
number = (number + 7) * 4 #4+7 = 11, 11*4 = 44 이므로, Number은 44가 된다.
print(number) #44로 출력된다.
number = number/11 #44/11= 4로 number은 4로 된다.
print(number) #4가 출력된다.
number = number **4  #number = 4의 4제곱인 256이 되므로, number은 256이 된다.
print(number) #256이 출력된다.
number = number/2 #256을 2로 나눈 몫인 128이 number가 된다.
print(number) #128이 출력이 된다.
print(abs(-6488)) #-6488의 절댓값인 6488이 출력된다.
print(abs(56545) - abs(6545)) #56545의 절댓값에서, 6545의 절댓값은 뺀, 50000이 된다.
print(round(7.68468)) #7.68468을 
print(pow(9, 9)) #9의 9제곱인387420489
print(max(2, 9)) #두 수중 가장 큰 수인 9를 출력한다.
print(min(68, 6544)) #두 수에서 가장 작은 수인 68을 출력한다.

from math import * #math Library를 불러온다.(import)
print(floor(4.99)) #4.99를 내림한 4가 출력된다.
print(ceil(5.65498)) #5.65498을 올림한 6이 출력된다.
print(sqrt(16)) #16의 제곱근인 4가 출력된다.