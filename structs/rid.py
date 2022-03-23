import numpy as np

class Grid:
    def __init__(self, size) -> None:
        self.__height = size
        self.__width = size

    def __len__(self) -> int:
        return self.__height * self.__width

    def get_height(self) -> int:
        return self.__height

    def get_width(self) -> int:
        return self.__width

    def get_width_as_range(self) -> int:
        return np.arange(self.__height+1, dtype=np.uint8)

    def get_height_as_range(self) -> int:
        return np.arange(self.__width+1, dtype=np.uint8)
