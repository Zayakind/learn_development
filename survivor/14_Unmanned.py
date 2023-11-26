class TrafficLight(object):

    def __init__(self, red_gisnal, green_signal):
        self.red = "red"
        self.green = "green"
        self.signal = self.red
        self.time_red = red_gisnal
        self.time_green = green_signal
        self.time_signal = self.time_red

    def check(self):
        return self.signal

    def run(self):
        self.time_signal -= 1

        if self.time_signal != 0:
            return

        if self.signal == self.red:
            self.signal = self.green
            self.time_signal = self.time_green
            return

        if self.signal == self.green:
            self.signal = self.red
            self.time_signal = self.time_red
            return


def created_track(lens: int, traffic_light: list[list[int]]) -> list[int, dict]:
    track = [1] * lens
    for lights in traffic_light:
        index = lights[0]
        if 0 < index <= lens:
            track[index - 1] = TrafficLight(lights[1], lights[2])

    return track


def run_traffic_light(traffic_light: list[list[int]], track):

    for value in traffic_light:
        if isinstance(track[value[0] - 1], TrafficLight):
            track[value[0] - 1].run()


def check_traffic_light(track: list[int, dict]) -> bool:

    for item in track:
        if isinstance(item, TrafficLight):
            return True
    return False


def Unmanned(L: int, N: int, track: list[list[int]]) -> int:
    result_track = created_track(L, track)
    time_to_path = 0
    section = 0

    while section < L:

        section += 1
        if check_traffic_light(result_track):
            run_traffic_light(track, result_track)
        road_section = result_track[section - 1]
        check_traffic_light(result_track)

        if not isinstance(road_section, TrafficLight):
            result_track[section - 1] = 0
            time_to_path += 1
            continue

        if road_section.signal == 'red':
            time_to_path += 1
            section -= 1
            continue

        result_track[section - 1] = 0
        time_to_path += 1

    return time_to_path
