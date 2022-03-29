#!/bin/bash

echo "----------------------------------------------------------"
echo "Clustering with Integer Linear Programming"
echo "Unit Distance in the Grid ~ 1.17 km"
echo "----------------------------------------------------------"
echo ""

for DISTANCE_THRESHOLD in 1 2 3 4 5 6 7 8 9 10
do
    echo "----------------------------------------------------------"
    echo "Model is running for the coverage distance = $DISTANCE_THRESHOLD km"
    echo "----------------------------------------------------------"
    python main.py --distance_threshold=$DISTANCE_THRESHOLD
    echo ""
done