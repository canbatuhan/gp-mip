from email.policy import default
import os
import argparse

from structs import Grid
from functions import preprocess as pproc
from functions import clustering

parser = argparse.ArgumentParser(description='ILP Sensor Clustering - Clustering of sensors using Integer Linear Programming concept')
parser.add_argument('--size', required=False, default=100, type=int)
parser.add_argument('--sensor_count', required=False, default=25, type=int)
parser.add_argument('--distance_threshold', required=False, default=150.0, type=float)

args = vars(parser.parse_args())
GRID_SIZE = args['size']
SENSOR_COUNT = args['sensor_count']
DISTANCE_THRESHOLD = args['distance_threshold']

if __name__=='__main__':
    # ___Initialization___
    grid = Grid(GRID_SIZE)
    sensor_set = pproc.generate_sensors(GRID_SIZE, SENSOR_COUNT)

    # ___Visualization___
    pproc.record_sensor_locations(sensor_set)
    pproc.show_sensor_locations(grid, sensor_set)

    # ___Building___
    generated_model, covered_sensors, gateway_locations = clustering.generate_model(
        grid=grid,
        sensor_set=sensor_set,
        distance_threshold=DISTANCE_THRESHOLD
    )

    developed_model = clustering.develop_model(
        model=generated_model,
        grid=grid,
        sensor_set=sensor_set,
        covered_sensors=covered_sensors,
        gateway_locations=gateway_locations
    )

    optimized_model = clustering.optimize_model(
        model=developed_model,
        grid=grid,
        sensor_set=sensor_set,
        covered_sensors=covered_sensors,
        gateway_locations=gateway_locations
    )
