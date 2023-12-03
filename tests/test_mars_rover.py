from src.mars_rover import MarsRover


class TestMarsRover:
    def test_landing_position_returns_0_0_N(self):
        # Given
        mars_rover = MarsRover()

        # When

        # Then
        assert mars_rover.execute("") == "0:0:N"

    def test_command_forward_returns_0_1_N(self):
        # Given
        mars_rover = MarsRover()

        # When

        # Then
        assert mars_rover.execute("M") == "0:1:N"
