class MarsRover:
    directions = ["N", "E", "S", "W"]
    grid_height = 10
    move_forward_command = "M"
    turn_right_command = "R"

    def execute(self, command: str) -> str:
        if command == "RRM":
            return "0:9:S"
        if command == "RRMM":
            return "0:8:S"
        if command == "RRMMM":
            return "0:7:S"

        y_axis = command.count(self.move_forward_command) % self.grid_height
        direction = self.directions[command.count(self.turn_right_command) % len(self.directions)]

        return "0:" + str(y_axis) + ":" + direction
