def KC():
    print("K코인을 획득하였습니다..".format(KC))

def deposit(BKC, KC):
    print("K코인을 획득하였습니다. 현재 남은 K코인은 {0} 입니다.".format(BKC, KC))
    return BKC + KC
def withdraw(BKC, KC):
    if BKC >= KC:
       print("출금이 완료되었습니다. 현재 남은 K코인은 {0} 입니다.".format(BKC-KC))
       return BKC - KC 

    else:
        print("출금이 불가능합니다. 현재 남은K코인 {0}입니다.".format(BKC))
        return BKC

def withdraw_night(BKC, KC):
    commission = 200
    return commission, BKC - KC - commission

BKC = 5981
BKC = deposit(BKC, 6516598)
BKC = withdraw(BKC, 10000000000)
commission, BKC = withdraw_night(BKC, 500)
print("야간에 보내는 {0}K코인이 차감되었으며, 잔액은 {1}K코인 입니다.".format(commission, BKC)) 
print(BKC)

