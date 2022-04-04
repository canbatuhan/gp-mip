import argparse

from structs import Grid
from functions import preprocessing
from functions import clustering
from functions import postprocessing
from functions import visualizer

parser = argparse.ArgumentParser(description='ILP Sensor Clustering - Clustering of sensors using Integer Linear Programming concept')
parser.add_argument('--distance_threshold', required=False, default=10.0, type=float)
parser.add_argument('--score_threshold', required=False, default=0.15, type=float)
parser.add_argument('--top_n_sensors', required=False, default=15, type=int)

# Parsing Arguments
args = vars(parser.parse_args())
GRID_SIZE = 100
DISTANCE_THRESHOLD_KM = args['distance_threshold']
DISTANCE_THRESHOLD = args['distance_threshold']/1.17 # km to unit ditance (for 100x100 grid)
SCORE_THRESHOLD = args['score_threshold']
TOP_N_SENSORS = args['top_n_sensors']

# File Paths
SENSOR_PLACEMENT_PATH = 'docs/output/img/_sensor_placement.png'
GRID_PATH = f'docs/output/img/{int(DISTANCE_THRESHOLD_KM)}_km_coverage_grid.png'
SENSOR_LOG_PATH_UNIT = 'docs/output/log_unit/_sensors_unit.txt'
GATEWAY_LOG_PATH_UNIT = f'docs/output/log_unit/{int(DISTANCE_THRESHOLD_KM)}_km_coverage_gateways_unit.txt'
SENSOR_LOG_PATH_COOR = 'docs/output/log_coor/_sensors_coor.txt'
GATEWAY_LOG_PATH_COOR = f'docs/output/log_coor/{int(DISTANCE_THRESHOLD_KM)}_km_coverage_gateways_unit.txt'

# Main Program
if __name__=='__main__':
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
    visualizer.show_locations("Sensor", sensor_set, grid, SENSOR_PLACEMENT_PATH)
    #visualizer.show_locations("Gateway", gateway_set, grid, f'docs/output/img/{DISTANCE_THRESHOLD}_units_distance_gateway_placement.png')
    visualizer.show_grid(TOP_N_SENSORS, sensor_set, gateway_set, grid, DISTANCE_THRESHOLD, GRID_PATH)

    # ___Post-processing___
    postprocessing.connect_nodes(sensor_set, gateway_set, DISTANCE_THRESHOLD)
    postprocessing.set_gateway_elevations(gateway_set)
    postprocessing.record_nodes(sensor_set, SENSOR_LOG_PATH_UNIT)
    postprocessing.gateway_with_top_sensors(TOP_N_SENSORS, sensor_set, gateway_set, GATEWAY_LOG_PATH_UNIT)

    # __Denormalizing___
    postprocessing.denormalize_locations(sensor_set, gateway_set, GRID_SIZE, extreme_longitude, extreme_latitude)
    postprocessing.record_nodes(sensor_set, SENSOR_LOG_PATH_COOR)
    postprocessing.gateway_with_top_sensors(TOP_N_SENSORS, sensor_set, gateway_set, GATEWAY_LOG_PATH_COOR)
