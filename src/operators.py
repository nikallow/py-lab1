from .exceptions import DivisionByZeroError, InvalidOperandTypeError

class Operators:
    def __init__(self):
        self.operators = {
            '+': {
                'arity': 2,
                'priority': 1,
                'func': lambda a, b: a + b,
            },
            '-': {
                'arity': 2,
                'priority': 1,
                'func': lambda a, b: a - b,
            },
            '*': {
                'arity': 2,
                'priority': 2,
                'func': lambda a, b: a * b,
            },
            '/': {
                'arity': 2,
                'priority': 2,
                'func': lambda a, b: a / b,
            },
            '%': {
                'arity': 2,
                'priority': 3,
                'func': lambda a, b: a % b,
            },
            '**': {
                'arity': 2,
                'priority': 3,
                'right_associative': True,
                'func': lambda a, b: a ** b,
            },
            '~': {
                'arity': 1,
                'priority': 4,
                'func': lambda a: a,
            },
            '@': {
                'arity': 1,
                'priority': 4,
                'func': lambda a: -a,
            }
        }

    def _divizion(self, a, b):
        if b == 0:
            raise DivisionByZeroError('Деление на ноль')
        return a / b

    def _integer_division(self, a, b):
        if not(isinstance(a, int) and isinstance(b, int)):
            raise InvalidOperandTypeError("Операнды должны быть целыми числами для операции '//'")
        if b == 0:
            raise DivisionByZeroError('Целочисленное деление на ноль')

    def _modulo(self, a, b):
        if not(isinstance(a, int) and isinstance(b, int)):
            raise InvalidOperandTypeError("Операнды должны быть целыми числами для операции '%'")
        if b == 0:
            raise DivisionByZeroError('Остаток от деления на ноль')
        return a % b

    def get_operators(self):
        return list(self.operators.keys())