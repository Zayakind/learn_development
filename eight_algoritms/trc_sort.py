def sort_recursive(trc: list[int], Lo=0, Mid=0, Hi=0) -> list[int]:
    if Hi == 0:
        Hi = len(trc) - 1
    if Mid > Hi:
        return trc

    if trc[Mid] == 0:
        trc[Mid], trc[Lo] = trc[Lo], trc[Mid]
        return sort_recursive(trc, Lo + 1, Mid + 1, Hi)
    elif trc[Mid] == 1:
        return sort_recursive(trc, Lo, Mid + 1, Hi)
    elif trc[Mid] == 2:
        trc[Mid], trc[Hi] = trc[Hi], trc[Mid]
        return sort_recursive(trc, Lo, Mid, Hi - 1)


def TRC_sort(trc: list[int]) -> list[int]:
    return sort_recursive(trc)
