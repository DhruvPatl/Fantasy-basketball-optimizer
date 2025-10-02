import pandas as pd
from optimizer.draft import DraftSimulator
from optimizer.matchup import MatchupSimulator

def main():
    # Load projections (replace with real data later)
    projections = pd.DataFrame({
        "Player": ["Jokic", "SGA", "Luka", "Tatum", "Giannis",
                   "Haliburton", "Curry", "Edwards", "AD", "KD"],
        "PTS": [26, 31, 33, 28, 30, 21, 29, 25, 24, 27],
        "REB": [12, 5, 9, 8, 11, 4, 5, 6, 12, 6],
        "AST": [8, 6, 9, 5, 6, 11, 6, 4, 3, 5],
        "STL": [1.2, 2.0, 1.3, 1.0, 1.1, 1.5, 0.9, 1.3, 1.2, 0.7],
        "BLK": [0.8, 0.7, 0.5, 0.6, 1.0, 0.4, 0.2, 0.5, 2.5, 0.8],
    })

    # Draft simulation
    draft = DraftSimulator(projections, num_teams=8, rounds=3)
    teams = draft.run_draft()

    print("Draft Results:")
    for i, t in enumerate(teams):
        print(f"Team {i+1}: {t}")

    # Matchup simulation
    matchup = MatchupSimulator(teams, projections)
    result = matchup.simulate(0, 1)

    print("\nMatchup Result (Team 1 vs Team 2):")
    print(result)

if __name__ == "__main__":
    main()
