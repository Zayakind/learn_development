def massdriver(activate: list[int]):
    nums = {}
    len_activate = len(activate)

    for i, num in enumerate(activate):
        if num in nums:
            if nums[num] < len_activate:
                len_activate = nums[num]
            continue
        nums[num] = i
    if len_activate == len(activate):
        return -1
    return len_activate
