import sys
import random
from team import Team
from interface import Interface
from statistic import Statistic


class Game:

    first_team: Team = None
    second_team: Team = None
    interface: Interface = Interface()
    statistic: Statistic

    def start(self):
        self.interface.print_start()
        self.set_teams()
        self.statistic = Statistic(first_team=self.first_team, second_team=self.second_team)
        self.interface.print_teams(first_team=self.first_team, second_team=self.second_team)

        while True:
            self.first_team.update_moves()
            self.second_team.update_moves()
            self._run()

    def set_teams(self):
        while self.second_team is None:
            self.first_team = self.get_team(team_number=1)
            self.second_team = self.get_team(team_number=2)

    def get_team(self, team_number: int):
        while True:
            char_class = self.interface.get_character_class(team_number=team_number)
            if self._repeat_input_or_exit(player_input=char_class, team_number=team_number):
                return None
            quantity = self.interface.get_character_quantity(char_name=char_class.name)
            if not self._repeat_input_or_exit(quantity, team_number=team_number, is_quantity=True):
                return Team(char_class=char_class, quantity=quantity)

    def _repeat_input_or_exit(self, player_input: str | int | type, team_number: int, is_quantity: bool = False):
        if player_input == 'b':
            if is_quantity or team_number == 2:
                return True
        elif player_input == 'q':
            self.interface.print_exit()
            sys.exit(0)

    def _run(self):
        while self.first_team.moves > 0 or self.second_team.moves > 0:
            if self.first_team.moves > 0:
                self.team_move(attacker=self.first_team, victim=self.second_team)
            if self.second_team.moves > 0:
                self.team_move(attacker=self.second_team, victim=self.first_team)

    def team_move(self, attacker: Team, victim: Team):
        victim_char = random.choice(victim.characters)
        attacker_char = attacker.characters[0]
        caused_damage = attacker_char.use_attack(victim_char=victim_char)
        victim.update_alive()
        self.statistic.update(name=attacker.name, damage=caused_damage)

        if not victim_char.is_alive:
            self.interface.print_dead_character(attacker=attacker, victim=victim)
            self.statistic.update(name=victim.name, is_victim_dead=True)
            victim.moves -= 1

        if not victim.characters:
            self.end(looser=victim, winner=attacker)

        attacker.moves -= 1

    def end(self, looser: Team, winner: Team):
        self.interface.print_end(looser=looser, winner=winner)
        self.statistic.show_stats()
        sys.exit(0)
