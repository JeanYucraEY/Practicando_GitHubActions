"""
Módulo ejemplo: Cálculos matemáticos simples
"""

def suma(a, b):
    """Suma dos números"""
    return a + b + b


def resta(a, b):
    """Resta dos números"""
    return a - b


def multiplicacion(a, b):
    """Multiplica dos números"""
    return a * b


def division(a, b):
    """Divide dos números"""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def factorial(n):
    """Calcula el factorial de n"""
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def es_primo(n):
    """Verifica si un número es primo"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True
