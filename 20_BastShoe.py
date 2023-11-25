class Lapot:

    def __init__(self):
        self.str_now = ""
        self.history = []
        self.undo_chain = []
        self.redo_chain = []
        self.last_operation = ""

    def add(self, add_string: str) -> None:
        self._check_operation()
        result = f"{self.str_now}{add_string}"
        self.undo_chain.append(["1", {"old": self.str_now, "new": result}])
        self.str_now = result

    def delete(self, count: int) -> None:
        self._check_operation()
        result = self.str_now[:(-count)]
        if count > len(self.str_now):
            self.undo_chain.append(["2", {"old": self.str_now, "new": ""}])
            self.str_now = ""
            return
        self.undo_chain.append(["2", {"old": self.str_now, "new": result}])
        self.str_now = result

    def issue(self, index: int) -> str:
        if index > len(self.str_now):
            return ""
        return self.str_now[index]

    def undo(self) -> None:
        result = self.undo_chain[0]
        if len(self.undo_chain) > 1:
            result = self.undo_chain.pop(-1)
        self.str_now = result[1]["old"]
        self.redo_chain.append(result)

    def redo(self) -> None:
        result = self.redo_chain.pop(-1)
        self.str_now = result[1]["new"]

    def _check_operation(self) -> None:
        if self.last_operation == "4":
            self.undo_chain = self.undo_chain[-1]
            self.redo_chain.clear()

    def now_operation(self, operation: str) -> None:
        lapot.last_operation = operation
        lapot.history.append(operation)


lapot = Lapot()


def BastShoe(command: str) -> str:

    if len(command) > 1:
        numb_command, changed = command.split(' ', 1)
    else:
        numb_command, changed = command, ""

    match numb_command:
        case "1":
            lapot.now_operation("1")
            lapot.add(changed)
            return lapot.str_now
        case "2":
            lapot.now_operation("2")
            lapot.delete(int(changed))
            return lapot.str_now
        case "3":
            lapot.now_operation("3")
            return lapot.issue(int(changed))
        case "4":
            lapot.now_operation("4")
            lapot.undo()
            return lapot.str_now
        case "5":
            lapot.now_operation("5")
            lapot.redo()
            return lapot.str_now
        case _:
            return lapot.str_now


# BastShoe("1 Привет")
# BastShoe("1 , Мир!")
# BastShoe("1 ++")
# BastShoe("2 2")
# BastShoe("4")
# BastShoe("4")
# BastShoe("1 *")
# BastShoe("4")
# BastShoe("4")
# BastShoe("4")
# BastShoe("3 6")
# BastShoe("2 100")
# BastShoe("1 Привет")
# BastShoe("1 , Мир!")
# BastShoe("1 ++")
# BastShoe("4")
# BastShoe("4")
# BastShoe("5")
# BastShoe("4")
# BastShoe("5")
# BastShoe("5")
# BastShoe("5")
# BastShoe("5")
# BastShoe("4")
# BastShoe("4")
# BastShoe("2 2")
# BastShoe("4")
# BastShoe("5")
# BastShoe("5")
# print(BastShoe("5"))
# print(BastShoe(""))
# print(BastShoe(""))
# print(BastShoe(""))
# print(BastShoe(""))
# print(BastShoe(""))
# print(BastShoe(""))
# print(BastShoe(""))
# print(BastShoe(""))
