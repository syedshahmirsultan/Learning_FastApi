
def add_Numbers(a:int,b:int)-> int:
    return a + b

# 'test' prefix must be in the function name of the testing function
def test_func():
    assert add_Numbers(3,5) == 8


def subtract_Two_Numbers(a:int,b:int)-> int:
    return a - b


def test_func1():
    assert subtract_Two_Numbers(5,3) == 2