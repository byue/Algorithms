def lis_memoized(sequence):
    def helper(sequence, i, memo):
        if i in memo:
            return memo[i]
        if i == 0:
            memo[i] = 1
        else:
            result = 1
            for j in range(i, len(sequence)):
                if sequence[j] > sequence[i]:
                    result = max(result, 1 + helper(sequence, j, memo))
            memo[i] = result
        return memo[i]
    result = 0
    memo = {}
    for i in range(len(sequence) - 1, -1, -1):
        result = max(result, helper(sequence, i, memo))
    return result

def lis_dp(sequence):
    if not sequence:
        return 0
    memo = [1] * len(sequence)
    for i in range(len(sequence) - 1, -1, -1):
        for j in range(i + 1, len(sequence)):
            if sequence[j] > sequence[i]:
                memo[i] = max(memo[i], memo[j] + 1)
    return max(memo)

def lis_binary(sequence):
    buckets = []
    for num in sequence:
        l = 0
        r = len(buckets) - 1
        while l <= r:
            m = (l + r) // 2
            if num >= buckets[m]:
                l = m + 1
            else:
                r = m - 1
        if l >= len(buckets):
            buckets.append(num)
        else:
            buckets[l] = num
    return len(buckets)

