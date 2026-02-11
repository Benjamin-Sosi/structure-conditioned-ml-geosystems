# Structure-Conditioned Machine Learning for Fractured Geosystems

This repository provides a reference implementation accompanying the manuscript:

"Structure-Conditioned Machine Learning for Fractured Geosystems:
A Computational Framework for Physically Coherent Inference"

The implementation demonstrates:

- Structural domain partitioning
- Physics-consistent feature construction
- Structure-aware learning within domains
- Convergence-based validation

## Requirements

Python 3.9 or higher.

Install dependencies using:

pip install -r requirements.txt

## Running the Quick Test

After installation, run:

python quick_test.py

The script will:

1. Load a synthetic fractured-system dataset
2. Partition data into structural regimes
3. Construct physics-consistent features
4. Train standard ML models within regimes
5. Perform convergence-based validation

If successful, the script will print validation results to the console.

## Notes

This is a minimal reference implementation intended for research reproducibility.
No proprietary software is required.
