import argparse
import math

from structs import Grid
from functions import preprocessing, clustering, postprocessing, visualizer
from settings import * # Importing File paths

parser = argparse.ArgumentParser(description='ILP Sensor Clustering - Clustering of sensors using Integer Linear Programming concept')
parser.add_argument('--grid_size', required=False, default=100, type=int)
parser.add_argument('--distance_threshold', required=False, default=10.0, type=float)
parser.add_argument('--score_threshold', required=False, default=0.15, type=float)

# Parsing Arguments
args = vars(parser.parse_args())
MAX_DISTANCE = 165 # km
GRID_SIZE = args['grid_size']
DISTANCE_THRESHOLD_KM = args['distance_threshold']
DISTANCE_THRESHOLD = args['distance_threshold']/(MAX_DISTANCE/(GRID_SIZE*math.sqrt(2))) # km to unit distance
SCORE_THRESHOLD = args['score_threshold']

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
    visualizer.show_sensor_locations(sensor_set, grid, SENSOR_LOCATIONS_PATH)
    for top_n_sensors in range(5, 35, 5):
        file_path = GATEWAY_PLACEMENTS_PATH(top_n_sensors, DISTANCE_THRESHOLD_KM)
        visualizer.show_gateway_placements(top_n_sensors, sensor_set, gateway_set, grid, DISTANCE_THRESHOLD, file_path)


    # ___Post-processing___
    postprocessing.connect_nodes(sensor_set, gateway_set, DISTANCE_THRESHOLD)
    postprocessing.set_gateway_elevations(gateway_set)
    postprocessing.record_sensor_locations(sensor_set, SENSOR_LOCATIONS_UNITS_PATH)

    for top_n_sensors in range(5, 35, 5):
        file_path = GATEWAY_PLACEMENTS_UNITS_PATH(top_n_sensors, DISTANCE_THRESHOLD_KM)
        postprocessing.record_gateway_placements(top_n_sensors, sensor_set, gateway_set, file_path)

    file_path = ALL_GATEWAY_PLACEMENTS_UNITS_PATH(DISTANCE_THRESHOLD_KM)
    postprocessing.record_gateway_placements(len(sensor_set), sensor_set, gateway_set, file_path)


    # ___Denormalizing___
    postprocessing.denormalize_locations(sensor_set, gateway_set, GRID_SIZE, extreme_longitude, extreme_latitude)
    postprocessing.record_sensor_locations(sensor_set, SENSOR_LOCATIONS_COOR_PATH)

    for top_n_sensors in range(5, 35, 5):
        file_path = GATEWAY_PLACEMENTS_COOR_PATH(top_n_sensors, DISTANCE_THRESHOLD_KM)
        postprocessing.record_gateway_placements(top_n_sensors, sensor_set, gateway_set, file_path)
    
    file_path = ALL_GATEWAY_PLACEMENTS_COOR_PATH(DISTANCE_THRESHOLD_KM)
    postprocessing.record_gateway_placements(len(sensor_set), sensor_set, gateway_set, file_path)
