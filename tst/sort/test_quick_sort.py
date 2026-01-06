from src.sort.quick_sort import select, sort

class TestQuickSort:
    def test_empty_sort(self):
        array = []
        sort(array)
        assert array == []

    def test_sorted_and_reverse_inputs(self):
        sorted_array = [1, 2, 3, 4, 5]
        reverse_array = list(reversed(sorted_array))
        sort(sorted_array)
        sort(reverse_array)
        assert sorted_array == [1, 2, 3, 4, 5]
        assert reverse_array == [1, 2, 3, 4, 5]

    def test_duplicates_and_negatives(self):
        array = [3, -1, 0, -1, 5, 3, 2]
        sort(array)
        assert array == [-1, -1, 0, 2, 3, 3, 5]

    def test_random_pivot_usage(self, monkeypatch):
        calls = []

        def fake_randint(start_idx, end_idx):
            calls.append((start_idx, end_idx))
            return start_idx  # pick first element to force swaps with pivot

        monkeypatch.setattr("src.sort.quick_sort.random.randint", fake_randint)
        array = [10, 5, 8, 3, 2]
        sort(array)
        assert array == [2, 3, 5, 8, 10]
        assert calls[0] == (0, 4)
        assert all(start <= end for start, end in calls)

    def test_select_basic(self):
        array = [7, 1, 5, 3, 9, 2]
        assert select(array[:], 0) == 1
        assert select(array[:], 3) == 5
        assert select(array[:], 5) == 9

    def test_select_with_duplicates(self):
        array = [4, 2, 5, 2, 3, 4, 1]
        assert select(array[:], 0) == 1
        assert select(array[:], 2) == 2
        assert select(array[:], 4) == 4

    def test_select_invalid_index(self):
        array = [10, 20, 30]
        assert select(array[:], -1) is None
        assert select(array[:], 3) is None
