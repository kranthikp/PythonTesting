# any pytest file should start with test_FILENAME
# pytest method names should start with test
# any code should be wrapped inside method only
# method name should have sense
# -k stands for method spec pattern execution, -s logs in output -v more info metadata
# can run specific file using py.test <filename>
# skip test @pytest.mark.skip added as marker to test_method
# skip in report but execute in run @pytest.mark.xfail
# fixture are used as setup and tear down methods for test cases
# conf_test file - to generalize applying  DRY principle
# fixture is available to all the test cases
# data driven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class, it will run once before class is init and after all class methods

# example1: py.test test_demo2.py -s -v
# example2: py.test -k second -s -v
# example3: py.test
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram(setup):
    msg = "Hello"
    assert msg == "Hi", "Test Failed, because  strings do not match"


def test_secondProgram():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"


def test_thirdProgram():
    a = 4
    b = 6
    assert a + 2 != 6, "Addition Matches"
