from src.dynamic_programming.lcs import lcs_memoized, lcs_dp

class TestLCS:
    def test_lcs_memoized(self):
        sequence_1 = "HIEROGLYPHOLOGY"
        sequence_2 = "MICHAELANGELO"
        expected_result = 5
        assert lcs_memoized(sequence_1, sequence_2) == expected_result

    def test_lcs_dp(self):
        sequence_1 = "HIEROGLYPHOLOGY"
        sequence_2 = "MICHAELANGELO"
        expected_result = "IELLO"
        assert lcs_dp(sequence_1, sequence_2) == expected_result
