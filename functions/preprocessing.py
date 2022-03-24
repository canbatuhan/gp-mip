import numpy as np
import csv

from . import helpers
from structs import Sensor


def generate_random_sensors(size:int, sensor_count:int) -> set:
    """
        Description:
            Generates sensors with random x and y locations
            within the given range (grid size)

        Arguments:
            - size : `int` grid size
            - sensor_count : `int` number of `Sensor` nodes
            - max_score : `int` maximum score a `Sensor` can have
            - min_score : `int` minimum score a `Sensor` can have

        Return:
            - `set` : set storing the `Sensor` nodes
    """
    sensor_set = set()

    for id in range(sensor_count):
        new_sensor = Sensor(
            id=str(id),
            x=np.random.randint(0, size),
            y=np.random.randint(0, size),
            score=np.random.rand())
        sensor_set.add(new_sensor)

    return sensor_set


def init_sensors_from_file(file_path:str) -> set:
    """
        Description:
            Reads location data of the sensors placed
            on the Ergene River, and create `Sensor` objects
            from this data

        Arguments:
            - file_path : `str` path of the input file

        Return:
            - `set` : set storing `Sensor` objects
    """
    SECONDS_DELIMITER = '"'
    MINUTES_DELIMITER = '\''
    DEGREES_DELIMITER = 'Â°' # in Windows
    # DEGREES_DELIMITER = '°' # in Linux
    
    sensor_set = set()

    with open(file_path) as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader, None) # headers
        
        for row in reader:
            sensor_id = row[0]
            latitude = row[1] # for example 41°47'30.7"
            longitude = row[2] # for example 27°16'37.9"
            #elevation = row[3]

            long_as_float = helpers.convert_to_float(
                raw_data=longitude,
                sec_delim=SECONDS_DELIMITER,
                min_delim=MINUTES_DELIMITER,
                deg_delim=DEGREES_DELIMITER)

            lat_as_float = helpers.convert_to_float(
                raw_data=latitude,
                sec_delim=SECONDS_DELIMITER,
                min_delim=MINUTES_DELIMITER,
                deg_delim=DEGREES_DELIMITER)

            new_sensor = Sensor(
                id=sensor_id,
                x=long_as_float,
                y=lat_as_float,
                score=np.random.rand()*(0.41-0.17)+0.17)

            sensor_set.add(new_sensor)

    return sensor_set


def set_sensor_scores(sensor_set:set, file_path:str) -> None:
    """
        Description:
            Sets the scores of some `Sensor` objects.
            TODO : There are some sensors without score,
            random scores will be assigned to these sensors

        Arguments:
            - sensor_set : `set` set storing `Sensor` objects
            - file_path : `str` path of the input file
    """
    with open(file_path) as file:
        reader = csv.reader(file, delimiter=',')
        next(reader, None) # headers

        for row in reader:
            #index = row[0]
            sensor_id = row[1]
            #sensor_number = row[2]
            #sensor_cost = row[3]
            sensor_score = float(row[4])
            
            for sensor in sensor_set:
                if sensor.get_id() == sensor_id:
                    sensor.set_score(sensor_score)


def normalize_sensor_locations(sensor_set:set, grid_size:int) -> None:
    """
        Description:
            Normalizes the location data of `Sensor` objects,
            so they can be used in the optimization model

        Arguments:
            - sensor_set : `set` set storing the `Sensor` objects
            - grid_size : `int` size to normalize the location data
    """
    max_x, max_y, min_x, min_y = helpers.get_max_min_locations(sensor_set)
    for sensor in sensor_set:
        new_x = grid_size*(sensor.get_x()-min_x)/(max_x-min_x)
        new_y = grid_size*(sensor.get_y()-min_y)/(max_y-min_y)
        sensor.set_x(new_x)
        sensor.set_y(new_y)
