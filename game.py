import sys
import random
from team import Team
from interface import Interface


class Game:

    first_team: Team
    second_team: Team
    interface: Interface = Interface()

    def start(self):
        self.interface.print_start()
        self.set_teams()
        self.interface.print_teams(first_team=self.first_team, second_team=self.second_team)
        while True:
            self.first_team.update_moves()
            self.second_team.update_moves()
            self._run()

    def set_teams(self):
        char_class = self.interface.get_character_class(team_number=1)
        quantity = self.interface.get_character_quantity(char_name=char_class.name)
        self.first_team = Team(char_class=char_class, quantity=quantity)
        char_class = self.interface.get_character_class(team_number=2)
        quantity = self.interface.get_character_quantity(char_name=char_class.name)
        self.second_team = Team(char_class=char_class, quantity=quantity)

    def _run(self):
        while self.first_team.moves > 0 or self.second_team.moves > 0:
            if self.first_team.moves > 0:
                self.team_move(attacker=self.first_team, attacked=self.second_team)
            if self.second_team.moves > 0:
                self.team_move(attacker=self.second_team, attacked=self.first_team)

    def team_move(self, attacker: Team, attacked: Team):
        victim_char = random.choice(attacked.characters)
        attacker_char = attacker.characters[0]
        caused_damage = attacker_char.use_attack(victim_char=victim_char)
        attacked.update_alive()
        attacker.stats.update(damage=caused_damage)

        if not victim_char.is_alive:
            self.interface.print_dead_character(attacker=attacker, attacked=attacked)
            attacked.stats.update(is_victim_dead=True)
            attacked.moves -= 1

        if not attacked.characters:
            self.end(looser=attacked, winner=attacker)

        attacker.moves -= 1

    def end(self, looser: Team, winner: Team):
        self.interface.print_end(looser=looser, winner=winner)
        self.interface.print_stats(first_team=self.first_team, second_team=self.second_team)
        sys.exit(0)
