#-----------------불리언, 변수, 주석 ---------------------------------------------------------------------------
#불리언은 True(참) 또는 False(거짓)으로 나눠져있다.


print(5<10) #10은 5보다 크므로 True 라고 출력된다.
print(5>10) #5는 10보다 작은데 여기선 크다고 나와있어 False로 출력된다.

print(35 == 26) #35는 26과 같지 않으므로 False로 출력된다.
print(8902 == 8902) #8902는 8902와 같기 때문에 True로 출력된다.


print("크림이" == "크림이") # ==은 같다라는 뜻이고 크림이 == 크림이는 참이므로 True가 출력된다.
print('villager' == 'pillager') #villager은 pillager이랑 같지 않으므로 False가 출력된다. 
print('Spain' == 'France')
print('남자' == '여자')
print('이등병' == '이등병')


banana = 7 #banana라는 변수가 7이랑 같다. 

print(banana == 7) #변수는 따옴표를 붙이지 않고, banana라는 변수는 7과 같기 때문에 True라고 출력된다.

print('내 나이는' + str(banana) + '살이야.')



banana = input('바나나의 개수:')    #바나나의 개수를 입력받음(문자열 변수 banana)
print(7 > int(banana))  #계산을 위해서 문자열 변수 banana를 정수형 변수로 변환 후 자신이 바나나를 7보다 작게 입력했으면 True로, 같거나 더 클때는 False로 출력된다.