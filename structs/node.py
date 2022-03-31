import numpy as np


def calculate_distance(point1:tuple, point2:tuple) -> float:
    """
        Description:
            Calculates the distance between two points

        Arguments:
            - point1 : `tuple` first point
            - point2 : `tuple` second point

        Returns:
            - `float` : distance between two points
    """
    x1, y1 = point1
    x2, y2 = point2
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)


class Node:
    def __init__(self, id:str, x:float, y:float, z:float) -> None:
        self.__id = id
        self.__x = x
        self.__y = y
        self.__z = z
        self.__covered_nodes = set()

    def find_covered_nodes(self, node_set:set, distance_threshold:float) -> None:
        for node in node_set:
            point = (self.__x, self.__y)
            node_point = (node.get_x(), node.get_y())
            distance = calculate_distance(point, node_point)
            if distance <= distance_threshold:
                self.__covered_nodes.add(node)

    def get_id(self) -> str:
        return self.__id

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def get_z(self) -> float:
        return self.__z

    def get_covered_nodes(self) -> set:
        return self.__covered_nodes

    def set_x(self, x:float) -> None:
        self.__x = x

    def set_y(self, y:float) -> None:
        self.__y = y

    def set_z(self, z:float) -> None:
        self.__z = z


class Sensor(Node):
    def __init__(self, id:str, x:float, y:float, z:float, score:float=0.0) -> None:
        super().__init__(id, x, y, z)
        self.__score = score

    def find_covered_gateways(self, gateway_set:set, distance_threshold:float) -> None:
        self.find_covered_nodes(gateway_set, distance_threshold)

    def get_covered_gateways(self) -> set:
        return self.get_covered_nodes()

    def get_score(self) -> float:
        return self.__score

    def set_score(self, score:float) -> None:
        self.__score = score


class Gateway(Node):
    def __init__(self, id:str, x:float, y:float, z:float) -> None:
        super().__init__(id, x, y, z)

    def __calc_scores(self) -> tuple:
        total_score = 0
        covered_sensors = self.get_covered_sensors()
        for sensor in covered_sensors:
            total_score += sensor.get_score()
        return total_score, total_score / len(covered_sensors)

    def find_covered_sensors(self, sensor_set:set, distance_threshold:float) -> None:
        self.find_covered_nodes(sensor_set, distance_threshold)

    def get_covered_sensors(self) -> set:
        return self.get_covered_nodes()

    def get_total_score(self) -> float:
        return self.__calc_scores()[0]

    def get_average_score(self) -> float:
        return self.__calc_scores()[1]

