import pytest


# optimize using class if multiple methods need fixture
@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("executed steps in fixture demo method")

    def test_fixtureDemo1(self):
        print("executed steps in fixture demo method")

    def test_fixtureDemo2(self):
        print("executed steps in fixture demo method")

    def test_fixtureDemo3(self):
        print("executed steps in fixture demo method")


