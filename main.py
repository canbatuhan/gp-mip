from email.policy import default
import os
import argparse

from structs import Grid
from functions import preprocess as pproc
from functions import clustering

parser = argparse.ArgumentParser(description='ILP Sensor Clustering - Clustering of sensors using Integer Linear Programming concept')
parser.add_argument('--size', required=False, default=None, type=int)
parser.add_argument('--sensor_count', required=False, default=75, type=int)

args = vars(parser.parse_args())
GRID_SIZE = args['size']
SENSOR_COUNT = args['sensor_count']

if __name__=='__main__':
    grid = Grid(GRID_SIZE)
    sensors = pproc.generate_sensors(GRID_SIZE, SENSOR_COUNT)
    # pproc.record_sensor_locations(sensors)
    # pproc.show_sensor_locations(grid, sensors)
    model_package = clustering.generate_model(grid, sensors)
