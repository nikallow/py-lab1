from src.exceptions import ParserError
from src.operators import Operators


class TokenParser:
    """
    Класс для токенизации строки выражения в RPN на токены.
    """

    def __init__(self):
        self.operators = Operators()
        self.supported_operators = self.operators.get_operators()

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

        # Проверка на валидность скобок и содержимого
        self._check_parentheses_content(tokens)

        return tokens

    def _check_parentheses_content(self, tokens):
        """
        Проверяет, что каждое выражение в скобках является корректным RPN.
        Args:
            tokens (list): список токенов
        Raises:
            ParserError: если выражение в скобках некорректное
        """
        stack = []  # Стек с подвыражениями
        subexpr = []  # Токены для текущего подвыражения

        for token in tokens:
            if token == '(':
                # Кидаем в стек подвыражение и создаём новое
                stack.append(subexpr)
                subexpr = []
            elif token == ')':
                # Не нашли открывающую скобку
                if not stack:
                    raise ParserError('Лишняя закрывающая скобка')
                # Проверяем подвыражение внутри скобок на корректный RPN
                if not self._is_valid_rpn(subexpr):
                    raise ParserError('Некорректное выражение внутри скобок')
                # Сворачиваем подвыражение до одного значения: помещаем плейсхолдер
                subexpr = stack.pop()
                subexpr.append(0)  # любое значение вместо скобок (плейсхолдер)
            else:
                # Копим токены текущего подвыражения
                subexpr.append(token)

        # После всех токенов стек должен быть пустым — иначе не хватило ')'
        if stack:
            raise ParserError('Лишняя открывающая скобка')

    def _is_valid_rpn(self, tokens):
        """
        Проверяет, что список токенов представляет корректное RPN-выражение.
        Args:
            tokens (list)
        Returns:
            bool
        """
        stack_size = 0  # Моделируем размер стека вычислений без хранения значений
        for token in tokens:
            if isinstance(token, (int, float)):
                # Операнд кладёт значение на стек
                stack_size += 1
            elif token in self.supported_operators:
                # Проверяем достаточность операндов для оператора заданной arity
                arity = self.operators.get_operator_info(token)['arity']
                if stack_size < arity:
                    return False
                # Применение оператора: снимаем arity, кладём один результат
                stack_size = stack_size - arity + 1
            else:
                return False
        # Корректное RPN выражение оставляет ровно одно значение на стеке
        return stack_size == 1
