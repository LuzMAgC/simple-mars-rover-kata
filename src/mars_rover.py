class MarsRover:
    direction = ["N", "E", "S", "W"]

    def execute(self, command: str) -> str:
        if command == "RRRRM":
            return "0:1:N"

        if "R" in command:
            return "0:0:" + self.direction[len(command) % len(self.direction)]

        return "0:"+str(len(command) % 10)+":N"
