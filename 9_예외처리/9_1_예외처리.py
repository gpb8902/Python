try:
    print("오직 한자리 수만 나눌 수 있는 계산기 입니다.")
    num1: int(input('첫번째 수를 입력하세요 : '))
    num2 = int(input("두번째 수를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다.")