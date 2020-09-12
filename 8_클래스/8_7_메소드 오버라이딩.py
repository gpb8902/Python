class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("상황병 : {0}(이)가 {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("HP : {0}, 공격력 :{1}".format(self.hp, self.damage))

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("상황병 : {0}이 {1}HP만큼의 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("상황병 : {0}의 현재 HP는 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("사령관 : 안타깝게도 {0}은 죽었어...".format(self.name))

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed =flying_speed

        def fly(self, name, location):
            print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(self.name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")