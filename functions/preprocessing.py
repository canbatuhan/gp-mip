import numpy as np
import csv

from structs import Sensor


def generate_random_sensors(size:int, sensor_count:int, max_score:int, min_score:int) -> set:
    """
        Description:
            Generates sensors with random x and y locations
            within the given range (grid size)

        Arguments:
            - size : `int` grid size
            - sensor_count : `int` number of `Sensor` nodes
            - max_score : `int` maximum score a `Sensor` can have
            - min_score : `int` minimum score a `Sensor` can have

        Return:
            - `set` : set storing the `Sensor` nodes
    """
    sensor_set = set()

    for id in range(sensor_count):
        new_sensor = Sensor(
            id=str(id),
            x=np.random.randint(0, size),
            y=np.random.randint(0, size),
            score=np.random.randint(min_score, max_score+1))
        sensor_set.add(new_sensor)

    return sensor_set


def init_sensors_from_file(file_path:str) -> set:
    with open(file_path) as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader, None)
        
        for row in reader:
            print(row)
        
