import random


class Character:

    name: str
    hp: int
    attack: int
    hit_chance: int
    is_alive: bool = True

    def get_hit_chance(self):
        return self.hit_chance / 100

    def decrease_hp(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False

    def use_attack(self, victim_char: 'Character') -> int | None:
        if random.random() < self.get_hit_chance():
            damage = self.attack
            victim_char.decrease_hp(damage=damage)
            return damage


class Penguin(Character):

    name = 'Penguin'
    hp = 10
    attack = 2
    hit_chance = 90


class Cat(Character):

    name = 'Cat'
    hp = 12
    attack = 3
    hit_chance = 70


class Granny(Character):

    name = 'Granny'
    hp = 12
    attack = 4
    hit_chance = 75


class Teen(Character):

    name = 'Teen'
    hp = 20
    attack = 1
    hit_chance = 100


class Soldier(Character):

    name = 'Soldier'
    hp = 30
    attack = 8
    hit_chance = 80


class Stormtrooper(Character):

    name = 'Stormtrooper'
    hp = 25
    attack = 20
    hit_chance = 30


class TRex(Character):

    name = 'T-Rex Dinosaur'
    hp = 100
    attack = 30
    hit_chance = 95
