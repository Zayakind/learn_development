def summ(num: int):
    if num < 9:
        return num
    return num % 10 + summ(num // 10)
