import pytest
from src.grid import Grid
from src.mars_rover import MarsRover


class TestMarsRover:
    @pytest.fixture
    def mars_rover(self):
        return MarsRover(Grid.make_default())

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

    @pytest.mark.parametrize("command, expected", [
        ("MRRM", "0:0:S"),
        ("MMRRM", "0:1:S"),
        ("RRMMRRM", "0:9:N"),
        ("MMMMMMMMMMMMRRMMMMMMMMMMMMMR", "0:9:W"),
        ("MMRRMRRMMMMRRMMRRMRRR", "0:4:W")
    ])
    def test_moving_back_the_way_it_came(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected

    @pytest.mark.parametrize("command, expected", [
        ("L", "0:0:W"),
        ("LL", "0:0:S"),
        ("LLL", "0:0:E"),
        ("LLLLL", "0:0:W")
    ])
    def test_rotate_left_return(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected

    @pytest.mark.parametrize("command, expected", [
        ("LLM", "0:9:S"),
        ("LLMLLMML", "0:1:W"),
        ("LLMMMRRMRLMRRL", "0:9:E")
    ])
    def test_moving_on_y_axis_after_turning_left_and_right(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected

    @pytest.mark.parametrize("command, expected", [
        ("RM", "1:0:E"),
        ("RMM", "2:0:E"),
        ("RMMMM", "4:0:E")
    ])
    def test_moving_east(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected

    @pytest.mark.parametrize("command, expected", [
        ("RMMMMMMMMMMM", "1:0:E"),
        ("RMMMMMMMMMMMM", "2:0:E"),
        ("RMMMMMMMMMMMMM", "3:0:E")
    ])
    def test_command_moving_east_after_wrapping_around_return(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected

    @pytest.mark.parametrize("command, expected", [
        ("LM", "9:0:W"),
        ("LMM", "8:0:W"),
        ("LMMMM", "6:0:W")
    ])
    def test_moving_west(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected

    @pytest.mark.parametrize("command, expected", [
        ("RML", "1:0:N"),
        ("RMMMMMMMLMMMRMMMMLMMMML", "1:7:W"),
        ("LLLMMMLMMMRRMMMMLMMMML", "7:9:N"),
        ("LMR", "9:0:N"),
        ("LMMRMMLMRRMMMMMRMLLM", "2:2:N"),
        ("LMLMLMLMR", "0:0:E")
    ])
    def test_command_moving_around(self, mars_rover, command, expected):
        assert mars_rover.execute(command) == expected
