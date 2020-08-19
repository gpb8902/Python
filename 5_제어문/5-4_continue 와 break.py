absent = [1, 4, 10, 12, 15, 21, 22, 25, 29] #absent가 1, 4, 10, 12...으로 지정된다.
no_book = [9] #no_book이 9로 지정된다.
for student in range(1, 31): #student가 1~30까지 있다.
    if student in absent: #만약 student가 absent면?
        continue #생략하고 계속 진행하다.
    elif student in no_book: #아니면 student가 no_book이면?
        print("¡Número de {0} estudiantes, ven a la sala de profesores!(으이구!! {0}번학생, 교무실로 올라와".format(student)) #¡Número de....이 출력된다.(student가 no_book에 있을 때)
        break #반복문을 멈춘다.
    print("Número de {0} estudiantes, lea un libro.({0}번 학생, 책읽어보세요.".format(student)) #Número de...이 출력된다.(student가 absent에 속해 있을 때)