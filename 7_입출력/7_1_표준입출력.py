print("Python", "Java", sep=",")
print("Python", "Java", sep="+")
print("Python", "Java", sep=" vs ")
print("Python", "Java", "JavaScript", sep=" vs ")
print("Python", "Java", sep=", ", end="? ")
print("Which programing is funnier, Python or Java?")
print("Python", "Java", sep=", ")
print("Which programing is funnier, Python or Java?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

scores = {"수학":85, "영어":100, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(15), str(score).rjust(5), sep=":")

for num in range(1, 1000):
    print("대기번호 : " + str(num).zfill(3))

answer = input("다음중 당신이 가장 좋아하는 호러캐릭터는?(Granny, Bendy, Bardy, Siren Head, Cartoon cat) : ")
print("당신이 좋아하는 호러캐릭터는 " + answer + "(이)군요." + answer + " is so scary that I'll have nightmare.")
print(type(answer))