def three_sum_slow(nums):
    result = set()
    input_size = len(nums)

    for i in range(input_size - 2):
        for j in range(i + 1, input_size - 1):
            for k in range(j + 1, input_size):
                if nums[i] + nums[j] + nums[k] == 0:
                    result.add(
                        tuple(sorted([nums[i], nums[j], nums[k]]))
                    )

    return map(list, result)


def three_sum_faster(nums):
    nums.sort()
    array_size = len(nums)
    result = set()

    for i in range(array_size - 1):
        head = i + 1
        tail = array_size - 1

        while (head < tail):
            current_sum = nums[head] + nums[tail] + nums[i]
            if current_sum == 0:
                result.add((nums[i], nums[head], nums[tail]))
                head += 1
                tail -= 1
            elif current_sum < 0:
                head += 1
            else:
                tail -= 1

    return map(list, result)
