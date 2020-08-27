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
