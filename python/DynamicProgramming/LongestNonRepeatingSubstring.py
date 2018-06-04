def lnr_substring_optimized(input_str):
    max_result = start = 0
    holder = {}

    for index, char in enumerate(input_str):
        if char in holder and start <= holder[char]:
            start = holder[char] + 1
        else:
            max_result = max(max_result, index - start + 1)
        holder[char] = index

    return max_result


def lnr_substring_naive(input_str):
    input_size = len(input_str)

    if input_size == 0:
        return 0

    max_result = 1

    for i in range(input_size - 1):
        holder = {input_str[i]: 1}
        current_max = 1

        for j in range(i + 1, input_size):
            if input_str[j] in holder:
                break

            current_max += 1
            holder[input_str[j]] = 1

        max_result = max(current_max, max_result)

    return max_result
