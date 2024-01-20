
def sort_list(data: dict) -> list[str]:

    data = sorted(data.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)

    while True:
        is_excess = False
        for index, (key, value) in enumerate(data):
            if index > 0 and data[index - 1][0] > key and data[index - 1][1] == value:
                data.insert(index, data.pop(index - 1))
                is_excess = True

        if not is_excess:
            break

    result = []

    for item in data:
        result.append(f"{item[0]} {item[1]}")

    return result


def ShopOLAP(N: int, items: list[str]) -> list[str]:

    temp_dict = {}

    for item in items:
        itm, sale = item.split(' ')
        if temp_dict.get(itm):
            temp_dict[itm] += int(sale)
            continue
        temp_dict[itm] = int(sale)

    result = sort_list(temp_dict)

    return result
