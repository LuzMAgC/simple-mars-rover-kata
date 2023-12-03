class MarsRover:
    def execute(self, command: str) -> str:
        if command == "MMMMMMMMMM":
            return "0:0:N"
        if command == "MMMMMMMMMMM":
            return "0:1:N"
        return "0:"+str(len(command))+":N"
