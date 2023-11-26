def switch_door(door: str) -> str:
    return '1' if door == '0' else '0'


def Keymaker(count_door: int) -> str:
    doors = ['0' for _ in range(count_door)]

    for step in range(1, count_door + 1):
        for i in range(step - 1, count_door, step):
            doors[i] = switch_door(doors[i])
    return ''.join(doors)
