students = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] #students가 1~25까지 있다.
print(students) #1~25까지 출력된다.
students = [i+100 for i in students] #student앞에 100을 붙인다.
print(students) #101, 102,103...이 출력된다.

students = ["Kim 은지", "Park 민우", "Park 정환", "Yee 진준", "Char 은수"] #students가 Kim 은지, Park 민우...으로 출력된다.
students = [len(i) for i in students] #students에 몇글자 있는지를 알려준다.
print(students) #6, 7, 7, 6, 7이 출력된다.

students = ["Kim Un Ji", "Park Min O", "Park Jung Hwan", "Yee Jin June", "Char Un Su"] #Students가 Kim Un Ji, Park Min O...이 된다.
students = [i.upper() for i in students] #모든 단어를 대문자로 바꾼다.
print(students) #KIM UN JI, PARK MIN O...으로 출력된다.