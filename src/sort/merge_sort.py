def sort(array):
    """Sorts array in-place using merge sort."""

    def merge_sort(start_idx, end_idx, buffer):
        if start_idx >= end_idx:
            return

        mid = (start_idx + end_idx) // 2
        merge_sort(start_idx, mid, buffer)
        merge_sort(mid + 1, end_idx, buffer)
        merge(start_idx, mid, end_idx, buffer)

    def merge(start_idx, mid, end_idx, buffer):
        buffer[start_idx : end_idx + 1] = array[start_idx : end_idx + 1]
        left = start_idx
        right = mid + 1
        current = start_idx

        while left <= mid and right <= end_idx:
            if buffer[left] <= buffer[right]:
                array[current] = buffer[left]
                left += 1
            else:
                array[current] = buffer[right]
                right += 1
            current += 1

        while left <= mid:
            array[current] = buffer[left]
            left += 1
            current += 1

        # elements from right half already in correct place

    if len(array) <= 1:
        return

    merge_sort(0, len(array) - 1, array[:])
