import sys
import random
from team import Team
from interface import Interface


class Game:

    first_team: Team
    second_team: Team
    interface: Interface = Interface()

    def start(self):
        self.set_teams()
        while True:
            self.first_team.update_moves()
            self.second_team.update_moves()
            self.main_loop()

    def set_teams(self):
        cls, quantity = self.interface.get_character_class(), self.interface.get_character_quantity()
        self.first_team = Team(char_class=cls, quantity=quantity)
        cls, quantity = self.interface.get_character_class(), self.interface.get_character_quantity()
        self.second_team = Team(char_class=cls, quantity=quantity)

    def main_loop(self):
        while self.first_team.moves > 0 or self.second_team.moves > 0:
            if self.first_team.moves > 0:
                self.team_move(attacker=self.first_team, attacked=self.second_team)
            if self.second_team.moves > 0:
                self.team_move(attacker=self.second_team, attacked=self.first_team)

    def team_move(self, attacker: Team, attacked: Team):
        victim = random.choice(attacked.characters)
        attacker.use_attack(victim_char=victim)
        attacked.update_alive()
        if not victim.get_is_alive():
            self.interface.print_dead_character(attacker=attacker, attacked=attacked)
            attacked.moves -= 1
        if not attacked.characters:
            self.end(looser=attacked, winner=attacker)
        attacker.moves -= 1

    def end(self, looser: Team, winner: Team):
        self.interface.print_end(looser=looser, winner=winner)
        sys.exit(0)
