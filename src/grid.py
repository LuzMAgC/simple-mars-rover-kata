class Grid:
    __height: int
    __width: int

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    @classmethod
    def make_default(cls) -> "Grid":
        return cls(10, 10)

    def height(self) -> int:
        return self.__height

    def width(self) -> int:
        return self.__width
