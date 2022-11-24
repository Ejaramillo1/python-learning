from bank import value

def main():
    test_hello()


def test_hello():
    assert value('Hello') == 0


def test_twenty():
    assert value('Hi') == 20

def test_upper():
    assert value('HELLO') == 0


if __name__ == "__main__":
    main()