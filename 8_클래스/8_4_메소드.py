class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("HP : {0}, 공격력 :{1}".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("HP : {0}, 공격력 :{1}".format(self.hp, self.damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("사령관 : {0}이 {1}HP만큼의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("사령관 : {0}의 현재 HP는 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("사령관 : 안타깝게도 {0}은 죽었어...".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)