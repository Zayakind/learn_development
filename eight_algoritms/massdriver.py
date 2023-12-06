def massdriver(activate: list[int]):
    nums = {}

    for i, num in enumerate(activate):
        if num in nums:
            return nums[num]
        nums[num] = i
    return -1
