weather = input("AI : 오늘 날씨는 어떤가요?")
if weather == "비" or weather == "눈":
    print("(AI가 차가운 물풍선을 내 머리 위로 뿌렸다. 그래서 나는 감기에 걸렸다.)")
elif weather == "미세먼지":
    print("(AI가 CS탄 2개를 나한테 뿌렸다. HP가 5씩 닳는 기분이 든다.")
else: 
    print("AI가 갑자기 집을 올리고 거대 돌 조각상 6개가 나와 집을 관으로 삼아 관짝춤을 추었다. 지상과의 거리는 23.651m이다.난 언제쯤 정상적으로 나갈까?")

temp = int(input("AI : 기온은 어때요?"))
if 30 <= temp:
    print("(AI가" + temp + "C의 온도로 집 안을 맞춰 놓아서 덥다.)")
elif 10 <= temp and temp < 30:
    print("(AI가 드디어 제일을 하나 싶었지만, -2배온도로 해가지고 얼어 죽을 것 같다.)")
else:
    print("(므흐흐 으흐흐흐므흐흐흐!!(AI가 나를 냉동인간으로 만들었다. 춥댜.)")