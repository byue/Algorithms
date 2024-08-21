from src.dynamic_programming.bowling import get_maximum_score_recursive, get_maximum_score_memoized, get_maximum_score_dp

class TestBowling:
    def test_get_maximum_score_recursive(self):
        pins = [1, 1, 9, 9, 2, -5, -5]
        assert get_maximum_score_recursive(pins) == 110

    def test_get_maximum_score_memoized(self):
        pins = [1, 1, 9, 9, 2, -5, -5]
        assert get_maximum_score_memoized(pins) == 110

    def test_get_maximum_score_dp(self):
        pins = [1, 1, 9, 9, 2, -5, -5]
        assert get_maximum_score_dp(pins) == 110
