import numpy as np
import mip.model
import mip.constants

from structs import Grid, Gateway
from . import helpers


def generate_model(grid:Grid) -> tuple:
    """
        Description:
            Generates a model and the variable matrices
            which will be used for optimizing

        Arguments:
            - grid : `Grid` grid that the sensors are located on

        Return:
            - `mip.model.Model` : raw model
            - `list` : locations that are proper for placing the gateway
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
    """
        Description:
            Develops the model by adding objectives and
            constraints which are the key part of the
            optimization problem

        Arguments:
            - model : `mip.model.Model` model to develop
            - grid : `Grid` grid that the nodes are located on
            - gateway_locations : `list` locations that are proper
            for placing the gateway
            - distance_threshold : `int` upper limit of distance
            between nodes so that can communicate

        Return:
            - `mip.model.Model` : model that is developed by objectives
            and constraints
    """

    model.objective = mip.model.minimize(
        mip.model.xsum([
            gateway_locations[gateway_y][gateway_x] * (0 < helpers.calculate_distance(
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
            gateway_locations[gateway_y][gateway_x] * (0 < helpers.calculate_distance(
                (sensor_x, sensor_y), (gateway_x, gateway_y)
            ) <= distance_threshold)
            for gateway_x in grid.get_width_as_range()
            for gateway_y in grid.get_height_as_range()
        ]) >= 1

    return model


def optimize_model(model:mip.model.Model, grid:Grid, gateway_locations:list) -> set:
    """
        Description:
            Optimizes the model, then generates gateway objects
            which are placed on the optimum locations
        
        Arguments:
            - model : `mip.model.Model` model to optimize
            - grid : `Grid` grid that the nodes are located on
            - gateway_locations : `list` locations that are proper
            for placing the gateway

        Return:
            - `set` : set storing the gateway objects
    """
    gateway_set = set()
    model.optimize()
    if model.num_solutions:
        for gateway_y in grid.get_height_as_range():
            for gateway_x in grid.get_width_as_range():
                if gateway_locations[gateway_y][gateway_x].x == 1:
                    new_gateway = Gateway(
                        id=str(gateway_x)+str(gateway_y),
                        x=gateway_x,
                        y=gateway_y)
                    gateway_set.add(new_gateway)        
    
    return gateway_set
