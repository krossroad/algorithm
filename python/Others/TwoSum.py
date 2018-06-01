def two_sum_naive(nums, target):
    index_mapper = {}

    for index, num in enumerate(nums):
        if num in index_mapper:
            return [index_mapper[num], index]

        index_mapper[target - num] = index

    return []
