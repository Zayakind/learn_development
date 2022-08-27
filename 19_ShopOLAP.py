
def ShopOLAP(N: int, items: list[str]) -> list[str]:

    result = []
    temp_dict = {}

    for item in items:
        itm, sale = item.split(' ')
        if temp_dict.get(itm):
            temp_dict[itm] += int(sale)
            continue
        temp_dict[itm] = int(sale)

    temp_dict = {key: value for key, value in sorted(temp_dict.items(), key=lambda item: item[1], reverse=True)}

    for key, value in temp_dict.items():
        result.append(f'{key} {value}')

    return result
