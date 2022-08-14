

def created_track(lens: int, traffic_light: list[list[int]]) -> list[int, dict]:
    track = [1] * lens
    for lights in traffic_light:
        index = lights[0]
        if 0 < index <= lens:
            track[index] = {'red': lights[1], 'green': lights[2]}

    return track


def Unmanned(L: int, N: int, track: list[list[int]]) -> int:

    track = created_track(L, track)
    time_to_path = 0
    section = 0
    while track[-1] != 0:
        section += 1
        road_section = track[section - 1]
        if not isinstance(road_section, dict):
            track[section - 1] = 0
            time_to_path += 1
            print(track, time_to_path)
            continue
        if time_to_path - road_section['red'] < 0:
            track[section - 1] = 0
            time_to_path += road_section['red'] - time_to_path + 1
            print(track, time_to_path)
            continue
        track[section - 1] = 0
        time_to_path += 1
        print(track, time_to_path)
        continue

    return time_to_path


print(Unmanned(10, 2, [[11, 5, 5], [15, 2, 2]]))
