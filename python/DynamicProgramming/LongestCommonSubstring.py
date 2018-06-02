import sys


def longest_common_substring_naive(input_str, test_str):
    def looper(i, j, acc):
        if i < 0 or j < 0:
            return acc

        if input_str[i] == test_str[j]:
            return looper(i - 1, j - 1, acc + 1)
        elif acc > 0:
            return acc
        else:
            return max(looper(i - 1, j, acc), looper(i, j - 1, acc))

    return looper(len(input_str) - 1, len(test_str) - 1, 0)


def longest_common_substring_dp(input_str, test_str):
    input_size = len(input_str)
    test_size = len(test_str)

    P = [[0 for _ in range(input_size + 1)] for _ in range(test_size + 1)]
    max_length = 0
    last_index = -1

    for i in xrange(1, input_size + 1):
        for j in xrange(1, test_size + 1):
            if input_str[i - 1] == test_str[j - 1]:
                P[i][j] = 1 + P[i - 1][j - 1]
                max_length = max(max_length, P[i][j])
                last_index = i
            else:
                P[i][j] = 0

    return max_length
