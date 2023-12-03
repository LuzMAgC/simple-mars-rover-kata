class MarsRover:
    direction = ["N", "E", "S", "W"]

    def execute(self, command: str) -> str:
        y_axis = command.count("M") % 10
        direction = self.direction[command.count("R") % len(self.direction)]

        return "0:" + str(y_axis) + ":" + direction
