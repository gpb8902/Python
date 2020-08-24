def KC(): #KC(K Coin의 약자)의 함수 생성
    print("K코인을 획득하였습니다.".format(KC)) #K코인을 획득하였습니다가 출력된다.

def deposit(BKC, KC): #BKC(Before K Coin의 약자)에서 KC(K Coin의 약자)가 출력된다.
    print("K코인을 획득하였습니다. 현재 남은 K코인은 {0} 입니다.".format(BKC, KC)) #코인을... 현재 남은 K코인은 BKC입니다.로 출력된다
    return BKC + KC #BKC+KC가 반환된다.
def withdraw(BKC, KC): #BKC에서 KC를 뺀다.
    if BKC >= KC: #BKC가 KC보다 크거나 같으면
       print("출금이 완료되었습니다. 현재 남은 K코인은 {0} 입니다.".format(BKC-KC)) #출금이 완료... 현재 남은 K코인은 BKC-KC 입니다가 출력된다.
       return BKC - KC  #BKC - KC가 반환되낟.

    else: #그렇지 않으면
        print("출금이 불가능합니다. 현재 남은K코인 {0}입니다.".format(BKC)) #출금이 불가능합니다...이 출력된다.
        return BKC #BKC가 반환된다.

def withdraw_night(BKC, KC): #야간에 보내는 K코인 + KC를 뺀다.
    commission = 200 #야간에 보내는 K코인이 200으로 지정된다.
    return commission, BKC - KC - commission #BKC에서 KC, commission을 뺀 값을 반환한다.

BKC = 5981 #BKC를 5981로 지정된다.
BKC = deposit(BKC, 6516598) #BKC가 BKC + 6516498로 지정된다.
BKC = withdraw(BKC, 10000000000) #BKC가 BKC - 10000000000로 지정된다.
commission, BKC = withdraw_night(BKC, 500) #commission이 BKC -500 으로 지정된다.
print("야간에 보내는 {0}K코인이 차감되었으며, 잔액은 {1}K코인 입니다.".format(commission, BKC)) #야간에 보내는 commission... 잔액은 BKC K코인 입니다.로 출력된다.
print(BKC) #BKC가 출력된다.

