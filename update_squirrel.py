def squirrel(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    while factorial > 10:
        factorial = factorial // 10
    return factorial
