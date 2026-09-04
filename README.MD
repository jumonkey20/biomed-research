# Structural Modeling of Disease-Associated Proteins and Therapeutic Screening

## Overview
This repository focuses on modeling structural changes in disease-target proteins and evaluating potential treatment compounds. It includes pipelines for retrieving structural coordinates, running molecular docking/binding simulations, and evaluating binding affinity scores across drug candidates.

## Repository Layout
- `data/pdb_structures/`: PDB/cIF coordinate files for target proteins and disease mutants.
- `data/ligands/`: Chemical library/treatment compound structures.
- `scripts/`: Automated pipelines for fetching structures, running docking programs, and analyzing binding residue interactions.
- `notebooks/`: Jupyter Notebooks for interactive data exploration and binding affinity visualizations.
- `visualization/`: PyMOL scripts/sessions to visualize binding pockets and drug-protein interaction interfaces.
- `results/`: Binding energy tables, affinity rankings, and figure outputs.

## Getting Started
### Prerequisites
- **Python** (>= 3.9)
- Key packages: `biopython`, `pypdb`, `pandas`, `matplotlib`, `seaborn`
- External Tools: PyMOL / UCSF ChimeraX, AutoDock Vina (or preferred docking engine)

### Usage
1. Fetch target PDB structures:
   ```bash
   python scripts/fetch_pdb.py --pdb_id 1ABC
