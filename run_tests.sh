#!/bin/bash

echo "----------------------------------------------------------"
echo "Clustering with Integer Linear Programming"
echo "Unit Distance in the Grid ~ 1.17 km"
echo "Model will be run for the following coverage distances;"
echo "-  7 units  ~  8.5  km"
echo "-  9 units  ~ 10.5  km"
echo "- 11 units  ~ 13.0  km"
echo "- 13 units  ~ 15.25 km"
echo "- 15 units  ~ 17.5  km"
echo "----------------------------------------------------------"

for DISTANCE_THRESHOLD in 7 9 11 13 15
do
    echo "----------------------------------------------------------"
    echo "Model is running for the coverage distance = $DISTANCE_THRESHOLD units"
    echo "----------------------------------------------------------"
    python main.py --distance_threshold=$DISTANCE_THRESHOLD
done