from src.binary_search.binary_search import binary_search
import pytest

class TestBisect:
    def test_basic_functionality(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        condition = lambda x: x < 5
        result = binary_search(array, condition)
        assert result == 4

    def test_empty_array(self):
        array = []
        condition = lambda x: x < 5
        with pytest.raises(ValueError):
            binary_search(array, condition)

    def test_none_condition(self):
        array = [1, 2, 3]
        with pytest.raises(ValueError):
            binary_search(array, None)

    def test_invalid_condition_type(self):
        array = [1, 2, 3]
        with pytest.raises(ValueError):
            binary_search(array, "not_a_function")

    def test_left_greater_than_right(self):
        array = [1, 2, 3]
        condition = lambda x: x > 1
        with pytest.raises(ValueError):
            binary_search(array, condition, l=3, r=1)

    def test_invalid_range(self):
        array = [1, 2, 3]
        condition = lambda x: x > 1
        with pytest.raises(ValueError):
            binary_search(array, condition, l=-1)

    def test_array_none(self):
        array = None
        condition = lambda x: x < 5
        with pytest.raises(ValueError):
            binary_search(array, condition)

    def test_single_element_array(self):
        array = [10]
        condition = lambda x: x < 5
        result = binary_search(array, condition)
        assert result == 0

    def test_all_elements_satisfy_condition(self):
        array = [1, 2, 3, 4, 5]
        condition = lambda x: x < 6
        result = binary_search(array, condition)
        assert result == len(array)

    def test_no_elements_satisfy_condition(self):
        array = [1, 2, 3, 4, 5]
        condition = lambda x: x > 5
        result = binary_search(array, condition)
        assert result == 0

    def test_custom_left_and_right_values(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8]
        condition = lambda x: x < 5
        result = binary_search(array, condition, l=2, r=6)
        assert result == 4

    def test_bisect_left(self):
        array = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8]
        condition = lambda x: x < 5
        result = binary_search(array, condition)
        assert result == 4

    def test_bisect_right(self):
        array = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8]
        condition = lambda x: x <= 5
        result = binary_search(array, condition)
        assert result == 7