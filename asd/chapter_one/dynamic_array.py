import ctypes
from typing import Any


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    @property
    def fill_percent(self):
        return self.count / self.capacity * 100

    def to_list(self):
        array, end = [], False
        try:
            for v in self.array:
                array.append(v)
        except ValueError:
            pass
        except IndexError:
            pass
        return array

    @property
    def meta(self):
        return (self.to_list(), self.count,
                self.capacity, self.fill_percent)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity: int):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i: int) -> None:
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity: int) -> None:
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm: Any) -> None:
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i: int, itm: Any) -> None:
        if self.count == i:
            self.append(itm)
            return
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        count = self.count + 1
        if count > self.capacity:
            self.resize(2 * self.capacity)
        move_forward_indices = list(range(i, self.count))
        for ind in move_forward_indices[::-1]:
            self.array[ind + 1] = self.array[ind]
        self.count = self.count + 1
        self.array[i] = itm

    def delete(self, i: int) -> None:
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        move_back_indices = list(range(i + 1, self.count))
        for ind in move_back_indices:
            self.array[ind - 1] = self.array[ind]
        self.count -= 1
        capacity = self.capacity
        if self.capacity > 16 and self.fill_percent <= 50:
            capacity = int(self.capacity / 1.5)
        if capacity > 16:
            self.resize(capacity)
            return
        self.resize(16)
