import numpy as np
import mip.model
import mip.constants

from structs import Grid


def calculate_distance(point1:tuple, point2:tuple) -> int:
    x1, y1 = point1
    x2, y2 = point2
    return int(np.sqrt((x1-x2)**2 + (y1-y2)**2))


def generate_model(grid:Grid) -> tuple:
    """
        Description:
            Generates a model and the variable matrices
            which will be used for optimizing

        Arguments:
            - grid : `Grid` grid that the sensors are located on

        Return:
            - `mip.Model` : raw model
            - `list` : list storing the model variables, representing the
            gateway location
    """
    # Creating an empty model
    model = mip.model.Model()

    # Creating an array to indicate that
    # a location is suitable for placing gateway 
    gateway_locations = [
        [
            model.add_var(
                var_type=mip.constants.BINARY
            ) for _ in grid.get_width_as_range()
        ] for _ in grid.get_height_as_range()
    ]

    return model, gateway_locations


def develop_model(model:mip.model.Model, grid:Grid, sensor_set:set, gateway_locations:list, distance_threshold:int) -> mip.model.Model:
    """model.objective = mip.model.minimize(
        objective=mip.model.xsum(
            gateway_locations[row][col] for col in grid.get_width_as_range() for row in grid.get_height_as_range()
        )
    )"""

    model.objective = mip.model.minimize(
        mip.model.xsum([
            gateway_locations[gateway_y][gateway_x] * (0 < calculate_distance(
                (sensor.get_x(), sensor.get_y()), (gateway_x, gateway_y)
            ) <= distance_threshold)
            for gateway_y in grid.get_height_as_range()
            for gateway_x in grid.get_width_as_range()
            for sensor in sensor_set
        ])
    )

    for sensor in sensor_set:
        sensor_x, sensor_y = sensor.get_x(), sensor.get_y()
        model += mip.model.xsum([
            gateway_locations[gateway_y][gateway_x] * (0 < calculate_distance(
                (sensor_x, sensor_y), (gateway_x, gateway_y)
            ) <= distance_threshold)
            for gateway_x in grid.get_width_as_range()
            for gateway_y in grid.get_height_as_range()
        ]) >= 1

    return model


def optimize_model(model:mip.model.Model, grid:Grid, gateway_locations:list) -> tuple:
    model.optimize()
    if model.num_solutions:
        for y in grid.get_height_as_range():
            for x in grid.get_width_as_range():
                if gateway_locations[y][x].x == 1:
                    print('Gateway Location: {}, {}'.format(x, y))
    
    return model, gateway_locations
