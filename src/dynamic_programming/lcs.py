def lcs_memoized(sequence_1, sequence_2):
    def helper(sequence_1, i, sequence_2, j, memo):
        key = (i, j)
        if key in memo:
            return memo[key]
        if i >= len(sequence_1) or j >= len(sequence_2):
            memo[key] = 0
        elif sequence_1[i] == sequence_2[j]:
            memo[key] = 1 + helper(sequence_1, i + 1, sequence_2, j + 1, memo)
        else:
            memo[key] = max(
                helper(sequence_1, i + 1, sequence_2, j, memo),
                helper(sequence_1, i, sequence_2, j + 1, memo)
            )
        return memo[key]
    return helper(sequence_1, 0, sequence_2, 0, {})

def lcs_dp(sequence_1, sequence_2):
    memo = [[0 for _ in range(len(sequence_2) + 1)] for _ in range(len(sequence_1) + 1)]
    for i in range(1, len(sequence_1) + 1):
        for j in range(len(sequence_2) - 1, -1, -1):
            if sequence_1[i - 1] == sequence_2[len(sequence_2) - j - 1]:
                memo[i][j] = 1 + memo[i - 1][j + 1]
            else:
                memo[i][j] = max(memo[i][j + 1], memo[i - 1][j])
    i = len(sequence_1)
    j = 0
    lcs = ""
    while i > 0 and j < len(sequence_2):
        if sequence_1[i - 1] == sequence_2[len(sequence_2) - j - 1]:
            lcs += sequence_1[i - 1]
            j += 1
            i -= 1
        elif memo[i - 1][j] > memo[i][j + 1]:
            i -= 1
        else:
            j += 1
    return lcs[::-1]
