def subset_sum_naive(items, start, end, S):
    if S == 0:
        return True

    if len(items) > 0 and items[start] == S:
        return True

    S -= items[start]

    for i in xrange(start + 1, end):
        if subset_sum_naive(items, i, end, S - items[i]):
            return True

    return False


def subset_sum_dp(sequence, S):
    cols = S + 1  # Plus 1 for 0 valued col.
    rows = len(sequence) + 1  # Plus 1 for 0 valued row.
    T = [[False for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        T[row][0] = True

    for index_i in range(1, rows):
        for index_j in range(1, cols):
            if index_j >= sequence[index_i - 1]:
                T[index_i][index_j] = T[index_i - 1][index_j] or T[index_i - 1][index_j - sequence[index_i - 1]]
            else:
                T[index_i][index_j] = T[index_i - 1][index_j]

    return T[rows - 1][cols - 1]


def array_partition_dp(sequence):
    if len(sequence) == 0:
        return False

    seq_size = len(sequence)
    seq_sum = sum(sequence)

    return not (seq_sum & 1) and subset_sum_dp(sequence, seq_size / 2)
