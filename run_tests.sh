#!/bin/bash

echo "----------------------------------------------------------"
echo "Clustering with Integer Linear Programming"
echo "Unit Distance in the Grid ~ 1.17 km"
echo "----------------------------------------------------------"
echo ""

DISTANCE_THRESHOLD=1
MAX_RANGE=10
while [ $DISTANCE_THRESHOLD -le $MAX_RANGE ]
do

    for TOP_N_SENSORS in 10 15 20 25 30
    do
        echo "----------------------------------------------------------"
        echo "Model is running for the following parameters"
        echo "coverage distance = $DISTANCE_THRESHOLD km"
        echo "considering top $TOP_N_SENSORS sensors"
        echo "----------------------------------------------------------"
        python main.py --distance_threshold=$DISTANCE_THRESHOLD --top_n_sensors=$TOP_N_SENSORS
        echo ""
    done

    DISTANCE_THRESHOLD=$((DISTANCE_THRESHOLD+1))
done