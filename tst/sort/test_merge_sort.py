from src.sort.merge_sort import sort


class TestMergeSort:
    def test_empty_array(self):
        data = []
        sort(data)
        assert data == []

    def test_single_element(self):
        data = [42]
        sort(data)
        assert data == [42]

    def test_sorted_and_reverse_inputs(self):
        sorted_array = [1, 2, 3, 4, 5]
        reverse_array = list(reversed(sorted_array))
        sort(sorted_array)
        sort(reverse_array)
        assert sorted_array == [1, 2, 3, 4, 5]
        assert reverse_array == [1, 2, 3, 4, 5]

    def test_mixed_values(self):
        data = [5, -1, 3, 0, 3, 2, -5]
        sort(data)
        assert data == [-5, -1, 0, 2, 3, 3, 5]

    def test_duplicates_preserved(self):
        data = ["b", "a", "c", "a", "b", "a"]
        sort(data)
        assert data == ["a", "a", "a", "b", "b", "c"]
