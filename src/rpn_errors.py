class BracketsError(Exception):
    """Неправильная расстановка скобок"""

class DivisionByZeroError(Exception):
    """Деление на ноль"""

class StackUnderflowError(Exception):
    """Ошибка нехватки чисел для вычисления результата"""

class InputError(Exception):
    """Неправильный ввод"""
