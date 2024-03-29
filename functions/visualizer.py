import numpy as np
import matplotlib.pyplot as plt

from . import helpers
from structs import Grid


def generate_circle(center:tuple, radius:int) -> tuple:
    """
        Description:
            Generates a circle data on x and y axes
        
        Arguments:
            - center : `tuple` center location of the circle
            - radius : `int` radiues of the center

        Returns:
            - `np.ndarray` : circle-plot data on x axis
            - `np.ndarray` : circle-plot data on y axis
    """
    center_x, center_y = center
    theta = np.linspace(0, 2*np.pi, 150)
    x_data = radius * np.cos(theta) + center_x
    y_data = radius * np.sin(theta) + center_y
    return x_data, y_data


def show_sensor_locations(sensor_set:set, grid:Grid, file_path:str) -> None:
    """
        Description:
            Visualizes the nodes on the generated grid
            and saves the figure
    
        Arguments:
            - sensor_set : `set` set storing the nodes
            - grid : `Grid` grid that the nodes are located on
            - file_path : `str` file to save figure into 
    """
    plt.figure(figsize=(9, 9))
    plt.title("Sensor Locations")
    plt.xlim(left=0-int(grid.get_width()*0.1), right=int(grid.get_width()*1.1))
    plt.ylim(bottom=0-int(grid.get_height()*0.1), top=int(grid.get_height()*1.1))

    sensor_x_data, sensor_y_data = list(), list()
    for sensor in sensor_set:
        sensor_x_data.append(sensor.get_x())
        sensor_y_data.append(sensor.get_y())
        
    plt.scatter(
        sensor_x_data, sensor_y_data,
        label="Sensors", marker='x',
        s=20, color="darkorange", alpha=0.9)
        
    plt.legend()
    plt.savefig(file_path)
    #plt.show()
    plt.close()


def show_gateway_placements(top_n:int, sensor_set:set, gateway_set:set, grid:Grid, distance_threshold:float, file_path:str) -> None:
    """
        Description:
            Visualizes the sensors and gateways on the same grid
            and visualizes the connection between nodes, finally
            saves the figure

        Arguments:
            - top_n : `int` number of sensors to take
            - sensor_set : `set` set storing the `Sensor` nodes
            - gateway_set : `set` set storing the `Gateway` nodes
            - grid : `Grid` grid that the nodes are located on
            - distance_threshold : `float` upper limit of distance
            between nodes so that can communicate
            - file_path : `str` file to save figure into
    """
    plt.figure(figsize=(9, 9))
    plt.title("Grid")
    plt.xlim(left=0-int(grid.get_width()*0.1), right=int(grid.get_width()*1.1))
    plt.ylim(bottom=0-int(grid.get_height()*0.1), top=int(grid.get_height()*1.1))

    gateway_x_data, gateway_y_data = list(), list()
    for gateway in gateway_set:
        gateway_x_data.append(gateway.get_x())
        gateway_y_data.append(gateway.get_y())

        circle_x, circle_y = generate_circle(
            center=(gateway.get_x(), gateway.get_y()),
            radius=distance_threshold)

        plt.plot(
            circle_x, circle_y,
            color='grey', alpha=0.5,
            linestyle='--', linewidth=0.75)

    sensor_x_data, sensor_y_data = list(), list()
    for sensor in sensor_set:
        sensor_x_data.append(sensor.get_x())
        sensor_y_data.append(sensor.get_y()) 

    hot_sensor_x_data, hot_sensor_y_data = list(), list()
    for hot_sensor in helpers.get_top_sensors(sensor_set, top_n):
        hot_sensor_x_data.append(hot_sensor.get_x())
        hot_sensor_y_data.append(hot_sensor.get_y())

    plt.scatter(
        gateway_x_data, gateway_y_data,
        label="Gateways", marker='o',
        s=50, color="royalblue", alpha=0.9)

    plt.scatter(
        sensor_x_data, sensor_y_data,
        label="Sensors", marker='x',
        s=20, color="darkorange", alpha=0.9)

    plt.scatter(
        hot_sensor_x_data, hot_sensor_y_data,
        label="Top {} Sensor".format(top_n), marker="x",
        s=20, color='red')

    for gateway in gateway_set:
        for sensor in sensor_set:
            gateway_point = (gateway.get_x(), gateway.get_y())
            sensor_point = (sensor.get_x(), sensor.get_y())
            if helpers.calculate_distance(gateway_point, sensor_point) <= distance_threshold:
                x_data = [gateway.get_x(), sensor.get_x()]
                y_data = [gateway.get_y(), sensor.get_y()]

                plt.plot(
                    x_data, y_data,
                    color="g", alpha=0.8,
                    linestyle='-', linewidth=1)
            
    plt.legend()
    plt.savefig(file_path)
    #plt.show()
    plt.close()
