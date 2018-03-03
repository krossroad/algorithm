def calc_longest_common_sub_sequence_naive(sequence1, sequence2):
    size1 = len(sequence1)
    size2 = len(sequence2)

    def looper(seq1, seq2, i, j):
        if i < 0 or j < 0:
            return 0

        return 1 + looper(seq1, seq2, i - 1, j - 1) if seq1[i] == seq2[j] \
            else max(looper(seq1, seq2, i - 1, j), looper(seq1, seq2, i, j - 1))

    return looper(sequence1, sequence2, size1 - 1, size2 - 1)


def calc_longest_common_sub_sequence_dp(seq1, seq2):
    size1 = len(seq1)
    size2 = len(seq2)

    P = [[0 for _ in xrange(size1 + 1)] for _ in xrange(size2 + 1)]

    for i in xrange(1, size2 + 1):
        for j in xrange(1, size1 + 1):
            P[i][j] = (1 + P[i - 1][j - 1]) if seq1[i - 1] == seq2[j - 1] \
                else max(P[i - 1][j], P[i][j - 1])

    return P[size2][size1]