class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("HP : {0}, 공격력 :{1}".format(self.hp, self.damage))

marine1 = Unit("슈퍼 마린", 80, 10)
marine2 = Unit("마린", 40, 5)
marine3 = Unit("마린 킹", 160, 20)
marine4 = Unit("마린", 40, 5)
marine5 = Unit("슈퍼 마린킹", 320, 40)
marine6 = Unit("슈퍼 마린", 80, 10)

tank = Unit("탱크", 150, 35)
tank = Unit("탱크", 150, 35)
tank = Unit("탱크", 150, 35)
tank = Unit("탱크", 150, 35)
tank = Unit("탱크", 150, 35)
tank = Unit("탱크", 150, 35)