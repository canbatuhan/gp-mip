import numpy as np
import matplotlib.pyplot as plt

from functions import helpers
from structs import Grid

def show_locations(node_type:str, node_set:set, grid:Grid, file_path:str) -> None:
    """
        Description:
            Visualizes the nodes on the generated grid
            and saves the figure
    
        Arguments:
            - node_type : `str` type of the node
            - node_set : `set` set storing the nodes
            - grid : `Grid` grid that the nodes are located on
            - file_path : `str` file to save figure into 
    """
    plt.figure(figsize=(9, 9))
    plt.title("{} Locations on Grid".format(node_type))
    plt.xlim(left=0, right=grid.get_width())
    plt.ylim(bottom=0, top=grid.get_height())

    x_locations, y_locations = list(), list()
    for node in node_set:
        x_locations.append(node.get_x())
        y_locations.append(node.get_y())

    plt.scatter(
        x_locations, y_locations,
        label=node_type, alpha=0.9)
        
    plt.legend()
    plt.savefig(file_path)
    #plt.show()
    plt.close()


def show_grid(sensor_set:set, gateway_set:set, grid:Grid, distance_threshold:int, file_path:str) -> None:
    """
        Description:
            Visualizes the sensors and gateways on the same grid
            and visualizes the connection between nodes, finally
            saves the figure

        Arguments:
            - grid : `Grid` grid that the nodes are located on
            - sensor_set : `set` set storing the `Sensor` nodes
            - gateway_set : `set` set storing the `Gateway` nodes
            - distance_threshold : `int` upper limit of distance
            between nodes so that can communicate
            - file_path : `str` file to save figure into
    """
    plt.figure(figsize=(9, 9))
    plt.title("Grid")
    plt.xlim(left=0, right=grid.get_width())
    plt.ylim(bottom=0, top=grid.get_height())

    gateway_x_data, gateway_y_data = list(), list()
    for gateway in gateway_set:
        gateway_x_data.append(gateway.get_x())
        gateway_y_data.append(gateway.get_y())

        circle_x, circle_y = helpers.generate_circle(
            center=(gateway.get_x(), gateway.get_y()),
            radius=distance_threshold)

        plt.plot(
            circle_x, circle_y,
            color='grey', alpha=0.5,
            linestyle='--', linewidth=1)

    sensor_x_data, sensor_y_data = list(), list()
    for sensor in sensor_set:
        sensor_x_data.append(sensor.get_x())
        sensor_y_data.append(sensor.get_y()) 

    plt.scatter(
        gateway_x_data, gateway_y_data,
        label="Gateways", marker='o', s=50)

    plt.scatter(
        sensor_x_data, sensor_y_data,
        label="Sensors", marker='x', s=20)

    for gateway in gateway_set:
        gateway_point = (gateway.get_x(), gateway.get_y())
        for sensor in sensor_set:
            sensor_point = (sensor.get_x(), sensor.get_y())
            if helpers.calculate_distance(gateway_point, sensor_point) <= distance_threshold:
                x_data = [gateway.get_x(), sensor.get_x()]
                y_data = [gateway.get_y(), sensor.get_y()]

                plt.plot(
                    x_data, y_data,
                    color = "g", alpha = 0.8,
                    linestyle='-', linewidth=1)
            
    plt.legend()
    plt.savefig(file_path)
    plt.show()
    plt.close()