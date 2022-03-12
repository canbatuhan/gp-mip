class Node:
    def __init__(self, id:str, x:int, y:int) -> None:
        self.__id = id
        self.__x = x
        self.__y = y

    def get_id(self) -> str:
        return self.__id

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y


class Gateway(Node):
    def __init__(self, id: str, x: int, y: int) -> None:
        super().__init__(id, x, y)

    def __str__(self) -> str:
        return "[Sensor#{}; x={}, y{}]".format(
            self.__id, self.__x, self.__y)


class Sensor(Node):
    def __init__(self, id: str, x: int, y: int) -> None:
        super().__init__(id, x, y)

    def __str__(self) -> str:
        return "[Sensor#{}; x={}, y{}]".format(
            self.__id, self.__x, self.__y)
