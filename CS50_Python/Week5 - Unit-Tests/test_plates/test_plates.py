from plates import is_valid

def main():
    test_letters()
    test_max_char()
    test_middle_numbers()
    test_punctuation()
    test_periods()
    test_non_zero()

def test_letters():
    assert is_valid('AA') == True
    assert is_valid('A1') == False
    assert is_valid('1A1') == False


def test_max_char():
    assert is_valid('adcetidkon') == False


def test_middle_numbers():
    assert is_valid("ab123a") == False

def test_punctuation():
    assert is_valid('ab..cd') == False

def test_periods():
    assert is_valid('ab .cd') == False

def test_non_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') ==  False


if __name__ == "__main__":
    main()