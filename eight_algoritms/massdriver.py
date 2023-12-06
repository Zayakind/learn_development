def massdriver(activate: list[int]):
    nums = {}
    temp = len(activate)

    for i, num in enumerate(activate):
        if num in nums:
            if nums[num] < temp:
                temp = nums[num]
            continue
        nums[num] = i
    if temp == len(activate):
        return -1
    return temp
