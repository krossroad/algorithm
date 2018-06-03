def longest_repeating_substring_dp(input_str):
    input_size = len(input_str)
    max_result = current_max = 1
    last_index = -1

    if input_size < 1:
        return 0

    for i in range(1, input_size):
        current_max = current_max + \
            1 if input_str[i] == input_str[i - 1] else 1
        if current_max > max_result:
            max_result = current_max
            last_index = i

    return max_result
