import time
from rich.console import Console
from rich.table import Table
from team import Team
from constants import CHARACTER_CLASSES


class Interface:

    def get_character_class(self, team_number: int):
        print(f'\nChoose one of following characters for the team {team_number}\n')
        self.print_characters()
        while True:
            choice = input('\nInput character number: ')
            if choice.isdigit() and int(choice) in range(1, len(CHARACTER_CLASSES) + 1):
                print(f'\nYou chose {CHARACTER_CLASSES[int(choice) - 1].name} \n')
                return CHARACTER_CLASSES[int(choice) - 1]
            print('Invalid character number.')

    def get_character_quantity(self, char_name: str):
        while True:
            answer = input(f'Input "{char_name}" character quantity: ')
            if answer.isdigit() and int(answer) > 0:
                return int(answer)
            print('Invalid characters quantity')

    def print_characters(self):
        counter = 1
        for character in CHARACTER_CLASSES:
            time.sleep(0.5)
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
            f'of {len(first_team.characters)}!\n')

    def print_dead_character(self, attacker: Team, attacked: Team):
        time.sleep(1)
        print(
            f'"{attacker.name}" killed '
            f'"{attacked.name}", '
            f'{len(attacked.characters)} "{attacked.name}" left'
        )

    def print_start(self):
        print('Hello! Welcome to the Autobattler Game!')

    def print_end(self, winner: Team, looser: Team):
        time.sleep(1)
        print(f'\nTeam "{winner.name}" won! Team "{looser.name}" lost...')

    def print_stats(self, first_team: Team, second_team: Team):
        table = Table(title="Statistics")

        table.add_column("Team", justify="left", style="cyan")
        table.add_column("Caused damage", justify="center", style="magenta")
        table.add_column("Survived", justify="center", style="green")

        table.add_row(
            first_team.name,
            str(first_team.stats.caused_damage),
            str(first_team.stats.survived)
        )
        table.add_row(
            second_team.name,
            str(second_team.stats.caused_damage),
            str(second_team.stats.survived)
        )

        console = Console()
        console.print(table)
