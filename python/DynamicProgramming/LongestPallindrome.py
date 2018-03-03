def is_palindrome(tst_str, start=0, end=None):
    end = end if end else (len(tst_str) - 1)

    if end == start:
        return True

    return tst_str[start] == tst_str[end] and is_palindrome(tst_str, start + 1, end - 1)


def get_longest_palindrome_naive(plain_text):
    str_size = len(plain_text)

    if str_size < 2:
        return ""

    lp = ""
    lp_len = 0

    for j in range(0, str_size - 1):
        for i in range(j + 1, str_size):
            tst_str = ''.join(plain_text[j:i + 1])
            tst_str_len = (i - j)
            if is_palindrome(tst_str) and tst_str_len > lp_len:
                lp = tst_str
                lp_len = tst_str_len

    return lp


def get_longest_palindrome_dp():
    return ""
