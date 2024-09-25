from .hello import hello


def main():
    test_argument()
    test_default()


def test_argument():
    assert hello("John") == "hello, John"


def test_default():
    assert hello() == "hello, world"


if __name__ == "__main__":
    main()
