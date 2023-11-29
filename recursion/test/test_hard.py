from recursion.task_hard import create_hooks


def test_1():
    data = create_hooks(5)
    assert data[0] == "((((()))))"
    assert data[1] == "()()()()()"
