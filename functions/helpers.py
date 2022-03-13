import numpy as np
import matplotlib.pyplot as plt

from structs import Grid, Sensor


def generate_sensors(size:int, sensor_count:int) -> set:
    """
        Description:
            Generates sensors with random x and y locations
            within the given range (grid size)

        Arguments:
            - size : `int` grid size
            - sensor_count : `int` number of sensors

        Return:
            - `set` : set storing the sensor objects
    """
    sensor_set = set()

    for id in range(sensor_count):
        new_sensor = Sensor(
            id=str(id),
            x=np.random.randint(0, size),
            y=np.random.randint(0, size))
        sensor_set.add(new_sensor)

    return sensor_set


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


def generate_circle(center:tuple, radius:int) -> tuple:
    """
        Description:
            Generates a circle data on x and y axes
        
        Arguments:
            - center : `tuple` center location of the circle
            - radius : `int` radiues of the center
    """
    center_x, center_y = center
    theta = np.linspace(0, 2*np.pi, 150)
    x_data = radius * np.cos(theta) + center_x
    y_data = radius * np.sin(theta) + center_y
    return x_data, y_data

