from random import *
def quiz_right():
    right = randrange(1,6)
    if right == 1:
        print("당신은 애국자!!!")
    elif right == 2:
        print("(He or She) is the perfect Korean among those I have seen so far.")
    elif right == 3:
        print("아닛!!! 혹시 SKY를 뛰어넘어 하버드대 한국역사학과(있는지는 모르겠다.) 출신인가요?")
    elif right == 4:
        print("Muchim Doraji:Is He or She the smartest Korean? \n아 네 Muchim Doraji님께서 문자 보내주었습니다.")
    elif right == 5:
        print("대대손손 애국자의 혈흔이 느껴집니다.")


def quiz_wrong():
    wrong = randrange(1,6)
    if wrong == 1:
        print("와... 실망입니다.")
    elif wrong == 2:
        print("Muchim Gaji: Is He or She Chinese?\n 아 네, Muchim Gaji님께서 실망이 크셨나봐요.")
    elif wrong == 3:
        print("뛰어난 친일력!!!")
    elif wrong == 4:
        print("진정한 을사오적 혈통이군요!!")
    elif wrong == 5:
        print("(He or She) is the perfect Japanese among those I have seen so far.")

print("---------------------------------------------------------------------------")
print("안녕하십니까? 저는 광복절 퀴즈를 진행할 사회자 사. 회. 자 입니다. \n답은 1,2,3...으로 번호만 작성해 주세요. 문제 나갑니다!")
print("---------------------------------------------------------------------------")
ans = input(""" 
1번 문제!!
광복절은 언제 일어났나요?
1번: 1945년 8월 14일
2번: 1954년 8월 15일
3번: 1945년 8월 15일
4번: 1845년 8월 15일
5번: 1954년 8월 15일
→ """)  #1번 문제

if "3" == ans:  #정답 3번이 맞을 때
    print("---------------------------------------------------------------------------")
    quiz_right()
    print("---------------------------------------------------------------------------")
    ans = input("""
2번 문제!!
다음중 독립운동가가 아닌 사람은?

1번: 유관순
2번: 박제순
3번: 안창호
4번: 김  구
→ """)  #2번 문제로 넘어감
    if "2" == ans:  #2번문제 정답2 맞출때
        print("---------------------------------------------------------------------------")
        quiz_right()
        print("---------------------------------------------------------------------------")
        ans = input("""
3번 문제!! 다음의 편지를 읽고
쓴 독립운동가를 맞추시오.

여기는 서울,
많은 독립운동가들이 수감되어있었다.
물론 나 또한 여기에 있었다.
왜 우리는 여기서 고문을 받아야 하는가
우리는 단지 모국을 되찾을려고 하는데
저는 꽃다운 나이에 먼저 갑니다...
 
1번: 유관순
2번: 윤봉길
3번: 김  구
→ """)
        if ans == "1": #3번문제 정답1 맞출때
            print("---------------------------------------------------------------------------")
            quiz_right()
            print("---------------------------------------------------------------------------")
            ans = input("""
4번 문제!!
다음 중 우리 말이 아닌 것은?
        
1번: 오두방정
2번: 냄비
3번: 교도소
→ """)  #4번에 2번
            if ans == "2":  #4번문제 정답 2맞출 때
                print("---------------------------------------------------------------------------")
                quiz_right()
                print("---------------------------------------------------------------------------")
                ans = input("""
5번 문제!!
광복절 이후 일어난 사건중
가장 먼저 일어난 것은?

1번: 5.18 민주화 운동
2번: 88올림픽 개막
3번: 4.19 혁명
4번: 6.25 전쟁
→""")
                if ans == "4":  #5번문제 정답 4맞출 때
                    print("---------------------------------------------------------------------------")
                    quiz_right()
                    print("---------------------------------------------------------------------------")
                    ans = input("""
6번 문제!!
다음 암호를 푼 결과는

3 1,10  14 1 2  3 5 1  4 10 6  5 1 2  7 3,10
올챙이 = 8 5 4  10 1,10 8  8 10
        
1번: 대일본제국짱
2번: 일본이싫어요
3번: 독도는우리땅
4번: 다람이근육질
5번: 대한독립만세
→ """)  #6번에 5번
                    if ans =="5": #6번문제가 5일때
                        quiz_right()
                    
                    else:#6번 문제가 틀렸을 때
                                quiz_wrong()

                else: #5번 문제가 틀렸을 때
                            quiz_wrong()

            else:#4번 문제가 틀렸을 때
                    quiz_wrong()

        else:   #3번 문제가 틀렸을 때
            quiz_wrong()
    
    else:  #2번 문제가 틀렸을 때
       quiz_wrong()

else:  #1번 문제가 틀렸을 때
    quiz_wrong()

