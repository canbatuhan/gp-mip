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
        sensor.find_covered_gateways(gateway_set, distance_threshold)
    
    for gateway in gateway_set:
        gateway.find_covered_sensors(sensor_set, distance_threshold)


def denormalize_locations(sensor_set:set, gateway_set:set, grid_size:int, longitude:tuple, latitude:tuple) -> None:
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


def record_nodes(node_set:set, file_path:str) -> None:
    """
        Description:
            Records the node locations for further use

        Arguments:
            - node_type : `str` type of the node
            - node_set : `set` set storing the nodes
            - file_path : `str` file to write into 
    """
    SECONDS_DELIMITER = '"'
    MINUTES_DELIMITER = '\''
    DEGREES_DELIMITER = 'Â°' # in Windows
    #DEGREES_DELIMITER = '°' # in Linux

    with open(file_path, 'w') as file:
        for node in node_set:
            """latitude = helpers.convert_to_coordinate(
                raw_data=node.get_y(),
                sec_delim=SECONDS_DELIMITER,
                min_delim=MINUTES_DELIMITER,
                deg_delim=DEGREES_DELIMITER)"""

            """longitude = helpers.convert_to_coordinate(
                raw_data=node.get_x(),
                sec_delim=SECONDS_DELIMITER,
                min_delim=MINUTES_DELIMITER,
                deg_delim=DEGREES_DELIMITER)"""
            
            file.write('{}\t{}\t{}\t{}\n'.format(
                node.get_id(), node.get_y(), node.get_x(), node.get_z()))
