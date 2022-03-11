import argparse

from structs import Grid
from functions import helpers
from functions import clustering

parser = argparse.ArgumentParser(description='ILP Sensor Clustering - Clustering of sensors using Integer Linear Programming concept')
parser.add_argument('--size', required=False, default=100, type=int)
parser.add_argument('--sensor_count', required=False, default=75, type=int)
parser.add_argument('--distance_threshold', required=False, default=15, type=float)

args = vars(parser.parse_args())
GRID_SIZE = args['size']
SENSOR_COUNT = args['sensor_count']
DISTANCE_THRESHOLD = args['distance_threshold']

if __name__=='__main__':
    # ___Initialization___
    grid = Grid(GRID_SIZE)
    sensor_set = helpers.generate_sensors(GRID_SIZE, SENSOR_COUNT)

    # ___Building___
    generated_model, gateway_locations = clustering.generate_model(grid=grid)

    # ___Developing___
    developed_model = clustering.develop_model(
        model=generated_model,
        grid=grid,
        sensor_set=sensor_set,
        gateway_locations=gateway_locations,
        distance_threshold=DISTANCE_THRESHOLD
    )

    # ___Running___
    optimized_model, gateway_locations = clustering.optimize_model(
        model=developed_model,
        grid=grid,
        gateway_locations=gateway_locations
    )

    # ___Visualization And Logging___
    helpers.record_sensor_locations(sensor_set)
    helpers.record_gateway_locations(grid, gateway_locations)
    helpers.show_sensor_locations(grid, sensor_set)
    helpers.show_gateway_locations(grid, gateway_locations)
    helpers.show_grid(grid, sensor_set, gateway_locations, DISTANCE_THRESHOLD)
