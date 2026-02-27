import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def editProfile(self, dataLoad): #preguntarle a deepseek sobre esto
        print(dataLoad)