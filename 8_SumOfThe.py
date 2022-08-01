
def SumOfThe(N: int, data: list[int]) -> int:
    summ = 0
    for numb in data[:-1]:
        summ += numb

    if summ == data[N - 1]:
        return summ
