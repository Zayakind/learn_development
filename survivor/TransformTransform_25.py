def cicle_transform(nums: list) -> list:
    result = []
    for i in range(len(nums)):
        result.extend(
            [max(nums[j:i + j + 1]) for j in range(len(nums) - i)]
        )
    return result


def TransformTransform(nums: list[int], num_b: int) -> bool:
    return sum(cicle_transform(cicle_transform(nums))) % 2 == 0
