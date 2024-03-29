

class Character:

    _hp: int
    _attack: int
    _hit_chance: int
    _is_alive: bool = True

    def get_hp(self):
        return self._hp

    def get_attack(self):
        return self._attack

    def get_hit_chance(self):
        return self._hit_chance

    def decrease_hp(self, damage: int):
        self._hp -= damage
        if self._hp <= 0:
            self._hp = 0
            self._is_alive = False

    def get_is_alive(self):
        return self._is_alive


class Penguin(Character):

    _hp = 10
    _attack = 2
    _hit_chance = 90


class Cat(Character):

    _hp = 12
    _attack = 3
    _hit_chance = 70


class Granny(Character):

    _hp = 12
    _attack = 4
    _hit_chance = 75


class Teen(Character):

    _hp = 20
    _attack = 1
    _hit_chance = 100


class Soldier(Character):

    _hp = 30
    _attack = 8
    _hit_chance = 80


class Stormtrooper(Character):

    _hp = 25
    _attack = 20
    _hit_chance = 30


class TRex(Character):

    _hp = 100
    _attack = 30
    _hit_chance = 95

