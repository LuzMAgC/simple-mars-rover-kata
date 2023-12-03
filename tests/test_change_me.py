from src.change_me import ChangeMe


class TestChangeMe:
    def test_change_me(self):
        # Given
        change_me = ChangeMe()

        # When

        # Then
        assert change_me.change_me() == True
