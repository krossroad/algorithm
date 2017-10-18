import sys


def rod_cutting_naive(lengths, profits, rod_length):
    if len(lengths) == 0 or len(profits) == 0 or rod_length <= 0:
        return 0

    max_value = -sys.maxint

    for key, length in enumerate(lengths):
        if rod_length < length:
            continue
        max_value = max(profits[key] + rod_cutting_naive(lengths, profits, rod_length - length), max_value)

    return max_value


def rod_cutting_dp(lengths, profits, rod_length):
    if len(profits) == 0:
        return 0

    if rod_length <= 0:
        return 0

    T = [0 for _ in xrange(rod_length + 1)]

    for i in xrange(1, rod_length + 1):
        for j in xrange(1, i + 1):
            T[i] = max(T[i], profits[j - 1] + T[i - j])

    return T[rod_length]
