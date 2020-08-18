absent = [1, 4, 10, 12, 15, 21, 22, 25, 29]
no_book = [6, 9, 17, 26, 30]
for student in range(1, 31):
    if student in absent:
        continue
    elif student in no_book:
        print("¡Número de {0} estudiantes, ven a la sala de profesores!(으이구!! {0}번학생, 교무실로 올라와".format(student))
        break
    print("Número de {0} estudiantes, lea un libro.({0}번 학생, 책읽어보세요.".format(student))