def MadMax(N: int, Tele: list[int]) -> list[int]:
    Tele.sort()
    middle = N // 2
    one, two = Tele[:middle], Tele[middle:]
    two.reverse()
    one.extend(two)
    return one

