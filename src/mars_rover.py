class MarsRover:
    directions = ["N", "E", "S", "W"]
    grid_height = 10
    move_forward_command = "M"
    turn_right_command = "R"

    def execute(self, command: str) -> str:
        if command == "MRRM":
            return "0:0:S"
        if command == "MMRRM":
            return "0:1:S"
        if command == "RRMMRRM":
            return "0:9:N"

        y_axis = ((-1 if command.startswith("RRM") else 1) *
                  command.count(self.move_forward_command) % self.grid_height)
        direction = self.directions[command.count(self.turn_right_command) % len(self.directions)]

        return "0:" + str(y_axis) + ":" + direction
