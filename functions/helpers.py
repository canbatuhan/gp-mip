import numpy as np
import matplotlib.pyplot as plt
from .clustering import calculate_distance

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


def record_sensor_locations(sensor_set:set) -> None:
    """
        Description:
            Records the sensor locations for further use

        Arguments:
            - sensor_set : `set` set storing the sensors
    """
    with open('docs/sensor_locations.txt', 'w') as file:
        for sensor in sensor_set:
            file.write('Sensor#{}\tx:{}\ty:{}\n'.format(
                sensor.get_id(), sensor.get_x(), sensor.get_y()))


def record_gateway_locations(grid:Grid, gateway_locations:list) -> None:
    with open('docs/gateway_locations.txt', 'w') as file:
        for x in grid.get_width_as_range():
            for y in grid.get_height_as_range():
                if gateway_locations[y][x].x == 1:
                    file.write('Gateway#{}{}\tx:{}\ty:{}\n'.format(
                        x, y, x, y))


def show_sensor_locations(grid:Grid, sensor_set:set) -> None:
    """
        Description:
            Visualizes the sensors on the generated grid
            and saves the figure
    
        Arguments:
            - grid : `Grid` grid that the sensors are located on
            - sensor_set : `set` array storing the sensors
    """
    x_locations, y_locations = list(), list()
    for sensor in sensor_set:
        x_locations.append(sensor.get_x())
        y_locations.append(sensor.get_y())

    plt.title("Sensor Locations on Grid")
    plt.xlim(left=0, right=grid.get_width())
    plt.ylim(bottom=0, top=grid.get_height())

    plt.grid(b=True, axis='both')
    plt.scatter(x_locations, y_locations, alpha=0.9)
    plt.legend()
    plt.savefig('docs/sensor_locations.png')
    plt.show()


def show_gateway_locations(grid:Grid, gateway_locations:list) -> None:
    x_locations, y_locations = list(), list()
    for x in grid.get_width_as_range():
        for y in grid.get_height_as_range():
            if gateway_locations[y][x].x == 1:
                x_locations.append(x)
                y_locations.append(y)

    plt.title("Gateway Locations on Grid")
    plt.xlim(left=0, right=grid.get_width())
    plt.ylim(bottom=0, top=grid.get_height())

    plt.grid(b=True, axis='both')
    plt.scatter(x_locations, y_locations, alpha=0.9)
    plt.legend()
    plt.savefig('docs/gateway_locations.png')
    plt.show()


def show_grid(grid:Grid, sensor_set:set, gateway_locations:list, distance_threshold:int) -> None:
    gateway_x_data, gateway_y_data = list(), list()
    for y in grid.get_height_as_range():
        for x in grid.get_width_as_range():
            if gateway_locations[y][x].x == 1:
                gateway_x_data.append(x)
                gateway_y_data.append(y)
                for sensor in sensor_set:
                    distance = calculate_distance((sensor.get_x(), sensor.get_y()), (x, y))
                    if distance <= distance_threshold:
                        plt.plot(
                            [x, sensor.get_x()],
                            [y, sensor.get_y()],
                            color="g", alpha=0.8
                        )

    sensor_x_data, sensor_y_data = list(), list()
    for sensor in sensor_set:
        sensor_x_data.append(sensor.get_x())
        sensor_y_data.append(sensor.get_y()) 

    plt.title("Grid")
    plt.xlim(left=0, right=grid.get_width())
    plt.ylim(bottom=0, top=grid.get_height())

    plt.grid(b=True, axis='both')
    plt.scatter(gateway_x_data, gateway_y_data, label="Gateways", s=40)
    plt.scatter(sensor_x_data, sensor_y_data, label="Sensors", s=20)
    plt.legend()
    plt.savefig('docs/grid.png')
    plt.show()
