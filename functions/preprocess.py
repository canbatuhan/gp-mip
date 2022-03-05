import numpy as np
import matplotlib.pyplot as plt

from ..structs import Grid, Sensor

def generate_sensors(size:int, sensor_count:int) -> np.ndarray:
    """
        Description:
            Generates sensors with random x and y locations
            within the given range (grid size)

        Arguments:
            - size : `int`, grid size
            - sensor_count : `int`, number of sensors

        Return:
            - `np.ndarray` : array storing the sensor objects
    """
    arr = np.ndarray([], dtype=Sensor)
    for _ in range(sensor_count):
        new_sensor = Sensor(np.random.randint(0, size+1), np.random.randint(0, size+1))
        np.append(arr, new_sensor)
    return arr

def show_sensor_locations(grid:Grid, sensor:np.ndarray):
    pass