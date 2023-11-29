def even_numbers(data: list, n: int = 0):
    if n == len(data):
        return False
    if data[n] % 2 == 0:
        print(data[n], end=" ")
    data.pop(0)
    even_numbers(data, n + 1)
