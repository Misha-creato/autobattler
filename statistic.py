from rich.console import Console
from rich.table import Table
from team import Team


class Statistic:

    def __init__(self, first_team: Team, second_team: Team):
        self.first_team = self.set_team_stats(team=first_team)
        self.second_team = self.set_team_stats(team=second_team)
        self.teams = [self.first_team, self.second_team]

    def set_team_stats(self, team: Team):
        return {
            'name': team.name,
            'survived': len(team.characters),
            'caused_damage': 0
        }

    def update(self, name: str, damage: int | None = None, is_victim_dead: bool = False):
        team = self.get_team_by_name(name=name)
        if damage is not None:
            team['caused_damage'] += damage
        if is_victim_dead:
            team['survived'] -= 1

    def get_team_by_name(self, name: str):
        for team in self.teams:
            if name == team['name']:
                return team

    def show_stats(self):
        table = Table(title="Statistics")

        table.add_column("Team", justify="left", style="cyan")
        table.add_column("Caused damage", justify="center", style="magenta")
        table.add_column("Survived", justify="center", style="green")

        for team in self.teams:

            table.add_row(
                team['name'],
                str(team['caused_damage']),
                str(team['survived'])
            )

        console = Console()
        console.print(table)
