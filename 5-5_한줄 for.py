students = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Kim 은지", "Park 민우", "Park 정환", "Yee 진준", "Char 은수"]
students = [len(i) for i in students]
print(students)

students = ["Kim Un Ji", "Park Min O", "Park Jung Hwan", "Yee Jin June", "Char Un Su"]
students = [i.upper() for i in students]
print(students)