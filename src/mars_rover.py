from src.grid import Grid


class MarsRover:
    __grid: Grid
    directions = ["N", "E", "S", "W"]
    move_forward_command = "M"
    turn_right_command = "R"
    turn_left_command = "L"

    def __init__(self, grid: Grid):
        self.__grid = grid

    def execute(self, command: str) -> str:
        direction = self.directions[0]
        y_axis = 0
        x_axis = 0

        for instruction in command:
            if instruction == self.turn_right_command:
                direction = self.__turn_right(direction)

            if instruction == self.turn_left_command:
                direction = self.__turn_left(direction)

            if instruction == self.move_forward_command:
                if direction == self.directions[0]:
                    y_axis += 1
                elif direction == self.directions[1]:
                    x_axis += 1
                elif direction == self.directions[2]:
                    y_axis -= 1
                else:
                    x_axis -= 1

        return str(x_axis % self.__grid.width()) + ":" + str(y_axis % self.__grid.height()) + ":" + direction

    def __turn_left(self, direction: str) -> str:
        return self.directions[(self.directions.index(direction) - 1) % len(self.directions)]

    def __turn_right(self, direction: str) -> str:
        return self.directions[(self.directions.index(direction) + 1) % len(self.directions)]
