class MarsRover:
    direction = ["N", "E", "S", "W"]

    def execute(self, command: str) -> str:
        if "R" in command:
            return "0:0:" + self.direction[len(command)]

        return "0:"+str(len(command) % 10)+":N"
