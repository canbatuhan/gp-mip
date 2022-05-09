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

    for TOP_N_SENSORS in 10 15 20 25 30
    do
        echo "----------------------------------------------------------"
        echo "Model is running for the following parameters"
        echo "Coverage Distance = $DISTANCE_THRESHOLD kilometers"
        echo "Considering the Top $TOP_N_SENSORS Sensors"
        echo "----------------------------------------------------------"
        python main.py --distance_threshold=$DISTANCE_THRESHOLD --top_n_sensors=$TOP_N_SENSORS
        echo ""
    done

    DISTANCE_THRESHOLD=$((DISTANCE_THRESHOLD+1))
done