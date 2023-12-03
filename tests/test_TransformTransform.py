from survivor.TransformTransform_25 import TransformTransform


def test_1():
    assert not TransformTransform([1, 2, 3, 4, 5], 5)


def test_2():
    assert not TransformTransform([5, 7, 12, 1, 8], 5)


def test_3():
    assert not TransformTransform([1], 1)
