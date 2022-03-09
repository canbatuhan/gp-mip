import numpy as np
import mip.model
import mip.constants

from structs import Grid, Sensor


def calculate_distance(point1:tuple, point2:tuple) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)


def sensors_covered(gateway_point:tuple, sensor_set:set, distance_threshold:float) -> set:
    covered_sensor_set = set()
    for sensor in sensor_set:
        distance = calculate_distance(gateway_point, (sensor.get_x(), sensor.get_y()))
        if distance <= distance_threshold:
            covered_sensor_set.add(sensor)
    return covered_sensor_set


def generate_model(grid:Grid, sensor_set:set, distance_threshold:float) -> dict:
    """
        Description:
            Generates a model and the variable matrices
            which will be used for optimizing

        Arguments:
            - grid : `Grid` grid that the sensors are located on
            - sensor_set : `set` array storing the sensors
            - distance_threshold : `float` thershold value for the distance
            between the gateway and a sensor

        Return:
            - `dict` : package storing the model and
            the model variables
    """
    # Creating empty model
    model = mip.model.Model()

    # Creating all possible gateway locations
    # with the data of covered sensors
    covered_sensors = [
        [
            sensors_covered(
                gateway_point=(x, y),
                sensor_set=sensor_set,
                distance_threshold=distance_threshold
            ) for y in grid.get_width_as_range()
        ] for x in grid.get_height_as_range()
    ]

    # Creating an array to indicate that
    # a location is suitable for placing gateway 
    gateway_locations = [
        [
            model.add_var(
                var_type=mip.constants.BINARY
            ) for _ in grid.get_width_as_range()
        ] for _ in grid.get_height_as_range()
    ]

    return model, covered_sensors, gateway_locations


def develop_model(model:mip.model.Model, grid:Grid, sensor_set:set, covered_sensors:list, gateway_locations:list) -> mip.model.Model:
    model.objective = mip.model.minimize(
        objective=mip.model.xsum(
            gateway_locations[row][col] for col in grid.get_width_as_range() for row in grid.get_height_as_range()
        )
    )

    model += mip.model.xsum(
        covered_sensors[row][col] for col in grid.get_width_as_range() for row in grid.get_height_as_range()
    ) == sensor_set

    return model


def optimize_model(model:mip.model.Model, grid:Grid, sensor_set:set, covered_sensors:list, gateway_locations:list) -> mip.model.Model:
    model.optimize()
    if model.num_solutions:
        print("FOUND")
