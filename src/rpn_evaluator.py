from src.operators import Operators
from src.exceptions import EvaluationError, DivisionByZeroError, InvalidOperandTypeError


class RPNEvaluator:
    """
    Класс для вычисления выражений в обратной польской нотации (RPN).
    Реализует стандартный стековый алгоритм для вычисления RPN.
    """
    
    def __init__(self):
        self.operators = Operators()
        self.supported_operators = self.operators.get_operators()

    def check_parentheses(self, tokens):
        """
        Проверяет корректность скобок в выражении.

        Args:
            tokens (list): Список токенов (числа, операторы и скобки).

        Returns:
            bool: True, если скобки сбалансированы, False в противном случае.

        Raises:
            EvaluationError: При несбалансированных скобках.
        """

        stack = []

        for token in tokens:
            if token == '(':
                stack.append(token)
            elif token == ')':
                if not stack:
                    raise EvaluationError('Непарная закрывающая скобка')
                stack.pop()
        if stack:
            raise EvaluationError('Непарная открывающая скобка')

    def evaluate(self, tokens):
        """
        Вычисляет выражение в обратной польской нотации (RPN).
        
        Args:
            tokens (list): Список токенов (числа и операторы).
            
        Returns:
            float или int: Результат вычисления выражения.
            
        Raises:
            EvaluationError: При ошибке вычисления выражения.
            DivisionByZeroError: При попытке деления на ноль.
            InvalidOperandTypeError: При неподходящем типе операндов.
        """

        # Проверяем правильность скобок
        self.check_parentheses(tokens)

        stack = []

        for token in tokens:
            # Если токен - число, то добавляем в стек
            if isinstance(token, (int, float)):
                stack.append(token)
            # Если токен - оператор, применяем его
            elif token in self.supported_operators:
                # Получаем информацию об операторе
                operator_info = self.operators.get_operator_info(token)

                # Проверка на достаточность операндов
                if len(stack) < operator_info['arity']:
                    raise EvaluationError('Недостаточно операндов для оператора')

                # Извлекаем операнды из стека, применяем оператор
                try:
                    if operator_info['arity'] == 1:
                        # Унарный оператор
                        a = stack.pop()
                        result = operator_info['func'](a)
                    else:
                        # Бинарный оператор
                        b = stack.pop()
                        a = stack.pop()
                        result = operator_info['func'](a, b)
                    
                    stack.append(result)
                except DivisionByZeroError:
                    raise
                except InvalidOperandTypeError:
                    raise
                except Exception as e:
                    raise EvaluationError(f'Ошибка при выполнении оператора "{token}": {e}')
            # Игнорируем скобки
            elif token in '()':
                continue
            else:
                raise EvaluationError(f'Неизвестный оператор: {token}')

        # Финальная проверка, что остался 1 элемент в стеке
        if len(stack) != 1:
            raise EvaluationError(f'Некорректное выражение: в стеке осталось {len(stack)} элементов вместо 1')

        return stack[0]



