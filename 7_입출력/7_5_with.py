with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("전과목에 대한 모든 지식을 얻고 싶어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))