def cicle_transform(nums: list) -> list:
    output_transform = []
    for i in range(len(nums)):
        output_transform.extend(
            [max(nums[j:i + j + 1]) for j in range(len(nums) - i)]
        )
    return output_transform


def TransformTransform(nums: list[int], num_b: int) -> bool:
    return sum(cicle_transform(cicle_transform(nums))) % 2 == 0
