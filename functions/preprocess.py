import numpy as np
import matplotlib.pyplot as plt

from structs import Grid, Sensor

def generate_sensors(size:int, sensor_count:int) -> list:
    """
        Description:
            Generates sensors with random x and y locations
            within the given range (grid size)

        Arguments:
            - size : `int` grid size
            - sensor_count : `int` number of sensors

        Return:
            - `list` : array storing the sensor objects
    """
    arr = list()

    for id in range(sensor_count):
        new_sensor = Sensor(str(id), np.random.randint(0, size), np.random.randint(0, size))
        arr.append(new_sensor)

    return arr


def record_sensor_locations(sensors:list) -> None:
    """
        Description:
            Records the sensor locations for further use

        Arguments:
            - sensors : `list` array storing the sensors
    """
    with open('docs/sensor_locations.txt', 'w') as file:
        for sensor in sensors:
            file.write(f'Sensor#{sensor.get_id()}\tx:{sensor.get_x()}\ty:{sensor.get_y()}\n')


def show_sensor_locations(grid:Grid, sensors:list) -> None:
    """
        Description:
            Visualizes the sensors on the generated grid
            and saves the figure
    
        Arguments:
            - grid : `Grid` grid that the sensors are located on
            - sensors : `list` array storing the sensors
    """
    x_locations = [sensor.get_x() for sensor in sensors]
    y_locations = [sensor.get_y() for sensor in sensors]

    plt.title("Sensor Locations on Grid")
    plt.xlim(left=0, right=grid.get_width())
    plt.ylim(bottom=0, top=grid.get_height())

    plt.grid(b=True, axis='both', )
    plt.scatter(x_locations, y_locations, color="r", alpha=0.9)
    plt.savefig('docs/sensor_locations.png')
