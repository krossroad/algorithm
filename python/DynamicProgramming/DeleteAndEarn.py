def delete_and_run(nums):
    points = [0] * 1001
    for num in nums:
        points[num] += num

    prev, curr = 0, 0

    for point in points:
        prev, curr = curr, max(point + prev, curr)

    return curr