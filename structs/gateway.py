from .node import Node

class Gateway(Node):
    def __init__(self, id: str, x: int, y: int) -> None:
        super().__init__(id, x, y)

    def __str__(self) -> str:
        return "[Sensor#{}; x={}, y{}]".format(
            self.__id, self.__x, self.__y)
