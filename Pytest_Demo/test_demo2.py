import pytest

def test_assertTest():
    msg="Hola mundo"
    assert msg=="Que onda", "Test failed because strings do not match"

@pytest.mark.smoke
def test_SecondProgram():
    a=4
    b=6
    assert a+2==b, "Addition do not match"

@pytest.fixture()
def setup():
    print("Method that executes first")