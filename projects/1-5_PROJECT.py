print("안녕하십니까?저는 이번에 특이한중학교에 전학생이고 이름은 밝히지 않겠습니다.")
rn = input("당신의 이름은 무었입니까?")
inf = input("당신 전 학교는 어디입니까?")
print(inf + "이라...")
ainf = input("그럼 생일이 언제입니까?")
print(ainf +"이군요!!")
ainff = input("왜 하필 이름이" + rn + "인가요?")
print(ainff)
ainfff = input("너 솔로니?(응, 또는 아니 라고만 대답해야함)")

if ainfff == "응":
    print ("동족이여!!!")
    ainffff = input("형이나 누나나 동생있어?(응 또는 아니 라고 대답해야함)")
    if ainffff == "응":
        print("있어?")
        oinf = input("그 사람 이름 뭐야?")
        print("이제 끝, 저기 Muchim YeolMu 옆에 앉아라")

    elif ainffff == "아니":
        print("종료!!이제 저기 옆에 교장쌤 옆에 앉아라")

elif ainfff == "아니":
    print("이 학교 교장쌤은 커플은 강제퇴학을 시키는 교법을 만들어서 퇴학당했다.")