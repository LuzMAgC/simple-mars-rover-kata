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

    @pytest.mark.parametrize("command, expected", [
        ("MMMMMMMMMM", "0:0:N"),
        ("MMMMMMMMMMM", "0:1:N"),
        ("MMMMMMMMMMMM", "0:2:N")
    ])
    def test_command_forward_after_wrapping_around_return(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected

    @pytest.mark.parametrize("command, expected", [
        ("R", "0:0:E"),
        ("RR", "0:0:S"),
        ("RRR", "0:0:W"),
        ("RRRR", "0:0:N")
    ])
    def test_rotate_right_return(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected

    @pytest.mark.parametrize("command, expected", [
        ("RRRRM", "0:1:N"),
        ("MR", "0:1:E"),
        ("MRRRRMRR", "0:2:S")
    ])
    def test_turn_around_and_forward(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected

    @pytest.mark.parametrize("command, expected", [
        ("RRM", "0:9:S"),
        ("RRMM", "0:8:S"),
        ("RRMMM", "0:7:S")
    ])
    def test_moving_south(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected
