#es un standard tener una file llamada "conftest"
#para tener la fixture disponible en todas las demás files

import pytest

#@pytest.fixture(scope="class") esto sirve para ejecutar el codigo antes del yield una sola vez
@pytest.fixture()
def setup():
    print("Method that executes first")
    yield
    print("Method that executes last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return["Pablo", "Sanchez", "chivas te amo"]

@pytest.fixture(params=["chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param
