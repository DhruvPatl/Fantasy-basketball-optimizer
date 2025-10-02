import pandas as pd
import numpy as np

class DraftSimulator:
    def __init__(self, projections: pd.DataFrame, num_teams: int = 8, rounds: int = 5):
        self.projections = projections
        self.num_teams = num_teams
        self.rounds = rounds
        self.teams = [[] for _ in range(num_teams)]

    def run_draft(self):
        available = self.projections.copy()

        for rnd in range(self.rounds):
            for pick in range(self.num_teams):
                idx = rnd * self.num_teams + pick
                if idx >= len(available):
                    break
                player = available.iloc[idx]
                self.teams[pick].append(player["Player"])
        return self.teams
