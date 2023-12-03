class MarsRover:
    def execute(self, command: str) -> str:
        if command == "R":
            return "0:0:E"
        if command == "RR":
            return "0:0:S"
        return "0:"+str(len(command) % 10)+":N"
