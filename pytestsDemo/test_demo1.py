# any pytest file should start with test_FILENAME
# pytest method names should start with test
# any code should be wrapped inside method only
# you can mark (tag) tests @pytest.mark.smoke and then run using -m marker_name
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("hello")


@pytest.mark.xfail
def test_secondProgram():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
    print(crossBrowser[1])
