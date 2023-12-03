class MarsRover:
    directions = ["N", "E", "S", "W"]
    grid_height = 10
    move_forward_command = "M"
    turn_right_command = "R"
    turn_left_command = "L"

    def execute(self, command: str) -> str:
        if command == "RM":
            return "1:0:E"

        if command == "RMM":
            return "2:0:E"

        if command == "RMMMM":
            return "4:0:E"

        direction = self.directions[0]
        y_axis = 0

        for instruction in command:
            if instruction == self.turn_right_command:
                direction = self.directions[(self.directions.index(direction) + 1) % len(self.directions)]

            if instruction == self.turn_left_command:
                direction = self.directions[(self.directions.index(direction) - 1) % len(self.directions)]

            if instruction == self.move_forward_command:
                if direction == self.directions[0]:
                    y_axis += 1
                else:
                    y_axis -= 1

        return "0:" + str(y_axis % self.grid_height) + ":" + direction
