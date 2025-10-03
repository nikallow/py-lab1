from src.exceptions import ParserError
from src.operators import Operators


class TokenParser:
    """
    Класс для токенизации строки выражения в RPN на токены.
    """

    def __init__(self):
        operators = Operators()
        self.supported_operators = operators.get_operators()

    def parse(self, expr):
        """
        Токенизирует строку с выражением в RPN на токены.

        Args:
            expr (str): Строка с выражением в RPN.

        Returns:
            list: Список токенов (числа и операторы).

        Raises:
            ParserError: При ошибке в разборе токенов.
        """
        if not expr or not (processed_expr := expr.strip()):
            raise ParserError('Пустое выражение')

        tokens = []

        for part in processed_expr.split():
            # Проверка на оператор
            if part in self.supported_operators:
                tokens.append(part)
                continue

            # Проверка на скобки
            if part in '()':
                tokens.append(part)
                continue

            # Проверка на число
            try:
                num = float(part) if '.' in part else int(part)
                if isinstance(num, float) and num.is_integer():
                    num = int(num)
                tokens.append(num)
            except ValueError:
                raise ParserError(f'Неизвестный токен: {part}') from None

        if not tokens:
            raise ParserError('Выражение не содержит токенов')

        return tokens
