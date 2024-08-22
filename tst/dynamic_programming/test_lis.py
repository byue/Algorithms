from src.dynamic_programming.lis import lis_memoized, lis_dp, lis_binary

class TestLIS:
    def test_lis_memoized(self):
        sequence = [10, 5, 8, 3, 9, 4, 12, 11]
        assert lis_memoized(sequence) == 4

    def test_lis_memoized_empty(self):
        sequence = []
        assert lis_memoized(sequence) == 0

    def test_lis_memoized_single(self):
        sequence = [3]
        assert lis_memoized(sequence) == 1

    def test_lis_dp(self):
        sequence = [10, 5, 8, 3, 9, 4, 12, 11]
        assert lis_dp(sequence) == 4

    def test_lis_dp_empty(self):
        sequence = []
        assert lis_dp(sequence) == 0

    def test_lis_dp_single(self):
        sequence = [3]
        assert lis_dp(sequence) == 1

    def test_lis_binary(self):
        sequence = [10, 5, 8, 3, 9, 4, 12, 11]
        assert lis_binary(sequence) == 4

    def test_lis_binary_empty(self):
        sequence = []
        assert lis_binary(sequence) == 0

    def test_lis_binary_single(self):
        sequence = [3]
        assert lis_binary(sequence) == 1