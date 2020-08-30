import time


rn = input("이름이 무엇입니까?")
time.sleep(2)
print(rn + "님, 안녕하세요.")
inf = input("당신이 다니는 학교는 어디입니까?")
time.sleep(3)
print(inf + "이라...")
secret = input("생일이 언제인가요?(78년3월9일생->783930")
time.sleep(2)
print(secret +"이군요!!")
ainff = input("당신은 어떤 언어를 배우고 싶습니까?(Python 같은 거 말고 한국어, 영어 같은 언어)")
time.sleep(6)
print(ainff + "를 배우고 싶군요!! 부럽습니다. 저도" + ainff + "을(를) 배우고 싶군요!")
ex = input("당신의 성별은 무엇인가요?(남자, 또는 여자로 대답해야만 함)")
    if ex == "남자":
    print("당신의 성별은" + ex + "이군요")
ainfff = input("당신은 애완동물을 기른가요?(네, 또는 아니요로 대답)")
time.sleep(4)


if ainfff == "네":
    print("정말로요?")
    ainffff = input("그럼 당신은 어떤 동물을 기르고 있나요?")
    time.sleep(3)
    if ainffff == "고양이":
        print("참으로 귀엽군요!!!")

        print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")
        time.sleep(80)
    elif ainffff == "개" or "강아지":
        print("참으로 귀엽지만, 저는 개공포증을 가지고 있어요!!")

        print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")
        time.sleep(80)
    elif ainffff == "새" or "앵무새":
        print("와! 정말 아름다운 새군요")

        print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")    
    elif ainffff == "금붕어" or "구피":
        print("물고기가 참 먆군요.")

        print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")
        time.sleep(80)
    elif ainffff == "토끼":
        print("털이 하얗네요. 하지만 야생 토끼에선 하얀 털을 가진 토끼는 없네요")

    print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")
        time.sleep(80)
    elif ainffff == "햄스터" or "기니피그":
        print("너무 깜찍하군요.")

        print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")
        time.sleep(80)
    else:
        print("당신은 특별한 애완동물을 기르고 있군요.")

        print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")
        time.sleep(80)
elif ainfff == "아니요":
    print("부모의 반대가 심하거나 자신이 털 알레르기가(애완동물) 있나 봐요.")

    print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은 어떠한 애완동물도 기르고 있지 않군요.")
    time.sleep(80)

elif ex == "여자":
    print("당신의 성별은 {0}이군요".format(ex))
ainfff = input("당신은 애완동물을 기른가요?(네, 또는 아니요로 대답)")
time.sleep(4)


if ainfff == "네":
    print("정말로요?")
    ainffff = input("그럼 당신은 어떤 동물을 기르고 있나요?")
    time.sleep(3)
    if ainffff == "고양이":
        print("참으로 귀엽군요!!!")

        print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")
        time.sleep(80)
    elif ainffff == "개" or "강아지":
        print("참으로 귀엽지만, 저는 개공포증을 가지고 있어요!!")

        print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")
        time.sleep(80)
    elif ainffff == "새" or "앵무새":
        print("와! 정말 아름다운 새군요")

        print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")    
    elif ainffff == "금붕어" or "구피":
        print("물고기가 참 먆군요.")

        print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")
        time.sleep(80)
    elif ainffff == "토끼":
        print("털이 하얗네요. 하지만 야생 토끼에선 하얀 털을 가진 토끼는 없네요")

    print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")
        time.sleep(80)
    elif ainffff == "햄스터" or "기니피그":
        print("너무 깜찍하군요.")

        print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")
        time.sleep(80)
    else:
        print("당신은 특별한 애완동물을 기르고 있군요.")

        print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은" + ainffff + "를 기르고 있군요.")
        time.sleep(80)
elif ainfff == "아니요":
    print("부모의 반대가 심하거나 자신이 털 알레르기가(애완동물) 있나 봐요.")

    print(rn + "님의 자기소개 메세지가 나왔어요.\n\n\n안녕하세요, 저는" + inf + "에 다니는"+ rn + "입니다.제 생년월일은" + secret + "이고, 배우고 싶은 언어는" + ainff + "이며,\n 당신은 어떠한 애완동물도 기르고 있지 않군요.")
    time.sleep(80)

open_se()