import time
from team import Team
from constants import CHARACTER_CLASSES


class Interface:

    def get_character_class(self, team_number: int):
        commands, choices = self.prepare_commands_and_choices(team_number=team_number)
        while True:
            choice = input(f'\nInput character number{commands}: ')
            if choice.isdigit() and int(choice) in range(1, len(CHARACTER_CLASSES) + 1):
                choice = int(choice)
                character = CHARACTER_CLASSES[choice - 1]
                print(f'\nYou chose {character.name} \n')
                return character
            elif choice in choices:
                return choice
            print('Invalid character number.')

    def prepare_commands_and_choices(self, team_number: int):
        time.sleep(0.5)
        print(f'\nChoose one of following characters for the team {team_number}\n')
        self.print_characters()
        commands = ' (press "b" to go back, press "q" to exit)'
        choices = ['b', 'q']
        if team_number == 1:
            commands = ' (press "q" to exit)'
            choices = ['q']
        return commands, choices

    def get_character_quantity(self, char_name: str):
        commands = ' (press "b" to go back, press "q" to exit)'
        while True:
            answer = input(f'Input "{char_name}" character quantity{commands}: ')
            if answer.isdigit() and int(answer) > 0:
                return int(answer)
            elif answer in ['b', 'q']:
                return answer
            print('Invalid characters quantity')

    def print_characters(self):
        time.sleep(1)
        counter = 1
        for character in CHARACTER_CLASSES:
            print(
                f'{counter}. {character.name} '
                f'[HP: {character.hp} '
                f'ATTACK: {character.attack} '
                f'HIT_CHANCE: {character.hit_chance} %]'
            )
            counter += 1

    def print_teams(self, first_team: Team, second_team: Team):
        time.sleep(1)
        print(
            f'\nLet the battle begin between team {first_team.name} '
            f'of {len(first_team.characters)} and team {second_team.name} '
            f'of {len(second_team.characters)}!\n'
        )

    def print_dead_character(self, attacker: Team, victim: Team):
        time.sleep(1)
        print(
            f'"{attacker.name}" killed '
            f'"{victim.name}", '
            f'{len(victim.characters)} "{victim.name}" left'
        )

    def print_start(self):
        time.sleep(0.5)
        print('Hello! Welcome to the Autobattler Game!')

    def print_end(self, winner: Team, looser: Team):
        time.sleep(1)
        print(f'\nTeam "{winner.name}" won! Team "{looser.name}" lost...')

    def print_exit(self):
        print('You chose to exit game.')
