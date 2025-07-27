#!/bin/bash
# Usage: ./openfoam_runner.sh <case_dir>
set -e
CASE_DIR=$1
cd $CASE_DIR
# Import mesh (placeholder)
echo "Importing mesh..."
# blockMesh or other mesh tool
blockMesh > log.blockMesh
# Generate grid (if needed)
# snappyHexMesh -overwrite > log.snappyHexMesh
# Simulate flow
echo "Running simulation..."
simpleFoam > log.simpleFoam
# Extract performance metrics
echo "Extracting results..."
# Example: get drag from forceCoeffs.dat
grep 'Cd' postProcessing/forceCoeffs/0/forceCoeffs.dat | tail -1 > drag.txt
# Add more post-processing as needed
echo "Done." 