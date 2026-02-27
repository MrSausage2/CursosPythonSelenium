import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_assertTest(self):
        msg = "Hola mundo"
        assert msg == "Que onda", "Test failed because strings do not match"

    @pytest.mark.smoke
    def test_SecondProgram(self):
        a = 4
        b = 6
        assert a + 2 == b, "Addition do not match"

    def test_fixture_Demo(self):
        print("I will execute steps in fixtureDemo method")