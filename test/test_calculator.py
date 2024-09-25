from .calculator import square
import pytest


def main():
    test_square_positive_2()
    test_square_positive_3()
    test_square_zero()
    test_square_negative_2()
    test_square_negative_3()
    test_square_million()
    test_str()


def test_square_positive_2():
    assert square(2) == 4


def test_square_positive_3():
    assert square(3) == 9


def test_square_zero():
    assert square(0) == 0


def test_square_negative_2():
    assert square(-2) == 4


def test_square_negative_3():
    assert square(-3) == 9


def test_square_million():
    assert square(1000000) == 1000000000000


def test_str():
    with pytest.raises(TypeError):
        square("cat")


if __name__ == "__main__":
    main()
