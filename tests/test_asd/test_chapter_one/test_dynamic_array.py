from asd.chapter_one.dynamic_array import DynArray


def test_one():
    dyn = DynArray()
    [dyn.insert(i, i) for i in range(25)]
    [dyn.delete(1) for i in range(15)]
