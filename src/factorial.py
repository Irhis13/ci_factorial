def factorial(n):
    # Validar si el numero es entero
    if not isinstance(n, int):
        raise TypeError("El número debe ser un entero")

    # Validar si el numero es negativo
    if n < 0:
        raise ValueError("El número no puede ser negativo")

    # Caso base
    if n == 0 or n == 1:
        return 1

    # Calcular factorial iterativamente
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
