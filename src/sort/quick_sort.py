import random

def sort(array):
    def get_partition(array, start_idx, end_idx):
        pivot_idx = random.randint(start_idx, end_idx)
        pivot = array[pivot_idx]
        array[pivot_idx], array[end_idx] = array[end_idx], array[pivot_idx]
        i = start_idx - 1
        for j in range(start_idx, end_idx):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[end_idx] = array[end_idx], array[i + 1]
        return i + 1

    def quick_sort(array, start_idx, end_idx):
        if start_idx < end_idx:
            partition = get_partition(array, start_idx, end_idx)
            quick_sort(array, start_idx, partition - 1)
            quick_sort(array, partition + 1, end_idx)

    quick_sort(array, 0, len(array) - 1)
