from src.stable_matching.stable_matching import get_stable_matches
import pytest

class TestStableMatching:
    def test_missing_receiver(self):
        proposer_to_preferences = {
            "X": ["A", "B", "C"],
            "Y": ["B", "A", "C"],
            "Z": ["A", "A", "C"]
        }

        receiver_to_preferences = {
            "A": ["Y", "X", "Z"],
            "B": ["X", "Y", "Z"],
            "C": ["X", "Y", "Z"]
        }

        with pytest.raises(ValueError) as e:
            get_stable_matches(proposer_to_preferences, receiver_to_preferences)
            assert str(e.value) == "Receiver Preference list of proposers must include all receivers"

    def test_missing_proposer(self):
        proposer_to_preferences = {
            "X": ["A", "B", "C"],
            "Y": ["B", "A", "C"],
            "Z": ["A", "B", "C"]
        }

        receiver_to_preferences = {
            "A": ["Y", "X", "Z"],
            "B": ["X", "Z", "Z"],
            "C": ["X", "Y", "Z"]
        }

        with pytest.raises(ValueError) as e:
            get_stable_matches(proposer_to_preferences, receiver_to_preferences)
            assert str(e.value) == "Proposer Preference list of receivers must include all proposers"

    def test_get_stable_matches_simple_preferences(self):
        proposer_to_preferences = {
            "X": ["A", "B", "C"],
            "Y": ["B", "A", "C"],
            "Z": ["A", "B", "C"]
        }

        receiver_to_preferences = {
            "A": ["Y", "X", "Z"],
            "B": ["X", "Y", "Z"],
            "C": ["X", "Y", "Z"]
        }

        expected_matches = {
            ("X", "A"),
            ("Y", "B"),
            ("Z", "C")
        }

        actual_matches = get_stable_matches(proposer_to_preferences, receiver_to_preferences)

        assert len(actual_matches) == 3
        assert actual_matches == expected_matches

    def test_get_stable_matches_with_replacement(self):
        # X matches with A, Y matches with B, Z matches with B replacing Y, Y matches with C
        proposer_to_preferences = {
            "X": ["A", "B", "C"],
            "Y": ["B", "A", "C"],
            "Z": ["A", "B", "C"]
        }

        receiver_to_preferences = {
            "A": ["X", "Y", "Z"],
            "B": ["X", "Z", "Y"],
            "C": ["X", "Y", "Z"]
        }

        expected_matches = {
            ("X", "A"),
            ("Z", "B"),
            ("Y", "C")
        }

        actual_matches = get_stable_matches(proposer_to_preferences, receiver_to_preferences)

        assert len(actual_matches) == 3
        assert actual_matches == expected_matches