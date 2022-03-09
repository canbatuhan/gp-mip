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
        new_sensor = Sensor(str(id), np.random.randint(0, size), np.random.randint(0, size))
        sensor_set.add(new_sensor)

    return sensor_set


def record_sensor_locations(sensor_set:set) -> None:
    """
        Description:
            Records the sensor locations for further use

        Arguments:
            - sensor_set : `set` set storing the sensors
    """
    with open('docs/sensor_locations.txt', 'w') as file:
        for sensor in sensor_set:
            file.write(f'Sensor#{sensor.get_id()}\tx:{sensor.get_x()}\ty:{sensor.get_y()}\n')


def show_sensor_locations(grid:Grid, sensor_set:set) -> None:
    """
        Description:
            Visualizes the sensors on the generated grid
            and saves the figure
    
        Arguments:
            - grid : `Grid` grid that the sensors are located on
            - sensor_set : `set` array storing the sensors
    """
    x_locations = [sensor.get_x() for sensor in sensor_set]
    y_locations = [sensor.get_y() for sensor in sensor_set]

    plt.title("Sensor Locations on Grid")
    plt.xlim(left=0, right=grid.get_width())
    plt.ylim(bottom=0, top=grid.get_height())

    plt.grid(b=True, axis='both')
    plt.scatter(x_locations, y_locations, color='r', alpha=0.9)
    plt.savefig('docs/sensor_locations.png')
