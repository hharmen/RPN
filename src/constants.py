from typing import Callable
BINARY_OPERATIONS = ['+', '-', '*', '/', '//', '%', '**']
UNARY_OPERATIONS = ['~', '$']
ALL_OPERATIONS = BINARY_OPERATIONS + UNARY_OPERATIONS

operations: dict[str, Callable] = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '//': lambda x, y: x // y,
            '%': lambda x, y: x % y,
            '**': lambda x, y: x ** y,
            '~': lambda x: -x,
            '$': lambda x: +x
        }
