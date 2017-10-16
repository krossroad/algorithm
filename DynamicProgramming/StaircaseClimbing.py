def get_stair_cases_naive(n):
    if n <= 0:
        return 0
    elif n <= 1:
        return 1
    elif n <= 2:
        return 2

    return get_stair_cases_naive(n - 1) \
           + get_stair_cases_naive(n - 2)


def get_stair_cases_dp(n):
    if n <= 0:
        return 0
    elif n <= 1:
        return 1
    elif n <= 2:
        return 2

    previous = 1
    current = 2

    for i in xrange(3, n):
        next_val = previous + current
        previous = current
        current = next_val

    return previous + current
