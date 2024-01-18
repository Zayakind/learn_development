def factorial_calculation(number: int) -> int:
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial_calculation(number - 1)


def squirrel(number: int) -> int:
    factorial = factorial_calculation(number)
    return int(str(factorial)[0])

