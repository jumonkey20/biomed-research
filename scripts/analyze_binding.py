import pandas as pd

def rank_candidates(scores_file="data/processed/docking_results.csv"):
    """Ranks drug treatment candidates by lowest binding energy (kcal/mol)."""
    try:
        df = pd.read_csv(scores_file)
        ranked = df.sort_values(by="binding_energy_kcal_mol", ascending=True)
        print("--- Top Drug Candidates ---")
        print(ranked.head())
        ranked.to_csv("results/tables/top_candidates.csv", index=False)
    except FileNotFoundError:
        print(f"File {scores_file} not found. Run docking simulations first.")

if __name__ == "__main__":
    rank_candidates()
