#!/bin/bash

# Get the day number from the command line argument
DAY_NUM=$1

# Pad with leading zero if necessary
DAY_PADDED=$(printf "%02d" "$DAY_NUM")

echo "Creating directory for Day $DAY_PADDED..."

# Create the directory
mkdir -p "day$DAY_PADDED"

# Create the input files
touch "day$DAY_PADDED/sample.txt"
touch "day$DAY_PADDED/full.txt"

# Create the jupyter notebook
touch "day$DAY_PADDED/code.ipynb"

# Link the common utility script
ln -s "../common/utils.py" "day$DAY_PADDED/utils.py"
