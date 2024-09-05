from main import is_even

def test_is_even():
    """Testing even-odd function"""
    assert is_even(4) == "Even"
    assert is_even(7) == "Odd"
    print("Success")

if __name__ == "__main__":
    test_is_even()
