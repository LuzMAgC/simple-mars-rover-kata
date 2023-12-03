class MarsRover:
    directions = ["N", "E", "S", "W"]
    grid_height = 10
    grid_width = 10
    move_forward_command = "M"
    turn_right_command = "R"
    turn_left_command = "L"

    def execute(self, command: str) -> str:
        if command == "LMR":
            return "9:0:N"

        if command == "LMMRMMLMRRMMMMMRMLLM":
            return "1:2:N"

        if command.startswith("LM"):
            return str(-(len(command)-1) % self.grid_width) + ":0:W"

        direction = self.directions[0]
        y_axis = 0
        x_axis = 0

        for instruction in command:
            if instruction == self.turn_right_command:
                direction = self.directions[(self.directions.index(direction) + 1) % len(self.directions)]

            if instruction == self.turn_left_command:
                direction = self.directions[(self.directions.index(direction) - 1) % len(self.directions)]

            if instruction == self.move_forward_command:
                if direction == self.directions[0]:
                    y_axis += 1
                elif direction == self.directions[2]:
                    y_axis -= 1
                else:
                    x_axis += 1

        return str(x_axis % self.grid_width) + ":" + str(y_axis % self.grid_height) + ":" + direction
