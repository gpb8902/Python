#name = "마린"
#hp = 40
#damage = 5

#tank_name = "더블더블 탱크"
#tank_hp = 300
#tank_damage = 70

#print("{} 유닛이 생성되었습니다.".format(name))
#print("HP : {}".format(hp))
#print("공격력 : {}\n".format(damage))

#print("{} (이)가 생성되었습니다.".format(tank_name))
#print("HP : {}".format(tank_hp))
#print("공격력 : {}".format(tank_damage))

#tank2_name = "더블더블 디렉스 탱크"
#tank2_hp = 600
#tank2_damage = 140

#print("{} (이)가 생성되었습니다.".format(tank2_name))
#print("HP : {}".format(tank2_hp))
#print("공격력 : {}".format(tank2_damage))

#def attack(name, location, damage):
#    print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 : {2}]".format(name, location, damage))

#attack(name, "1시", damage)
#attack(tank_name, "12시", tank_damage)
#attack(tank2_name, "2시", tank2_damage)

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