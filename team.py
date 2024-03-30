from statistic import Statistic


class Team:

    def __init__(self, char_class: type, quantity: int):
        self.name = char_class.name
        self.characters = self.set_characters(
            char_class=char_class,
            quantity=quantity
        )
        self.stats = Statistic(survived=quantity)
        self.moves = quantity

    def set_characters(self, char_class: type, quantity: int):
        return [char_class() for _ in range(quantity)]

    def update_alive(self):
        self.characters = list(filter(lambda char: char.is_alive, self.characters))

    def update_moves(self):  # обновляет количество ходов
        self.moves = len(self.characters)
