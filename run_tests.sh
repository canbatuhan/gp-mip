#!/bin/bash

echo "----------------------------------------------------------"
echo "Clustering with Integer Linear Programming"
echo "Unit Distance in the Grid ~ 1.17 km"
echo "----------------------------------------------------------"
echo ""

MAX_RANGE = 10
while [ $DISTANCE_THRESHOLD -le $MAX_RANGE ]
do
    echo "----------------------------------------------------------"
    echo "Model is running for the coverage distance = $DISTANCE_THRESHOLD km"
    echo "----------------------------------------------------------"
    python main.py --distance_threshold=$DISTANCE_THRESHOLD
    echo ""

    DISTANCE_THRESHOLD = DISTANCE_THRESHOLD + 1
done