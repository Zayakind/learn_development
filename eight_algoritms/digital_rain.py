def digital_rain(col: str) -> str:
    n = len(col)
    diffcount = {0: -1}
    presum = 0
    ansmaxlen = -1

    for i in range(n):
        presum += 1 if col[i] == '1' else -1

        if presum in diffcount:
            ansmaxlen = max(ansmaxlen, i - diffcount[presum])
            continue
        diffcount[presum] = i

    if ansmaxlen > 0:
        return col[-ansmaxlen:]
    return ""
