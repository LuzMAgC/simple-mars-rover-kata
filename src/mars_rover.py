from src.grid import Grid


class MarsRover:
    __grid: Grid
    __directions = ["N", "E", "S", "W"]
    __move_forward_command = "M"
    __turn_right_command = "R"
    __turn_left_command = "L"

    def __init__(self, grid: Grid):
        self.__grid = grid

    def execute(self, command: str) -> str:
        direction = self.__directions[0]
        y_axis = 0
        x_axis = 0

        for instruction in command:
            if instruction == self.__turn_right_command:
                direction = self.__turn_right(direction)

            if instruction == self.__turn_left_command:
                direction = self.__turn_left(direction)

            if instruction == self.__move_forward_command:
                if direction == self.__directions[0]:
                    y_axis += 1
                elif direction == self.__directions[1]:
                    x_axis += 1
                elif direction == self.__directions[2]:
                    y_axis -= 1
                else:
                    x_axis -= 1

        return str(x_axis % self.__grid.width()) + ":" + str(y_axis % self.__grid.height()) + ":" + direction

    def __turn_left(self, direction: str) -> str:
        return self.__directions[(self.__directions.index(direction) - 1) % len(self.__directions)]

    def __turn_right(self, direction: str) -> str:
        return self.__directions[(self.__directions.index(direction) + 1) % len(self.__directions)]
