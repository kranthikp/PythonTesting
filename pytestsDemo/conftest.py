import pytest


@pytest.fixture(scope="class")
def setup():
    print("executed first")
    yield
    print("i will be executed in last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["panda", "kranthi", "automatepanda.com"]


@pytest.fixture(params=[("chrome", "panda", "kranthi"), ("firefox", "panda"), ("Edge", "KK")])
def crossBrowser(request):
    # running tests with multiple datasets
    return request.param
