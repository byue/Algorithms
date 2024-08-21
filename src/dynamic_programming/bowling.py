# Given n pins 0,...,n-1
# Pin i has value v_i
# hit 1 pin, get v_i points
# hit 2 pins i, i+1, get v_i * v_i+1
# Return maximum score
def get_maximum_score_recursive(pin_values):
    def helper(pin_values, j): # j is the right boundary non-inclusive
        if j == 0: # empty case
            return 0
        if j == 1: # first pin
            return max(pin_values[0], 0)
        score_excluding_single = helper(pin_values, j - 1)
        score_excluding_pair = helper(pin_values, j - 2)
        return max(
            pin_values[j - 2] * pin_values[j - 1] + score_excluding_pair,
            pin_values[j - 1] + score_excluding_single,
            score_excluding_single
        )
    return helper(pin_values, len(pin_values))

def get_maximum_score_memoized(pin_values):
    def helper(pin_values, j, memo):
        if j in memo:
            return memo[j]
        if j == 0:
            memo[j] = 0
        elif j == 1:
            memo[j] = max(pin_values[0], 0)
        else:
            score_excluding_single = helper(pin_values, j - 1, memo)
            score_excluding_pair = helper(pin_values, j - 2, memo)
            memo[j] = max(
                pin_values[j - 2] * pin_values[j - 1] + score_excluding_pair,
                pin_values[j - 1] + score_excluding_single,
                score_excluding_single
            )
        return memo[j]
    return helper(pin_values, len(pin_values), {})

def get_maximum_score_dp(pin_values):
    memo = [0] * (len(pin_values) + 1)
    memo[0] = 0
    if len(pin_values) > 0:
        memo[1] = max(pin_values[0], 0)
    for j in range(2, len(pin_values) + 1):
        memo[j] = max(
            pin_values[j - 2] * pin_values[j - 1] + memo[j - 2],
            pin_values[j - 1] + memo[j - 1],
            memo[j - 1]
        )
    return memo[len(pin_values)]
