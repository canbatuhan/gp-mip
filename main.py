import argparse

from structs import Grid
from functions import preprocessing
from functions import clustering
from functions import postprocessing
from functions import visualizer


parser = argparse.ArgumentParser(description='ILP Sensor Clustering - Clustering of sensors using Integer Linear Programming concept')
#parser.add_argument('--size', required=False, default=100, type=int)
#parser.add_argument('--sensor_count', required=False, default=75, type=int)
parser.add_argument('--distance_threshold', required=False, default=10.0, type=float)
parser.add_argument('--score_threshold', required=False, default=0.15, type=float)


args = vars(parser.parse_args())
#GRID_SIZE = args['size']
GRID_SIZE = 100
#SENSOR_COUNT = args['sensor_count']
DISTANCE_THRESHOLD_KM = args['distance_threshold']
DISTANCE_THRESHOLD = args['distance_threshold']/1.17 # km to unit ditance (for 100x100 grid)
SCORE_THRESHOLD = args['score_threshold']


if __name__=='__main__':
    # ___Random Initializing___
    #grid = Grid(GRID_SIZE)
    #sensor_set = preprocessing.generate_random_sensors(GRID_SIZE, SENSOR_COUNT, MAX_SCORE, MIN_SCORE)
    
    # ___Pre-processing___
    grid = Grid(GRID_SIZE)
    sensor_set = preprocessing.init_sensors_from_file('docs/input/sensor_locations.tsv')
    preprocessing.set_sensor_scores(sensor_set, 'docs/input/sensor_placements.csv')
    extreme_longitude, extreme_latitude = preprocessing.normalize_sensor_locations(sensor_set, GRID_SIZE)

    # ___Optimization___
    generated_model, gateway_locations = clustering.generate_model(grid)
    developed_model = clustering.develop_model(generated_model, grid, sensor_set, gateway_locations, DISTANCE_THRESHOLD, SCORE_THRESHOLD)
    gateway_set = clustering.optimize_model(developed_model, grid, gateway_locations)
    
    # ___Visualization___
    visualizer.show_locations("Sensor", sensor_set, grid, 'docs/output/img/_sensor_placement.png')
    #visualizer.show_locations("Gateway", gateway_set, grid, f'docs/output/img/{DISTANCE_THRESHOLD}_units_distance_gateway_placement.png')
    visualizer.show_grid(sensor_set, gateway_set, grid, DISTANCE_THRESHOLD, f'docs/output/img/{int(DISTANCE_THRESHOLD_KM)}_km_coverage_distance_grid.png')

    # ___Post-processing___
    postprocessing.connect_nodes(sensor_set, gateway_set, DISTANCE_THRESHOLD)
    postprocessing.set_gateway_elevations(gateway_set)
    postprocessing.denormalize_locations(sensor_set, gateway_set, GRID_SIZE, extreme_longitude, extreme_latitude)
    postprocessing.record_nodes(sensor_set, f'docs/output/log/_sensors.txt')
    postprocessing.record_nodes(gateway_set, f'docs/output/log/{int(DISTANCE_THRESHOLD_KM)}_km_coverage_distance_gateways.txt')
