def knapsack_naive(values, weights, W):
    if W <= 0 or len(values) == 0 or len(weights) == 0:
        return 0

    value = values[0]
    weight = weights[0]
    values = values[1:]
    weights = weights[1:]

    value_including = (value + knapsack_naive(values, weights, W - weight)) if W >= weight else 0
    value_excluding = knapsack_naive(values, weights, W)

    return max(value_including, value_excluding)


def knapsack_dp(values, weights, W):
    if 0 == W:
        return 0

    sequence_size = len(values)
    T = [[0 for _ in range(W + 1)] for _ in range(sequence_size + 1)]

    for i in xrange(1, sequence_size + 1):
        for j in xrange(1, W + 1):
            if j < weights[i - 1]:
                T[i][j] = T[i - 1][j]

            else:
                T[i][j] = max(T[i - 1][j], values[i - 1] + T[i - 1][j - weights[i - 1]])

    return T[sequence_size][W]
