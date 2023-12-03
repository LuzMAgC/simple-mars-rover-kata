import pytest
from src.mars_rover import MarsRover


class TestMarsRover:
    @pytest.fixture
    def mars_rover(self):
        return MarsRover()

    def test_landing_position_returns_0_0_N(self, mars_rover):
        assert mars_rover.execute("") == "0:0:N"

    @pytest.mark.parametrize("command, expected", [
        ("M", "0:1:N"),
        ("MM", "0:2:N"),
        ("MMM", "0:3:N")
    ])
    def test_command_forward_return(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected

    def test_command_forward_to_end_of_grid_should_wrap_around(self, mars_rover):
        assert mars_rover.execute("MMMMMMMMMM") == "0:0:N"

    @pytest.mark.parametrize("command, expected", [
        ("MMMMMMMMMMM", "0:1:N"),
        ("MMMMMMMMMMMM", "0:2:N")
    ])
    def test_command_forward_after_wrapping_around_return(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected
