
def SumOfThe(N: int, data: list[int]) -> int:

    for i in range(N):
        temp_list = data[:]
        value = temp_list.pop(i - 1)
        summ = sum(temp_list)
        if summ == value:
            return value
