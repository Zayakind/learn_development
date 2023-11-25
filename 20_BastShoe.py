

class Example:

    def __init__(self):
        self.str_now = ""
        self.history_changes = []
        self.history_undo = []
        self.undo_index = 0
        self.history = []
        self.redo_index = 0

    def _save_history(self, numb_command, will_be):

        self.history.append(numb_command)

        if len(self.history) > 2 and self.history[-2] == "4" and self.history[-1] in "12":
            self.history_changes.clear()
            self.history.clear()
            self.history_undo.clear()
            self.history_changes.append([numb_command, self.str_now, will_be])
            self.undo_index = 0
            self.history.append(numb_command)
            self.history_undo.append([numb_command, self.str_now, will_be])
            return

        self.history_changes.append([numb_command, self.str_now, will_be])

    def add(self, changed):

        temp = f"{self.str_now}{changed}"
        self._save_history('1', temp)
        self.str_now = temp

    def delete(self, count):

        if int(count) > len(self.str_now):
            self._save_history('2', "")
            self.str_now = ""
            return self.str_now

        temp = f"{self.str_now[:-int(count)]}"
        self._save_history('2', temp)
        self.str_now = temp

    def issue(self, index):

        return self.str_now[int(index)]

    def undo(self):

        for index, value in enumerate(self.history_changes[::-1]):
            if ('1' in value or '2' in value) and index >= self.undo_index:
                self.history_undo.append(value)
                self.history.append("4")
                self.str_now = value[1]
                self.undo_index += 1
                break

    def redo(self):

        if not self.history_undo:
            return self.str_now

        for index, value in enumerate(self.history_undo[::-1]):
            if index + 1 >= self.redo_index:
                self._save_history(value[0], value[2])
                self.str_now = value[2]
                self.redo_index += 1
                break


def BastShoe(command: str) -> str:
    example = Example()

    if len(command) > 1:
        numb_command, changed = command.split(' ', 1)
    else:
        numb_command, changed = command, "0"

    match numb_command:
        case "1":
            example.add(changed)
            return example.str_now
        case "2":
            example.delete(changed)
            return example.str_now
        case "3":
            return example.issue(changed)
        case "4":
            example.undo()
            return example.str_now
        case "5":
            example.redo()
            return example.str_now
        case _:
            return example.str_now
