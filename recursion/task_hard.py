def create_hooks(count_hooks: int, data: list[str] = None) -> list[str]:
    if not data:
        data = ["", ""]
    if count_hooks == 0:
        return data
    count_hooks -= 1
    data[0], data[1] = "(" + data[0] + ")", data[1] + "()"
    return create_hooks(count_hooks, data)
