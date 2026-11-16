from calc import add, average


def test_add():
    assert add(2, 3) == 5


def test_average():
    assert average([1, 2, 3]) == 2
