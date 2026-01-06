import random

def get_partition(array, start_idx, end_idx):
    # works well on duplicate elements, where regular quicksort degrades to quadratic performance due to bad partitions
    lt = start_idx
    eq = start_idx
    gt = end_idx
    pivot = array[random.randint(start_idx, end_idx)]
    while eq <= gt:
        if array[eq] == pivot:
            eq += 1
        elif array[eq] > pivot:
            array[eq], array[gt] = array[gt], array[eq]
            gt -= 1
        else:
            array[eq], array[lt] = array[lt], array[eq]
            eq += 1
            lt += 1
    return lt - 1, gt + 1

def sort(array):
    def quick_sort(array, start_idx, end_idx):
        if start_idx < end_idx:
            l, r = get_partition(array, start_idx, end_idx)
            quick_sort(array, start_idx, l)
            quick_sort(array, r, end_idx)
    quick_sort(array, 0, len(array) - 1)

def select(array, k):
    """Return the k-th smallest element (0-indexed) using quickselect."""
    if k < 0 or k >= len(array):
        return None

    l, r = 0, len(array) - 1

    while l <= r:
        left_end, right_start = get_partition(array, l, r)

        # equal region is [left_end + 1 .. right_start - 1]
        eq_l = left_end + 1
        eq_r = right_start - 1

        if k < eq_l:
            r = left_end              # search in "< pivot"
        elif k > eq_r:
            l = right_start           # search in "> pivot"
        else:
            # k is inside the "== pivot" block
            return array[k]