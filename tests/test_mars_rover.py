from src.mars_rover import MarsRover


class TestMarsRover:
    def test_landing_position_returns_0_0_N(self):
        # Given
        mars_rover = MarsRover()

        # When

        # Then
        assert mars_rover.execute("") == "0:0:N"
