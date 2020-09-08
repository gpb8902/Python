import pickle
#profile_file = open("profile.pickle", "wb")
#profile = {"이름":"박정한", "나이":15, "취미":["게임", "컴퓨터", "음악", "코딩"]}
#print(profile)
#pickle.dump(profile, profile_file)
#profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()