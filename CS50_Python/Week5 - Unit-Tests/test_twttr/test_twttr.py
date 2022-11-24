from twttr import shorten

def main():
    test_shorten()
    test_no_replacement()


# Test letters upper and lower cases

def test_shorten():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWTTER')  == 'TWTTR' 
    assert shorten('tWiTTeR') == 'tWTTR' 


def test_numb():
    assert shorten('5678') == '5678'


# Test punctuation

def test_punct():
    assert shorten('!?.,') == '!?.,'

if __name__ == "__main__":
    main()