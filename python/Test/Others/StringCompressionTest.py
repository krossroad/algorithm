import unittest


def string_compress(input_str):
    input_len = len(input_str)
    i = -1
    counter = [0] * input_len
    characters = [None] * input_len

    for j, c in enumerate(input_str):
        if j != 0 and c == input_str[j - 1]:
            counter[i] += 1
        else:
            i += 1
            characters[i] = c
            counter[i] += 1

    result = ""
    for i, char in enumerate(characters):
        if char is None:
            break
        result += char + str(counter[i])

    return result


class StringCompressionTest(unittest.TestCase):

    def test_should_run(self):
        string_compress("")

    def test_should_return(self):
        self.assertEqual("a1", string_compress("a"))
        self.assertEqual("a2b1c5a3", string_compress("aabcccccaaa"))
