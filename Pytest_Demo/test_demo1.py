#All pytest files should start with "test_" or end with "_test"
#pytest method names should start with "test_"
#All the code must be wrapped in method only
#El path del Module de python NO tiene que tener espacios
#cd + el path en la consola para ejecutar los comandos py.test
#py.test -k "keyword"" -v -s despues de la k se pone el grupo o keyword de test cases deseados
#py.test -m "mark" pones una tag al metodo con un nombre y solamente corre los metodos con esa marca
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    print("Hola mundo")

def test_secondProgram():
    print("Arriba las chivas")
