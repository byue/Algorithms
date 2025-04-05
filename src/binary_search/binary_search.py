# Returns index at index where condition first fails
def binary_search(array, condition, l=0, r=None):
    if array is not None and not r:
        r = len(array)
    if array is None or condition is None or not callable(condition) or l < 0 or l > r or l >= len(array) or r < 0 or r > len(array):
        raise ValueError()
    while l < r:
        m = l + (r - l) // 2
        if condition(array[m]):
            l = m + 1
        else:
            r = m
    return l
