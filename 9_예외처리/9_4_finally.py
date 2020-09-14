class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 수만 나눌 수 있는 전용 계산기 입니다.")
    num1 = int(input("첫번째 수를 입력하세요 : "))
    num2 = int(input("두번째 수를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력갑 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 수만 입력 할 수 있습니다.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 수만 입력 할 수 있습니다.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")