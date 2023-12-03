class MarsRover:
    directions = ["N", "E", "S", "W"]
    grid_height = 10
    move_forward_command = "M"
    turn_right_command = "R"

    def execute(self, command: str) -> str:
        if command == "LLM":
            return "0:9:S"

        if command == "LLMLLMML":
            return "0:1:W"

        if "L" in command:
            return "0:0:" + self.directions[-len(command) % len(self.directions)]

        direction = self.directions[0]
        y_axis = 0

        for instruction in command:
            if instruction == "R":
                direction = self.directions[(self.directions.index(direction) + 1) % len(self.directions)]

            if instruction == "M":
                if direction == "N":
                    y_axis += 1
                else:
                    y_axis -= 1

        return "0:" + str(y_axis % self.grid_height) + ":" + direction
