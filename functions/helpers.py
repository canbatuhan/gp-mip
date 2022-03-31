import sys
import numpy as np


def convert_to_float(raw_data:str, sec_delim:str, min_delim:str, deg_delim:str) -> float:
    """
        Description:
            Converts the geographical data (for example, 27°16'37.9")
            to a float value
        
        Arguments:
            - raw_data : `str` geographical data
            - sec_delim : `str` delimiter char for seconds
            - min_delim : `str` delimiter char for minutes
            - deg_delim : `str` delimiter char for degrees

        Returns:
            `float` : degree value
    """
    seconds = float(raw_data.rsplit(min_delim)[-1].rsplit(sec_delim)[0])
    minutes = float(raw_data.rsplit(deg_delim)[-1].rsplit(min_delim)[0])
    degrees = float(raw_data.rsplit(deg_delim)[0])
    return degrees + minutes/60 + seconds/3600


def get_max_min_locations(sensor_set:set) -> tuple:
    """
        Description:
            Finds the maximum and minimum x and y data
            among `Sensor` objects

        Arguments:
            - sensor_set : `set` set storing the `Sensor` objects

        Returns:
            `tuple` : maximum and minimum x and y data
    """
    max_x, max_y, min_x, min_y = 0, 0, sys.maxsize, sys.maxsize

    for sensor in sensor_set:
        sensor_x, sensor_y = sensor.get_x(), sensor.get_y()
        if sensor_x > max_x: max_x = sensor_x
        elif sensor_x < min_x: min_x = sensor_x
        if sensor_y > max_y: max_y = sensor_y
        elif sensor_y < min_y: min_y = sensor_y

    return max_x, max_y, min_x, min_y


def calculate_distance(point1:tuple, point2:tuple) -> float:
    """
        Description:
            Calculates the distance between two points

        Arguments:
            - point1 : `tuple` first point
            - point2 : `tuple` second point

        Returns:
            - `float` : distance between two points
    """
    x1, y1 = point1
    x2, y2 = point2
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)
    

def calculate_avg_score(gateway_point:tuple, sensor_set:set, distance_threshold:float) -> float:
    """
        Description:
            Calculates the average score of the sensors
            covered by a `Gateway`

        Arguments:
            - gateway_point : `tuple` location of the `Gateway`
            - sensor_set : `set` set storing `Sensor` nodes
            - distance_threshold : `float` upper limit of distance
            between nodes so that can communicate

        Returns:
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


def get_top_sensors(sensor_set:set, n_sensors:int) -> set:
    """
        Description:
            Gets top `n` sensors with the highest score
            from the `Sensor` objects placed on `Grid`

        Arguments:
            - sensor_set : `set` set storing the `Sensor` nodes
            - n_sensors : `int` number of sensors to get

        Returns:
            - `set` : set of `n` sensors with the highest score
    """
    sorted_set = sorted(sensor_set, key = lambda sensor: sensor.get_score(), reverse=True)
    return sorted_set[:n_sensors]


def convert_to_coordinate(raw_data:float, sec_delim:str, min_delim:str, deg_delim:str) -> str:
    """
        Description:
            Converts converts float value to the geographical data
            (for example, 27°16'37.9")

        Arguments:
            - raw_data : `float` value as degree
            - sec_delim : `str` delimiter char for seconds
            - min_delim : `str` delimiter char for minutes
            - deg_delim : `str` delimiter char for degrees

        Returns:
            `str` : geographical data as string
    """
    degrees = int(raw_data)
    minutes_float = (raw_data-degrees)*60
    minutes = int(minutes_float)
    seconds_float = (minutes_float-minutes)*60
    seconds = round(seconds_float, 1)
    return str(degrees) + deg_delim + str(minutes) + min_delim + str(seconds) + sec_delim
    