def add(a, b):
    """Сложение."""
    return a + b


def subtract(a, b):
    """Вычитание."""
    return a - b


def multiply(a, b):
    """Умножение."""
    return a * b


def divide(a, b):
    """Деление с проверкой на ноль."""
    if b == 0:
        raise ValueError('Деление на ноль невозможно')
    return a / b
