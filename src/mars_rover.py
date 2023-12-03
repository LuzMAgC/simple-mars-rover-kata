class MarsRover:
    directions = ["N", "E", "S", "W"]
    grid_height = 10
    move_forward_command = "M"
    turn_right_command = "R"

    def execute(self, command: str) -> str:
        y_axis = command.count(self.move_forward_command) % self.grid_height
        direction = self.directions[command.count(self.turn_right_command) % len(self.directions)]

        return "0:" + str(y_axis) + ":" + direction
