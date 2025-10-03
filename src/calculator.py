from src.exceptions import CalculatorError
from src.rpn_evaluator import RPNEvaluator
from src.token_parser import TokenParser


class Calculator:
    """
    Основной класс калькулятора, обрабатывающий выражения в обратной польской записи
    """

    def __init__(self):
        self.token_parser = TokenParser()
        self.rpn_evaluator = RPNEvaluator()

    def evaluate(self, expr):
        """
        Вычисляет значение выражения в обратной польской записи.
        Args:
             expr (str): Строка с выражением в RPN.
        Returns:
            float/int: Результат вычисления выражения.
        Raises:
            CalculatorError: При наличии ошибок в выражении.
        """
        try:
            # Токенизация выражения
            tokens = self.token_parser.parse(expr)

            # Вычисление результата
            result = self.rpn_evaluator.evaluate(tokens)
            return result

        except Exception as e:
            # Преобразование всех исключений в CalculatorError
            if isinstance(e, CalculatorError):
                raise
            else:
                if isinstance(e, CalculatorError):
                    raise
                else:
                    raise CalculatorError(f'Ошибка при вычислении: {str(e)}') from e
