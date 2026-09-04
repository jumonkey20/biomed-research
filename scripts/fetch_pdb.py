import sys
import os
from Bio.PDB import PDBList

def download_structure(pdb_id, output_dir="data/pdb_structures"):
    """Downloads a PDB structure file into the data directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    pdbl = PDBList()
    pdbl.retrieve_pdb_file(pdb_id, pdir=output_dir, file_format="mmCif")
    print(f"Structure {pdb_id} downloaded successfully to {output_dir}.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "1TUP"  # Example: P53 cancer mutant
    download_structure(target)
