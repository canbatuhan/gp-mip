import numpy as np


def calculate_distance(point1:tuple, point2:tuple) -> int:
    """
        Description:
            Calculates the distance between two points

        Arguments:
            - point1 : `tuple` first point
            - point2 : `tuple` second point

        Returns:
            - `int` : ceil integer of the calculated
            (float) distance
    """
    x1, y1 = point1
    x2, y2 = point2
    return int(np.ceil(np.sqrt((x1-x2)**2 + (y1-y2)**2)))
    

def calculate_avg_score(gateway_point:tuple, sensor_set:set, distance_threshold:int) -> float:
    """
        Description:
            Calculates the average score of the sensors
            covered by a `Gateway`

        Arguments:
            - gateway_point : `tuple` location of the `Gateway`
            - sensor_set : `set` set storing `Sensor` nodes
            - distance_threshold : `int` upper limit of distance
            between nodes so that can communicate

        Return:
            - `float` : average score of `Sensor` nodes
    """
    total_score = 0
    n_sensor_covered = 0
    for sensor in sensor_set:
        covers = calculate_distance(
            gateway_point,
            (sensor.get_x(), sensor.get_y())
        ) <= distance_threshold
        if covers:
            total_score = total_score + sensor.get_score()
            n_sensor_covered += 1
    
    if n_sensor_covered == 0: return 0
    else: return total_score/n_sensor_covered


def connect_nodes(sensor_set:set, gateway_set:set, distance_threshold:int) -> None:
    """
        Description:
            Connects the `Sensor` objects and `Gateway` objects
            with each other to analyse the model performance

        Argunments:
            - sensor_set : `set` set storing the `Sensor` nodes
            - gateway_set : `set` set stroing the `Gateway` nodes
            - distance_threshold : `int` upper limit of distance
            between nodes so that can communicate
    """
    for sensor in sensor_set:
        sensor.find_covered_gateways(gateway_set, distance_threshold)
    
    for gateway in gateway_set:
        gateway.find_covered_sensors(sensor_set, distance_threshold)
