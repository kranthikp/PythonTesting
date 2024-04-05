import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_editProfile(self, dataLoad):
        print(dataLoad)
        for index in dataLoad:
            print(index)
