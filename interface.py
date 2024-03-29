from constants import CHARACTER_CLASSES
from team import Team


class Interface:

    def __init__(self):
        self.characters = self.get_all_characters()

    def get_character_class(self):
        self.print_characters()
        while True:
            player_choice = input('Input character number: ')
            if player_choice in self.characters.keys():
                print(f'You chose {self.characters[player_choice].__name__}')
                return CHARACTER_CLASSES[int(player_choice) - 1]
            print('Invalid character number.')

    def get_character_quantity(self):
        while True:
            player_answer = input('Input characters quantity: ')
            if player_answer.isdigit() and int(player_answer) > 0:
                return int(player_answer)
            print('Invalid characters quantity')

    def print_characters(self):
        for key, char in self.characters.items():
            print(f'{key}. {char.__name__} '
              f'[HP: {char().get_hp()} '
              f'ATTACK: {char().get_attack()} '
              f'HIT_CHANCE: {char().get_hit_chance()}]')

    def print_teams(self):
        print()

    def print_dead_character(self, attacker: Team, attacked: Team):
        print(f'{attacker.name} killed '
              f'{attacked.name}, '
              f'{len(attacked.characters)} {attacked.name} left')

    def get_all_characters(self):
        char_keys = [str(i + 1) for i in range(len(CHARACTER_CLASSES))]
        return dict(zip(char_keys, CHARACTER_CLASSES))

    def print_end(self, winner: Team, looser: Team):
        print(f'Team "{winner.name}" won! '
              f'Survived: {len(winner.characters)}, '
              f'damage caused to the team "{looser.name}": {winner.caused_damage} ')
