import argparse

from structs import Grid
from functions import clustering
from functions import helpers
from functions import logger
from functions import preprocessing
from functions import visualizer


parser = argparse.ArgumentParser(description='ILP Sensor Clustering - Clustering of sensors using Integer Linear Programming concept')
parser.add_argument('--size', required=False, default=100, type=int)
parser.add_argument('--sensor_count', required=False, default=75, type=int)
parser.add_argument('--distance_threshold', required=False, default=13, type=int)


args = vars(parser.parse_args())
GRID_SIZE = args['size']
SENSOR_COUNT = args['sensor_count']
DISTANCE_THRESHOLD = args['distance_threshold']


if __name__=='__main__':
    # ___Random Initializing___
    #grid = Grid(GRID_SIZE)
    #sensor_set = preprocessing.generate_random_sensors(GRID_SIZE, SENSOR_COUNT, MAX_SCORE, MIN_SCORE)
    
    # ___Initializing Through File___
    grid = Grid(GRID_SIZE)
    sensor_set = preprocessing.init_sensors_from_file('docs/input/sensor_locations.tsv')
    preprocessing.set_sensor_scores(sensor_set, 'docs/input/sensor_placements.csv')
    preprocessing.normalize_sensor_locations(sensor_set, GRID_SIZE)

    # ___Building The Model___
    generated_model, gateway_locations = clustering.generate_model(grid)

    # ___Developing The Model___
    developed_model = clustering.develop_model(generated_model, grid, sensor_set, gateway_locations, DISTANCE_THRESHOLD)

    # ___Optimizing The Model___
    gateway_set = clustering.optimize_model(developed_model, grid, gateway_locations)

    # ___Connecting Sensors and Gateways___
    helpers.connect_nodes(sensor_set, gateway_set, DISTANCE_THRESHOLD)

    # ___Logging___
    logger.record_nodes(sensor_set, 'docs/output/log/_sensors.txt')
    logger.record_nodes(gateway_set, f'docs/output/log/{DISTANCE_THRESHOLD}_units_distance_gateways.txt')

    # ___Visualization___
    visualizer.show_locations("Sensor", sensor_set, grid, 'docs/output/img/_sensor_placement.png')
    #visualizer.show_locations("Gateway", gateway_set, grid, f'docs/output/img/{DISTANCE_THRESHOLD}_units_distance_gateway_placement.png')
    visualizer.show_grid(sensor_set, gateway_set, grid, DISTANCE_THRESHOLD, f'docs/output/img/{DISTANCE_THRESHOLD}_units_distance_grid.png')
