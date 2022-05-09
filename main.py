import argparse
import math

from structs import Grid
from functions import preprocessing, clustering, postprocessing, visualizer

parser = argparse.ArgumentParser(description='ILP Sensor Clustering - Clustering of sensors using Integer Linear Programming concept')
parser.add_argument('--grid_size', required=False, default=100, type=int)
parser.add_argument('--distance_threshold', required=False, default=10.0, type=float)
parser.add_argument('--score_threshold', required=False, default=0.15, type=float)
parser.add_argument('--top_n_sensors', required=False, default=15, type=int)

# Parsing Arguments
args = vars(parser.parse_args())
MAX_DISTANCE = 165 # km
GRID_SIZE = args['grid_size']
DISTANCE_THRESHOLD_KM = args['distance_threshold']
DISTANCE_THRESHOLD = args['distance_threshold']/(MAX_DISTANCE/(GRID_SIZE*math.sqrt(2))) # km to unit distance
SCORE_THRESHOLD = args['score_threshold']
TOP_N_SENSORS = args['top_n_sensors']

# Input File Paths
SENSOR_LOCATIONS_INPUT = 'docs/input/sensor_locations.tsv'
SENSOR_SCORES_INPUT = 'docs/input/sensor_placements.csv'

# Output File Paths
SENSOR_LOCATIONS_PATH = 'docs/output/gateway_placements_visualizations/_sensor_locations.png'
GATEWAY_PLACEMENTS_PATH = f'docs/output/gateway_placements_visualizations/top_{TOP_N_SENSORS}_sensors/{int(DISTANCE_THRESHOLD_KM)}_km_coverage_gateway_placements.png'
SENSOR_LOCATIONS_UNITS_PATH = 'docs/output/gateway_placements_units/_sensor_locations_units.txt'
GATEWAY_PLACEMENTS_UNITS_PATH = f'docs/output/gateway_placements_units/top_{TOP_N_SENSORS}_sensors/{int(DISTANCE_THRESHOLD_KM)}_km_coverage_gateway_placements.txt'
SENSOR_LOCATIONS_COOR_PATH = 'docs/output/gateway_placements_coordinates/_sensor_locations_coordinates.txt'
GATEWAY_PLACEMENTS_COOR_PATH = f'docs/output/gateway_placements_coordinates/top_{TOP_N_SENSORS}_sensors/{int(DISTANCE_THRESHOLD_KM)}_km_coverage_gateway_placements.txt'

# Main Program
if __name__=='__main__':
    # ___Pre-processing___
    grid = Grid(GRID_SIZE)
    sensor_set = preprocessing.init_sensors_from_file(SENSOR_LOCATIONS_INPUT)
    preprocessing.set_sensor_scores(sensor_set, SENSOR_SCORES_INPUT)
    extreme_longitude, extreme_latitude = preprocessing.normalize_sensor_locations(sensor_set, GRID_SIZE)

    # ___Optimization___
    generated_model, gateway_locations = clustering.generate_model(grid)
    developed_model = clustering.develop_model(generated_model, grid, sensor_set, gateway_locations, DISTANCE_THRESHOLD, SCORE_THRESHOLD)
    gateway_set = clustering.optimize_model(developed_model, grid, gateway_locations)
    
    # ___Visualization___
    visualizer.show_sensor_locations(TOP_N_SENSORS, sensor_set, grid, SENSOR_LOCATIONS_PATH)
    visualizer.show_gateway_placements(TOP_N_SENSORS, sensor_set, gateway_set, grid, DISTANCE_THRESHOLD, GATEWAY_PLACEMENTS_PATH)

    # ___Post-processing___
    postprocessing.connect_nodes(sensor_set, gateway_set, DISTANCE_THRESHOLD)
    postprocessing.set_gateway_elevations(gateway_set)
    postprocessing.record_nodes(sensor_set, SENSOR_LOCATIONS_UNITS_PATH)
    postprocessing.gateway_with_top_sensors(TOP_N_SENSORS, sensor_set, gateway_set, GATEWAY_PLACEMENTS_UNITS_PATH)

    # ___Denormalizing___
    postprocessing.denormalize_locations(sensor_set, gateway_set, GRID_SIZE, extreme_longitude, extreme_latitude)
    postprocessing.record_nodes(sensor_set, SENSOR_LOCATIONS_COOR_PATH)
    postprocessing.gateway_with_top_sensors(TOP_N_SENSORS, sensor_set, gateway_set, GATEWAY_PLACEMENTS_COOR_PATH)
