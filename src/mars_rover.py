class MarsRover:
    def execute(self, command: str) -> str:
        return "0:"+str(len(command) % 10)+":N"
