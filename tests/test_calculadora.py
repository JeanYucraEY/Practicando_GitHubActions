"""
Pruebas para el módulo calculadora
"""

import pytest
from src.calculadora import suma, resta, multiplicacion, division, factorial, es_primo


class TestOperacionesBasicas:
    """Pruebas para operaciones básicas"""
    
    def test_suma(self):
        assert suma(2, 3) == 5
        assert suma(-1, 1) == 0
        assert suma(0, 0) == 0
    
    def test_resta(self):
        assert resta(5, 3) == 2
        assert resta(0, 5) == -5
        assert resta(10, 10) == 0
    
    def test_multiplicacion(self):
        assert multiplicacion(3, 4) == 12
        assert multiplicacion(-2, 3) == -6
        assert multiplicacion(0, 100) == 0
    
    def test_division(self):
        assert division(10, 2) == 5
        assert division(7, 2) == 3.5
        assert division(-10, 2) == -5
    
    def test_division_por_cero(self):
        with pytest.raises(ValueError):
            division(10, 0)


class TestFunciones:
    """Pruebas para funciones adicionales"""
    
    def test_factorial(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(10) == 3628800
    
    def test_factorial_negativo(self):
        with pytest.raises(ValueError):
            factorial(-1)
    
    def test_es_primo(self):
        assert es_primo(2) == True
        assert es_primo(3) == True
        assert es_primo(5) == True
        assert es_primo(7) == True
        assert es_primo(11) == True
    
    def test_no_es_primo(self):
        assert es_primo(1) == False
        assert es_primo(4) == False
        assert es_primo(6) == False
        assert es_primo(9) == False
        assert es_primo(10) == False
