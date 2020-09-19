language = input("무슨 언어를 좋아하세요?(한국어, 영어, 중국어와 같은 언어들)")
print("{0}은(는) 좋은 언어입니다! 훌륭하시군요!!".format(language))
speak = input("그럼 혹시 {0}을(를) 읽고, 쓰고, 말할 수 있나요?(Y or N)".format(language))

if speak == "Y" or "y":
    print("당신은 언어 천재군요!!")

elif speak == "N" or "n":
    print("그럼 나중에 한번 공부해 보세요. 아마 도움이 될 거 에요.")

else:
    print("그럼 무엇이란 말입니까? 그럼 안녕~~~!")




#==========================================외장함수 부분(내장함수 강의에서 나온 외장함수)======================================================
print(dir())
import random
print(dir())
import pickle
print(dir())

print(dir(random))
lst = [1, 2, 3]
print(dir(lst))

name = "지나가던 인간"
print(dir(name))