#!/bin/bash

echo "----------------------------------------------------------"
echo "Clustering with Mixed-Integer Programming"
echo "Unit Distance in the Grid ~ 1.17 km"
echo "----------------------------------------------------------"
echo ""

DISTANCE_THRESHOLD=1
MAX_RANGE=10
while [ $DISTANCE_THRESHOLD -le $MAX_RANGE ]
do
    echo "----------------------------------------------------------"
    echo "Model is running for the following parameters"
    echo "Coverage Distance = $DISTANCE_THRESHOLD kilometers"
    echo "----------------------------------------------------------"
    python main.py --distance_threshold=$DISTANCE_THRESHOLD &
    python base.py --distance_threshold=$DISTANCE_THRESHOLD &
    echo ""

    DISTANCE_THRESHOLD=$((DISTANCE_THRESHOLD+1))
done