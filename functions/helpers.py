import numpy as np
import matplotlib.pyplot as plt

from structs import Grid, Sensor


def calculate_distance(point1:tuple, point2:tuple) -> int:
    x1, y1 = point1
    x2, y2 = point2
    return int(np.sqrt((x1-x2)**2 + (y1-y2)**2))


def generate_circle(center:tuple, radius:int) -> tuple:
    center_x, center_y = center
    theta = np.linspace(0 , 2*np.pi, 150)
    x_data = radius * (np.cos(theta) - center_x)
    y_data = radius * (np.sin(theta) - center_y)
    return x_data, y_data


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


def record_locations(node_type:str, node_set:set, file_path:str) -> None:
    """
        Description:
            Records the node locations for further use

        Arguments:
            - node_type : `str` type of the node
            - node_set : `set` set storing the nodes
            - file_path : `str` file to write into 
    """
    with open(file_path, 'w') as file:
        for node in node_set:
            file.write('{}#{}\tx:{}\ty:{}\n'.format(
                node_type, node.get_id(), node.get_x(), node.get_y()))


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
    x_locations, y_locations = list(), list()
    for node in node_set:
        x_locations.append(node.get_x())
        y_locations.append(node.get_y())

    plt.title("{} Locations on Grid".format(node_type))
    plt.xlim(left=0, right=grid.get_width())
    plt.ylim(bottom=0, top=grid.get_height())

    plt.scatter(x_locations, y_locations, alpha=0.9)
    plt.legend()
    plt.savefig(file_path)
    plt.show()


def show_grid(grid:Grid, sensor_set:set, gateway_set:list, distance_threshold:int, file_path:str) -> None:
    """
        Description:
            Visualizes the sensors and gateways on the same grid
            and visualizes the connection between nodes, finally
            saves the figure

        Arguments:
            - grid : `Grid` grid that the nodes are located on
            - sensor_set : `set` set storing the sensor objects
            - gateway_set : `set` set storing the gateway objects
            - distance_threshold : `int` upper limit of distance
            between nodes so that can communicate
            - file_path : `str` file to save figure into
    """
    gateway_x_data, gateway_y_data = list(), list()
    for gateway in gateway_set:
        gateway_x_data.append(gateway.get_x())
        gateway_y_data.append(gateway.get_y())
        circle_x, circle_y = generate_circle(
            center=(gateway.get_x(), gateway_y_data()),
            radius=distance_threshold)
        plt.plot(circle_x, circle_y, color='grey')

    sensor_x_data, sensor_y_data = list(), list()
    for sensor in sensor_set:
        sensor_x_data.append(sensor.get_x())
        sensor_y_data.append(sensor.get_y()) 

    plt.title("Grid")
    plt.xlim(left=0, right=grid.get_width())
    plt.ylim(bottom=0, top=grid.get_height())

    plt.scatter(gateway_x_data, gateway_y_data, label="Gateways", s=50)
    plt.scatter(sensor_x_data, sensor_y_data, label="Sensors", s=20)

    for gateway in gateway_set:
        gateway_point = (gateway.get_x(), gateway.get_y())
        for sensor in sensor_set:
            sensor_point = (sensor.get_x(), sensor.get_y())
            if calculate_distance(gateway_point, sensor_point) <= distance_threshold:
                x_data = [gateway.get_x(), sensor.get_x()]
                y_data = [gateway.get_y(), sensor.get_y()]
                plt.plot(x_data, y_data, color = "g", alpha = 0.9)
            
    plt.legend()
    plt.savefig(file_path)
    plt.show()
