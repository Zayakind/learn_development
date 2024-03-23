from typing import List


def depth_result_array(data_array: List) -> int:
    depth_tree = 0
    len_tree = 0
    while len_tree < len(data_array):
        depth_tree += 1
        len_tree = 2 ** (depth_tree + 1) - 1
    return depth_tree


def recursive_generate(in_array: List, out_array: List, index: int) -> None:
    if len(in_array) > 0:
        index_mid = len(in_array) // 2
        out_array[index] = in_array[index_mid]
        recursive_generate(in_array[:index_mid], out_array, 2 * index + 1)
        recursive_generate(in_array[index_mid + 1:], out_array, 2 * index + 2)


def GenerateBBSTArray(bst_array: List) -> List:
    bst_array.sort()
    depth = depth_result_array(bst_array)
    result_array = [None] * (2 ** (depth + 1) - 1)
    recursive_generate(bst_array, result_array, 0)
    return result_array
