import time

def receipt():  #영수증 발급을 위한 함수
    receipt = open("receipt.txt", "r", encoding="utf8")
    print("현 잔액 : ", file=receipt)
    print("가격 : ", file=receipt)
    receipt.close()

def line(): #줄을 표현하기 위한 함수
    print("---------------------------------------------------------------------------")

def purchase(menuName, price): #돈 계산을 위한 함수
    if int(money) >= int(price):    #돈이 가격보다 많거나 같으면
        print("주문이 완료되었습니다. 현재 남은잔액은 {0} 입니다.".format(int(money)-int(price)))   #주문 성공!
        return int(money)-int(price)
    else:   #돈이 가격보다 적을경우
        print("잔액이 부족합니다. 현재 남은잔액은 {0} 입니다.".format(int(money)))
        charge = input("카드에 돈을 충전하시겠어요? (Y/N) ")
        if charge == "Y" or "y":
            chargeMoney()
        elif charge == "N" or "n":
            line()
            print('앞으로 고객님을 위한 더 좋은 앱이 되도록 하겠습니다. 감사합니다.')
            line()
            exit

def chargeMoney():
    money = input("카드에 몇 원을 추가하시겠습니까? (숫자만 입력하세요.) -> ")
    selectMenu()

def selectMenu():   #메뉴 선택 함수
    selectedMenu = input("""
---------------------------------------------------------------------------
도미니카공화국 피자
Menu

1 -> 피자
2 -> 사이드
3 -> 음료

---------------------------------------------------------------------------
""")

    open_menu()



def open_menu():    #메뉴판 여는 함수
    if selectedMenu == "1": #피자 메뉴가 선택되었을 때
        line()
        print("※ 피자 메뉴 [현재 잔액: " + money + "원 ]")
        order1 = input("""
(1)불고기피자  29,000원
(2)콤비네이션피자  27,000원
(3)치즈피자    27,500원
(4)하와이안파인애플피자    34,800원
(5)고구마피자  28,000원
(6)남미의 해산물피자   29,700원
""")
        line()
        if order1 == "1":   #불고기피자
            choose1 = input("주문하신 음식이 불고기피자(29,000원)가 맞나요? (Y, N)")
            if choose1 == "Y" or "y":
                purchase(menuName="불고기피자", price=29000)
            elif choose1 == "아니요":
                selectMenu()
            else:
                print()
        elif order1 == "2": #콤비네이션피자
            choose2 = input("주문하신 음식이 콤비네이션피자(27,000원)가 맞나요? (Y, N)")
            if choose2 == "Y" or "y":
                purchase(menuName="콤비네이션피자", price=27000)
            elif choose2 == "N" or "n":
                selectMenu()
        elif order1 == "3":   #불고기피자
            choose1 = input("주문하신 음식이 치즈피자(27,500원)가 맞나요? (Y, N)")
            if choose1 == "Y" or "y":
                purchase(menuName="치즈피자", price=27500)
            elif choose1 == "아니요":
                selectMenu()
            else:
                print()
        elif order1 == "4":   #불고기피자
            choose1 = input("주문하신 음식이 하와이안파인애플피자(34,800원)가 맞나요? (Y, N)")
            if choose1 == "Y" or "y":
                purchase(menuName="하와이안파인애플피자", price=34800)
            elif choose1 == "아니요":
                selectMenu()
            else:
                print()
        elif order1 == "5":   #불고기피자
            choose1 = input("주문하신 음식이 고구마피자(28,000원)가 맞나요? (Y, N)")
            if choose1 == "Y" or "y":
                purchase(menuName="고구마피자", price=28000)
            elif choose1 == "아니요":
                selectMenu()
            else:
                print()
        elif order1 == "6":   #불고기피자
            choose1 = input("주문하신 음식이 남미의 해산물피자(29,700원)가 맞나요? (Y, N)")
            if choose1 == "Y" or "y":
                purchase(menuName="남미의 해산물피자", price=29700)
            elif choose1 == "아니요":
                selectMenu()
            else:
                print()
    elif selectedMenu == "2":
        line()
        print("※ 사이드 메뉴 [현재 잔액: " + money + "원 ]")
        order2 = input("""
(1)오븐구이스파게티    7,600원
(2)크림치즈스파게티    7,600원
""")
        line()
        if order2 == "1":   #불고기피자
            choose1 = input("주문하신 음식이 오븐구이스파게티(7,600원)가 맞나요? (Y, N)")
            if choose1 == "Y" or "y":
                purchase(menuName="오븐구이스파게티", price=7600)
            elif choose1 == "아니요":
                selectMenu()
            else:
                print()
        elif order2 == "2":   #불고기피자
            choose1 = input("주문하신 음식이 크림치즈스파게티(7,600원)가 맞나요? (Y, N)")
            if choose1 == "Y" or "y":
                purchase(menuName="크림치즈스파게티", price=7600)
            elif choose1 == "N" or "nd":
                selectMenu()
            else:
                print()
    elif selectedMenu == "3":
        line()
        print("※ 음료수 메뉴 [현재 잔액: " + money + "원 ]")
        order3 = input("""
(1)콜라(1L)    1,200원
(2)사이다(1L)  1,200원
(3)환타(1L)    1,200원
""")
        line()
        if order3 == "1":   #불고기피자
            choose1 = input("주문하신 음식이 콜라(1L)(1,200원)가 맞나요? (Y, N)")
            if choose1 == "Y" or "y":
                purchase(menuName="콜라(1L)", price=1200)
            elif choose1 == "아니요":
                selectMenu()
            else:
                print()
        elif order3 == "2":   #불고기피자
            choose1 = input("주문하신 음식이 사이다(1L)(1,200원)가 맞나요? (Y, N)")
            if choose1 == "Y" or "y":
                purchase(menuName="사이다(1L)", price=1200)
            elif choose1 == "아니요":
                selectMenu()
            else:
                print()
        elif order3 == "3":   #불고기피자
            choose1 = input("주문하신 음식이 환타(1L)(1,200원)가 맞나요? (Y, N)")
            if choose1 == "Y" or "y":
                purchase(menuName="환타(1L)", price=1200)
            elif choose1 == "아니요":
                selectMenu()
            else:
                print()
    
print("""
---------------------------------------------------------------------------
안녕하십니까? 로켓음식배달입니다.
출시된 지 얼마되지 않아서, 주문시킬 수 있는 음식점이 도미니카공화국 피자 밖에 없습니다. 
한 주문당 한 음식만 시킬 수 있습니다.
---------------------------------------------------------------------------
""")    #앱 시작할 때 나오는 메시지

money = input("카드에 몇 원을 추가하시겠습니까? (숫자만 입력하세요.) -> ")

selectedMenu = input("""
---------------------------------------------------------------------------
도미니카공화국 피자
Menu

1 -> 피자
2 -> 사이드
3 -> 음료

---------------------------------------------------------------------------
""")

open_menu()
