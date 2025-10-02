import numpy as np

class MatchupSimulator:
    def __init__(self, teams, projections):
        self.teams = teams
        self.projections = projections.set_index("Player")

    def simulate(self, team_a: int, team_b: int):
        stats_a = self._team_stats(self.teams[team_a])
        stats_b = self._team_stats(self.teams[team_b])

        categories = stats_a.keys()
        wins_a, wins_b = 0, 0

        for cat in categories:
            if stats_a[cat] > stats_b[cat]:
                wins_a += 1
            elif stats_b[cat] > stats_a[cat]:
                wins_b += 1

        return {"Team A Wins": wins_a, "Team B Wins": wins_b}

    def _team_stats(self, players):
        subset = self.projections.loc[players]
        return subset.drop(columns=["Player"]).mean().to_dict()
