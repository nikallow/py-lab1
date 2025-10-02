from src.exceptions import DivisionByZeroError, InvalidOperandTypeError


class Operators:
    """
    Класс операторов с их свойствами и функциями.
    """
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
                'func': self._division,
            },
            '//': {
                'arity': 2,
                'priority': 2,
                'func': self._integer_division,
            },
            '%': {
                'arity': 2,
                'priority': 2,
                'func': self._modulo,
            },
            '^': {
                'arity': 2,
                'priority': 3,
                'right_associative': True,
                'func': lambda a, b: a ** b,
            },
            '~': {
                'arity': 1,
                'priority': 4,
                'func': lambda a: -a,
            },
            '@': {
                'arity': 1,
                'priority': 4,
                'func': lambda a: a,
            }
        }

    def _division(self, a, b):
        """
        Выполняет операцию деления с проверкой деления на ноль.

        Args:
            a: Делимое.
            b: Делитель.

        Returns:
            float: Результат деления.

        Raises:
            DivisionByZeroError: При делении на ноль.
        """
        if b == 0:
            raise DivisionByZeroError('Деление на ноль')
        return a / b

    def _integer_division(self, a, b):
        """
        Выполняет операцию целочисленного деления с проверками.

        Args:
            a: Делимое.
            b: Делитель.

        Returns:
            int: Результат целочисленного деления.

        Raises:
            DivisionByZeroError: При делении на ноль.
            InvalidOperandTypeError: Если операнды не целые числа.
        """
        if not (isinstance(a, int) and isinstance(b, int)):
            raise InvalidOperandTypeError("Операнды должны быть целыми числами для операции '//'")
        if b == 0:
            raise DivisionByZeroError('Целочисленное деление на ноль')
        return a // b

    def _modulo(self, a, b):
        """
        Выполняет операцию получения остатка от деления с проверками.

        Args:
            a: Делимое.
            b: Делитель.

        Returns:
            int: Остаток от деления.

        Raises:
            DivisionByZeroError: При делении на ноль.
            InvalidOperandTypeError: Если операнды не целые числа.
        """
        if not (isinstance(a, int) and isinstance(b, int)):
            raise InvalidOperandTypeError("Операнды должны быть целыми числами для операции '%'")
        if b == 0:
            raise DivisionByZeroError('Остаток от деления на ноль')
        return a % b

    def get_operators(self):
        """
        Возвращает список всех поддерживаемых операторов.

        Returns:
            list: Список операторов.
        """
        return list(self.operators.keys())

    def get_operator_info(self, operator):
        """
        Возвращает информацию об операторе.

        Args:
            operator (str): Оператор.

        Returns:
            dict: Информация об операторе.

        Raises:
            KeyError: Если оператор не найден.
        """
        if operator not in self.operators:
            raise KeyError(f'Неизвестный оператор: {operator}')
        return self.operators[operator]
