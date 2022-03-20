#!/bin/bash

for DISTANCE_THRESHOLD in 9 11 13 15
do
    echo "------------------------------------"
    echo "Optimization is running..."
    echo "distance_threshold = $DISTANCE_THRESHOLD"
    echo "------------------------------------"
    python main.py --distance_threshold=$DISTANCE_THRESHOLD
done