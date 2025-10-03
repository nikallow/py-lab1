import pytest
from src.exceptions import DivisionByZeroError, InvalidOperandTypeError
from src.operators import Operators


class TestOperators:
    def setup_method(self):
        self.operators = Operators()

    def test_operators_list(self):
        """Проверка получения списка операторов"""
        ops = self.operators.get_operators()
        expected_ops = ['+', '-', '*', '/', '//', '%', '^', '~', '@']
        assert sorted(ops) == sorted(expected_ops)

    def test_get_operator_info(self):
        """Проверка получения информации об операторе"""
        # Проверка бинарного оператора
        info = self.operators.get_operator_info('+')
        assert info['arity'] == 2
        assert info['priority'] == 1
        assert callable(info['func'])

        # Проверка унарного оператора
        info = self.operators.get_operator_info('~')
        assert info['arity'] == 1
        assert info['priority'] == 4
        assert callable(info['func'])

        # Проверка несуществующего оператора
        with pytest.raises(KeyError):
            self.operators.get_operator_info('?')

    def test_binary_operators(self):
        """Тестирование бинарных операторов"""
        # Сложение
        add_func = self.operators.get_operator_info('+')['func']
        assert add_func(3, 4) == 7

        # Вычитание
        sub_func = self.operators.get_operator_info('-')['func']
        assert sub_func(7, 3) == 4

        # Умножение
        mul_func = self.operators.get_operator_info('*')['func']
        assert mul_func(3, 4) == 12

        # Деление
        div_func = self.operators.get_operator_info('/')['func']
        assert div_func(10, 2) == 5.0

        # Целочисленное деление
        idiv_func = self.operators.get_operator_info('//')['func']
        assert idiv_func(10, 3) == 3

        # Остаток от деления
        mod_func = self.operators.get_operator_info('%')['func']
        assert mod_func(10, 3) == 1

        # Возведение в степень
        pow_func = self.operators.get_operator_info('^')['func']
        assert pow_func(2, 3) == 8

    def test_unary_operators(self):
        """Тестирование унарных операторов"""
        # Унарный минус
        neg_func = self.operators.get_operator_info('~')['func']
        assert neg_func(5) == -5

        # Унарный плюс
        pos_func = self.operators.get_operator_info('@')['func']
        assert pos_func(5) == 5

    def test_division_by_zero(self):
        """Проверка деления на ноль"""
        div_func = self.operators.get_operator_info('/')['func']
        with pytest.raises(DivisionByZeroError):
            div_func(10, 0)

        idiv_func = self.operators.get_operator_info('//')['func']
        with pytest.raises(DivisionByZeroError):
            idiv_func(10, 0)

        mod_func = self.operators.get_operator_info('%')['func']
        with pytest.raises(DivisionByZeroError):
            mod_func(10, 0)

    def test_invalid_operand_type(self):
        """Проверка операций с неправильными типами операндов"""
        idiv_func = self.operators.get_operator_info('//')['func']
        with pytest.raises(InvalidOperandTypeError):
            idiv_func(10.5, 2)
        with pytest.raises(InvalidOperandTypeError):
            idiv_func(10, 2.5)

        mod_func = self.operators.get_operator_info('%')['func']
        with pytest.raises(InvalidOperandTypeError):
            mod_func(10.5, 2)
        with pytest.raises(InvalidOperandTypeError):
            mod_func(10, 2.5)
