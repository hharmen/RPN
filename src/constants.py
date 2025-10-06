from typing import Dict, Callable
BINARY_OPERATIONS = ['+', '-', '*', '/', '//', '%', '**']
UNARY_OPERATIONS = ['~', '$']
ALL_OPERATIONS = BINARY_OPERATIONS + UNARY_OPERATIONS

operations: Dict[str, Callable] = {
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
