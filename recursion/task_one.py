def exponentiation(num: int | float, degree: int | float):
    if degree == 0:
        return 1
    if degree == 1:
        return num
    if degree == 2:
        return num * num
    if degree < 0:
        return 1 / (num * exponentiation(num, -degree - 1))
    if degree % 2 != 0:
        return num * exponentiation(num, degree - 1)
    return exponentiation(num, degree // 2)**2


print(exponentiation(3, 5))
