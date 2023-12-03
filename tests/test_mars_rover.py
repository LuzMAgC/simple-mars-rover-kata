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

    def test_command_forward_twice_returns_0_2_N(self):
        # Given
        mars_rover = MarsRover()

        # When

        # Then
        assert mars_rover.execute("MM") == "0:2:N"

    def test_command_forward_three_times_returns_0_3_N(self):
        # Given
        mars_rover = MarsRover()

        # When

        # Then
        assert mars_rover.execute("MMM") == "0:3:N"
