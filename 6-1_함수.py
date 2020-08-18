nickname = input("닉네임을 무었으로 바꾸시겠습니까?") #nickname이 input에 대한 답변이 된다.

def open_account(): #def는 함수를 쓸때 쓰고open_account():는 식당에서 말하면 호출벨 같은 것이다.
    print("닉네임이 {0}(으)로 변경되었습니다.".format(nickname)) #닉네임이 답변 으로 변경되었습니다. 로 출력된다.

open_account() #식당에서 말하면 호출벨 같은 것이다.(아래에 이걸 써야 함수가 출력된다.)