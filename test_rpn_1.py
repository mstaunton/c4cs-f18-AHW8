import rpn

def test_add():
    result = rpn.calculate("1 1 +")
    assert result == 2

def test_subtract():
    result = rpn.calculate("5 3 -")
    assert result == 2

def test_multiply():
    result = rpn.calculate("5 3 *")
    assert result == 15

def test_divide():
    result = rpn.calculate("6 3 /")
    assert result == 2

def test_exponent():
    result = rpn.calculate("5 2 ^")
    assert result == 25
