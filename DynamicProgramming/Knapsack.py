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
