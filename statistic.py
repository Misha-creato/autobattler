

class Statistic:

    caused_damage: int = 0

    def __init__(self, survived: int):
        self.survived = survived

    def update(self, damage: int | None = None, is_victim_dead: bool = False):
        if damage is not None:
            self.caused_damage += damage
        if is_victim_dead:
            self.survived -= 1
