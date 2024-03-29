import random
from characters import Character


class Team:

    def __init__(self, char_class: type, quantity: int):
        self.name = char_class.__name__
        self.characters = [char_class() for _ in range(quantity)]
        self.caused_damage = 0
        self.quantity = quantity
        self.moves = quantity

    def update_alive(self):
        self.characters = list(filter(lambda char: char.get_is_alive(), self.characters))

    def use_attack(self, victim_char: Character):
        chance = self.characters[0].get_hit_chance()
        chance /= 100
        if random.random() < chance:
            damage = self.characters[0].get_attack()
            victim_char.decrease_hp(damage=damage)
            self.caused_damage += damage

    def update_moves(self):
        self.moves = self.quantity
