import pytest
from src.exceptions import DivisionByZeroError, EvaluationError, InvalidOperandTypeError
from src.rpn_evaluator import RPNEvaluator


class TestRPNEvaluator:
    def setup_method(self):
        self.evaluator = RPNEvaluator()

    def test_simple_expressions(self):
        """Тестирование простых выражений"""
        # Сложение
        assert self.evaluator.evaluate([3, 4, '+']) == 7

        # Вычитание
        assert self.evaluator.evaluate([7, 3, '-']) == 4

        # Умножение
        assert self.evaluator.evaluate([3, 4, '*']) == 12

        # Деление
        assert self.evaluator.evaluate([10, 2, '/']) == 5.0

        # Целочисленное деление
        assert self.evaluator.evaluate([10, 3, '//']) == 3

        # Остаток от деления
        assert self.evaluator.evaluate([10, 3, '%']) == 1

        # Возведение в степень
        assert self.evaluator.evaluate([2, 3, '^']) == 8

    def test_complex_expressions(self):
        """Тестирование сложных выражений"""
        # (3 + 4) * 2
        assert self.evaluator.evaluate([3, 4, '+', 2, '*']) == 14

        # 3 + 4 * 2
        assert self.evaluator.evaluate([3, 4, 2, '*', '+']) == 11

        # (3 + 4 * 2) / 2
        assert self.evaluator.evaluate([3, 4, 2, '*', '+', 2, '/']) == 5.5

        # Выражение с унарным оператором
        assert self.evaluator.evaluate([3, '~', 4, '+']) == 1  # -3 + 4 = 1

        # Комбинированное выражение с разными операторами
        assert (
            self.evaluator.evaluate([3, 4, '+', 2, '*', 6, '/', 1, '+'])
            == 3.3333333333333335
        )

        # Выражение с целочисленным делением после обычного
        assert self.evaluator.evaluate([4.5, 1.5, '/', 3, '//'])

    def test_unary_operators(self):
        """Тестирование унарных операторов"""
        # Унарный минус
        assert self.evaluator.evaluate([5, '~']) == -5

        # Унарный плюс
        assert self.evaluator.evaluate([5, '@']) == 5

        # Комбинация унарных операторов
        assert self.evaluator.evaluate([5, '~', '~']) == 5  # -(-5) = 5

    def test_parentheses(self):
        """Тестирование выражений со скобками"""
        # (3 + 4)
        assert self.evaluator.evaluate(['(', 3, 4, '+', ')']) == 7

        # 3 * (4 + 2)
        tokens = [3, '*', '(', 4, 2, '+', ')']
        with pytest.raises(EvaluationError):
            # В RPN не должно быть инфиксной записи
            self.evaluator.evaluate(tokens)

    def test_errors(self):
        """Тестирование обработки ошибок"""
        # Недостаточно операндов
        with pytest.raises(EvaluationError):
            self.evaluator.evaluate([3, '+'])

        # Слишком много операндов
        with pytest.raises(EvaluationError):
            self.evaluator.evaluate([3, 4, 5])

        # Деление на ноль
        with pytest.raises(DivisionByZeroError):
            self.evaluator.evaluate([3, 0, '/'])

        # Целочисленное деление на ноль
        with pytest.raises(DivisionByZeroError):
            self.evaluator.evaluate([3, 0, '//'])

        # Неверный тип операндов
        with pytest.raises(InvalidOperandTypeError):
            self.evaluator.evaluate([3.5, 2, '//'])
