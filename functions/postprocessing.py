import csv
from . import helpers


def connect_nodes(sensor_set:set, gateway_set:set, distance_threshold:float) -> None:
    """
        Description:
            Connects the `Sensor` objects and `Gateway` objects
            with each other to analyse the model performance

        Argunments:
            - sensor_set : `set` set storing the `Sensor` nodes
            - gateway_set : `set` set storing the `Gateway` nodes
            - distance_threshold : `float` upper limit of distance
            between nodes so that can communicate
    """
    for sensor in sensor_set:
        sensor.find_covering_gateway(gateway_set, distance_threshold)
    
    for gateway in gateway_set:
        gateway.find_covered_sensors(sensor_set, distance_threshold)


def denormalize_locations(sensor_set:set, gateway_set:set, grid_size:int, longitude:tuple, latitude:tuple) -> tuple:
    """
        Descriptipn:
            Denormalizes the location data of `Sensor` objects,
            so they will have their original values

        Arguments:
            - sensor_set : `set` set storing the `Sensor` objects
            - gateway_set : `set` set storing the `Gateway` objects
            - grid_size : `int` size of the grid
            - longitude : `tuple` maximum and minimum longitude values
            - latitude : `tuple` maximum and minimum latitude values

        Returns:
            - `tuple` : maximum and minimum longitude and latitude data
    """
    max_long, min_long = longitude
    max_lat, min_lat = latitude

    for sensor in sensor_set:
        new_x = (max_long-min_long)*(sensor.get_x())/(grid_size) + min_long
        new_y = (max_lat-min_lat)*(sensor.get_y())/(grid_size) + min_lat
        sensor.set_x(new_x)
        sensor.set_y(new_y)

    for gateway in gateway_set:
        new_x = (max_long-min_long)*(gateway.get_x())/(grid_size) + min_long
        new_y = (max_lat-min_lat)*(gateway.get_y())/(grid_size) + min_lat
        gateway.set_x(new_x)
        gateway.set_y(new_y)

    return (grid_size, 0), (grid_size, 0)


def set_gateway_elevations(gateway_set:set) -> None:
    """
        Description:
            Sets the gateway elevations according to the covered
            sensors by the gateway

        Arguments:
            - gateway_set : `set` set storing Gateway objects
    """
    for gateway in gateway_set:
        total_elevation = 0
        for sensor in gateway.get_covered_sensors():
            total_elevation = total_elevation + sensor.get_z()
        
        avg_elevation = total_elevation / len(gateway.get_covered_sensors())
        gateway.set_z(avg_elevation)


def record_sensor_locations(sensor_set:set, file_path:str) -> None:
    """
        Description:
            Records the node locations for further use

        Arguments:
            - sensor_set : `set` set storing the nodes
            - file_path : `str` file to write into 
    """
    with open(file_path, 'w') as file:
        for sensor in sensor_set:
            file.write('{}\t{}\t{}\t{}\n'.format(
                sensor.get_id(), sensor.get_y(), sensor.get_x(), sensor.get_z()))


def record_gateway_placements(top_n:int, sensor_set:set, gateway_set:set, file_path:str) -> None:
    """
        Description:
            Records the gateways covering the top `n`
            sensors, according to their scores

        Arguments:
            - top_n : `int` number of sensors to take
            - sensor_set : `set` set storing `Sensor` objects
            - gateway_set : `set` set storing `Gateway` objects
            - file_path : `str` file to write into
    """
    top_sensors = helpers.get_top_sensors(sensor_set, top_n)

    with open(file_path, 'w') as file:
        for gateway in gateway_set:
            for sensor in gateway.get_covered_sensors():
                if sensor in top_sensors:
                    file.write('{}\t{}\t{}\t{}\n'.format(
                        gateway.get_id(), gateway.get_y(), gateway.get_x(), gateway.get_z()))
                    break
                

def sensor_locations_loraplan(sensor_set:set, file_path:str):
    """
        Description:
            Records the node locations for further use

        Arguments:
            - sensor_set : `set` set storing the sensors
            - file_path : `str` file to write into 
    """
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['lat', 'lon', 'number_sensors'])

        for sensor in sensor_set:
            writer.writerow([
                sensor.get_y(), sensor.get_x(), 1.0])


def gateway_placements_loraplan(gateway_set:set, file_path:str):
    """
        Description:
            Records the node locations for further use

        Arguments:
            - gateway_set : `set` set storing the gateways
            - file_path : `str` file to write into 
    """
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            'id', 'x', 'y', 'height', 'environment'])

        for gateway in gateway_set:
            writer.writerow([
                gateway.get_id(), gateway.get_y(), gateway.get_x(), gateway.get_z(), 'urban'])