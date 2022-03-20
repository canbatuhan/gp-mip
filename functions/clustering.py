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
            - sensor_set : `set` set storing the `Sensor` nodes
            - gateway_locations : `list` locations that are proper
            for placing the gateway
            - distance_threshold : `int` upper limit of distance
            between nodes so that can communicate

        Return:
            - `mip.model.Model` : model that is developed by objectives
            and constraints
    """
    distance_condition = lambda x1, y1, x2, y2 : 0 <= helpers.calculate_distance(
            (x1, y1), (x2, y2)
        ) <= distance_threshold

    neg_avg_score_condition = lambda x1, y1, set : not helpers.calculate_avg_score(
            (x1, y1), set, distance_threshold
        ) >= 0.25

    # Aim is to minimize the total number of gateways
    # covering the sensors placed on the grid
    model.objective = mip.model.minimize(
        mip.model.xsum(
            gateway_locations[gateway_y][gateway_x] * int(distance_condition(
                sensor.get_x(), sensor.get_y(), gateway_x, gateway_y))
            for gateway_x in grid.get_width_as_range()
            for gateway_y in grid.get_height_as_range()
            for sensor in sensor_set))

    # A constraint for the model is that a sensor must be
    # covered by at least 1 gateway
    for sensor in sensor_set:
        model.add_constr(mip.model.xsum(
            gateway_locations[gateway_y][gateway_x] * int(distance_condition(
                sensor.get_x(), sensor.get_y(), gateway_x, gateway_y))
            for gateway_x in grid.get_width_as_range()
            for gateway_y in grid.get_height_as_range()) >= 1)

    # A constraint for the model is that the average score
    # of the sensors covered by the same gateway should
    # be at least 4 (maximum : 10)
    model.add_constr(mip.model.xsum(
        gateway_locations[gateway_y][gateway_x] * int(neg_avg_score_condition(
            gateway_x, gateway_y, sensor_set))
        for gateway_x in grid.get_width_as_range()
        for gateway_y in grid.get_height_as_range()) == 0)

    return model


def optimize_model(model:mip.model.Model, grid:Grid, gateway_locations:list) -> set:
    """
        Description:
            Optimizes the model, then generates `Gateway` objects
            which are placed on the optimum locations
        
        Arguments:
            - model : `mip.model.Model` model to optimize
            - grid : `Grid` grid that the nodes are located on
            - gateway_locations : `list` locations that are proper
            for placing the gateway

        Return:
            - `set` : set storing the `Gateway` nodes
    """
    gateway_set = set()
    model.optimize()

    if model.num_solutions:
        gateway_id = 0
        for gateway_y in grid.get_height_as_range():
            for gateway_x in grid.get_width_as_range():
                if gateway_locations[gateway_y][gateway_x].x == 1:
                    new_gateway = Gateway(
                        id=str(gateway_id),
                        x=gateway_x,
                        y=gateway_y)
                    gateway_set.add(new_gateway)
                    gateway_id += 1      
    
    return gateway_set
