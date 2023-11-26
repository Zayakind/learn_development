
def MaximumDiscount(N: int, price: list[int]) -> int:

    count_sale = N // 3
    summ_sale = 0
    price.sort(reverse=True)

    for pack in range(count_sale):
        temp = [price[item] for item in range(3)]
        [price.remove(item) for item in temp]
        summ_sale += temp[-1]

    return summ_sale

