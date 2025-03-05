import pytest
from src.factorial import factorial

# Se elimina este test porque la función ya está definida
# def test_factorial_1_falla():
#     with pytest.raises(NameError):
#         factorial(1)

def test_factorial_1_pasa():
    assert factorial(1) == 1

def test_tipo_falla():
    with pytest.raises(TypeError):  
        factorial("texto")

def test_tipo_pasa():
    assert factorial(2) == 2

def test_negativo_falla():
    with pytest.raises(ValueError): 
        factorial(-5)

def test_negativo_pasa():
    with pytest.raises(ValueError):
        factorial(-5)

def test_positivo_pasa():
    assert factorial(5) == 120
