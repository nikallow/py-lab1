import pytest
from src.calculator import Calculator
from src.exceptions import CalculatorError


class TestCalculator:
    def setup_method(self):
        self.calculator = Calculator()

    def test_simple_expressions(self):
        """Тестирование простых выражений"""
        # Сложение
        assert self.calculator.evaluate('3 4 +') == 7

        # Вычитание
        assert self.calculator.evaluate('7 3 -') == 4

        # Умножение
        assert self.calculator.evaluate('3 4 *') == 12

        # Деление
        assert self.calculator.evaluate('10 2 /') == 5.0

        # Целочисленное деление
        assert self.calculator.evaluate('10 3 //') == 3

        # Остаток от деления
        assert self.calculator.evaluate('10 3 %') == 1

        # Возведение в степень
        assert self.calculator.evaluate('2 3 ^') == 8

    def test_complex_expressions(self):
        """Тестирование сложных выражений"""
        # (3 + 4) * 2 в RPN: 3 4 + 2 *
        assert self.calculator.evaluate('3 4 + 2 *') == 14

        # RPN: 3 4 + 2 * (со скобками)
        assert self.calculator.evaluate('( 3 4 + ) 2 *') == 14

        # 3 + 4 * 2 в RPN: 3 4 2 * +
        assert self.calculator.evaluate('3 4 2 * +') == 11

        # (3 + 4 * 2) / 2 в RPN: 3 4 2 * + 2 /
        assert self.calculator.evaluate('3 4 2 * + 2 /') == 5.5

    def test_unary_operators(self):
        """Тестирование унарных операторов"""
        # Унарный минус
        assert self.calculator.evaluate('5 ~') == -5

        # Унарный плюс
        assert self.calculator.evaluate('5 @') == 5

        # -3 + 4
        assert self.calculator.evaluate('3 ~ 4 +') == 1

    def test_errors(self):
        """Тестирование обработки ошибок"""
        # Пустое выражение
        with pytest.raises(CalculatorError):
            self.calculator.evaluate('')

        # Неизвестный токен
        with pytest.raises(CalculatorError):
            self.calculator.evaluate('3 4 $')

        # Недостаточно операндов
        with pytest.raises(CalculatorError):
            self.calculator.evaluate('3 +')

        # Слишком много операндов
        with pytest.raises(CalculatorError):
            self.calculator.evaluate('3 4 5')

        # Деление на ноль
        with pytest.raises(CalculatorError):
            self.calculator.evaluate('3 0 /')

        # Целочисленное деление на ноль
        with pytest.raises(CalculatorError):
            self.calculator.evaluate('3 0 //')

        # Неверный тип операндов
        with pytest.raises(CalculatorError):
            self.calculator.evaluate('3.5 2 //')

    def test_floating_point_results(self):
        """Тестирование результатов с плавающей точкой"""
        # Проверка деления с плавающей точкой
        assert self.calculator.evaluate('7 2 /') == 3.5

        # Проверка сложных выражений с плавающей точкой
        assert self.calculator.evaluate('3.5 2.5 + 2 *') == 12.0

    def test_integer_results(self):
        """Тестирование целочисленных результатов"""
        # Проверка, что целые числа остаются целыми
        result = self.calculator.evaluate('3 4 +')
        assert isinstance(result, int) or result.is_integer()

        # Проверка, что дробные числа не преобразуются в целые
        result = self.calculator.evaluate('7 2 /')
        assert not result.is_integer()
