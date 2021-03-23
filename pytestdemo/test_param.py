import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize('a,b,expect', [
    [1, 2, 3], [0.1, 0.2, 0.3], [1, 0, 1]
], ids=['int', 'floar', '0'])
def test_add(a, b, expect):
    assert add(a, b) == expect


def test_add1():
    assert add(0.1, 0.2) == 0.3


@pytest.mark.parametrize('a', [[1, 2], [3, 4]])
def test_a(a):
    print(a)
