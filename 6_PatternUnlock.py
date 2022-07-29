
def PatternUnlock(N: int, hits: list[int]) -> str:
    katet = ['12', '19', '16', '21', '28', '23', '25', '32', '34', '37', '45', '43', '56', '52', '54', '61', '65', '73',
             '78', '82', '87', '89', '91', '98']
    gipotenyza = ['15', '18', '26', '29', '27', '24', '35', '38', '42', '51', '53', '62', '72', '83', '81', '92']
    summ = 0.0

    for index in range(N):
        if index < N - 1:
            step = f'{hits[index]}{hits[index+1]}'
            if step in katet:
                summ += 1.0
            if step in gipotenyza:
                summ += 1.41421356237
    summ = str(round(summ, 5))
    result = ''
    for i in summ:
        if i in '123456789':
            result += i
    return result


hits = [1,2,3,4,5,6,2,7,8,9]
print(PatternUnlock(len(hits), hits))
