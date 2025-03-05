"""Módulo que contiene la función factorial"""

def factorial(n):
    """
    Calcula el factorial de un número.

    Parámetros:
    - n: Número entero positivo.

    Retorna:
    - El factorial de n.

    Lanza:
    - TypeError si n no es un entero.
    - ValueError si n es negativo.
    """
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero")
    if n < 0:
        raise ValueError("El número no puede ser negativo")
    if n in {0, 1}:  # Corrección sugerida por pylint
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
