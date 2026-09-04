# Biomedical Research & Molecular Docking Pipeline

## 👋 About This Project
Welcome! I am an undergraduate Biomedical Science student at the University of Surrey. This repository showcases my independent exploration into **bioinformatics and structural biology**, specifically focusing on molecular docking simulations. 

Rather than relying purely on complex terminal-based scripting, this project demonstrates a streamlined, user-friendly virtual screening workflow using **PyRx (AutoDock Vina GUI)**. Here, I investigate ligand-protein binding interactions—such as docking PRIMA-1 against target receptors like 1TUP—to analyze binding affinities and structural conformations efficiently.

---

## 📂 Repository Structure

```text
biomed-research/
├── data/
│   ├── ligands/          # Input ligand files (e.g., SDF / PDBQT)
│   ├── pdb_structures/   # Target receptor protein files (e.g., 1TUP)
│   └── processed/        # Generated docking output poses and score tables
├── results/              # Organized analysis output files
├── scripts/              # Custom automation or analysis scripts
└── README.md             # Project documentation



If you want to replicate or run this virtual screening workflow using the PyRx graphical interface, follow these steps:

1. Load Molecules
Open PyRx and navigate to the AutoDock tab.

Click Add Ligand to import your prepared ligand file (.pdbqt).

Click Add Macromolecule to import your target protein receptor file (.pdbqt, e.g., 1TUP).

2. Select Molecules for Docking
Go to the Select Molecules panel.

Check the boxes next to your target ligand and macromolecule in the Navigator tree.

Click Forward to proceed to the Vina Wizard search space setup.

3. Define the Search Space (Grid Box)
Adjust the grid box dimensions and center coordinates in the 3D viewer to cover the active binding site of your protein.

Click Forward to execute the AutoDock Vina docking calculation.

4. Analyze & Export Results
Once the progress bar completes, view the Binding Affinity (kcal/mol) table in the results panel.

Export your binding affinity scores and download your docked conformations (.sdf or .pdb) into your data/processed/ directory.
