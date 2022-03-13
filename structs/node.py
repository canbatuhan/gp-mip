import numpy as np


def calculate_distance(point1:tuple, point2:tuple) -> int:
    """
        Description:
            Calculates the distance between two points

        Arguments:
            - point1 : `tuple` first point
            - point2 : `tuple` second point

        Returns:
            - `int` : ceil integer of the calculated
            (float) distance
    """
    x1, y1 = point1
    x2, y2 = point2
    return int(np.ceil(np.sqrt((x1-x2)**2 + (y1-y2)**2)))


class Node:
    def __init__(self, id:str, x:int, y:int) -> None:
        self.__id = id
        self.__x = x
        self.__y = y
        self.__covered_nodes = set()

    def get_id(self) -> str:
        return self.__id

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def get_covered_nodes(self) -> set:
        return self.__covered_nodes

    def find_covered_nodes(self, node_set:set, distance_threshold:int) -> None:
        for node in node_set:
            point = (self.__x, self.__y)
            node_point = (node.get_x(), node.get_y())
            distance = calculate_distance(point, node_point)
            if distance <= distance_threshold:
                self.__covered_nodes.add(node)


class Gateway(Node):
    def __init__(self, id: str, x: int, y: int) -> None:
        super().__init__(id, x, y)

    def __str__(self) -> str:
        return "[Gateway#{}; x={}; y={}]".format(
            self.get_id(), self.get_x(), self.get_y())

    def get_covered_sensors(self) -> set:
        return self.get_covered_nodes()

    def find_covered_sensors(self, sensor_set:set, distance_threshold:int) -> None:
        self.find_covered_nodes(sensor_set, distance_threshold)


class Sensor(Node):
    def __init__(self, id: str, x: int, y: int) -> None:
        super().__init__(id, x, y)

    def __str__(self) -> str:
        return "[Sensor#{}; x={}; y={}]".format(
            self.get_id(), self.get_x(), self.get_y())

    def get_covered_gateways(self) -> set:
        return self.get_covered_nodes()

    def find_covered_gateways(self, gateway_set:set, distance_threshold:int) -> None:
        self.find_covered_nodes(gateway_set, distance_threshold)
