def fact(number: int) -> int:
    if number == 1 or number == 0:
        return 1
    else:
        return number * fact(number - 1)


def squirrel(number: int) -> int:
    factorial = fact(number)
    return int(str(factorial)[0])

