import pytest
from src.exceptions import ParserError
from src.token_parser import TokenParser


class TestTokenParser:
    def setup_method(self):
        self.parser = TokenParser()

    def test_empty_expression(self):
        """Тестирование пустого выражения"""
        with pytest.raises(ParserError) as excinfo:
            self.parser.parse('')
        assert 'Пустое выражение' in str(excinfo.value)

        with pytest.raises(ParserError) as excinfo:
            self.parser.parse('     ')
        assert 'Пустое выражение' in str(excinfo.value)

    def test_invalid_token(self):
        """Тестирование неизвестных токенов"""
        with pytest.raises(ParserError) as excinfo:
            self.parser.parse('3 4 & +')
        assert 'Неизвестный токен' in str(excinfo.value)

    def test_valid_tokens(self):
        """Тестирование корректной работы токенизатора без скобок"""
        # Тест с числами и основными операторами
        tokens = self.parser.parse('3 4 +')
        assert tokens == [3, 4, '+']

        # Тест со всеми операторами
        tokens = self.parser.parse('3 4 + 5 - 6 * 7 / 8 // 9 % 2 ^ ~ @')
        assert tokens == (
            [3, 4, '+', 5, '-', 6, '*', 7, '/', 8, '//', 9, '%', 2, '^', '~', '@']
        )

        # Тест с десятичными числами
        tokens = self.parser.parse('3.5 4.2 +')
        assert tokens == [3.5, 4.2, '+']

        # Тест с отрицательными числами
        tokens = self.parser.parse('-3 -4 +')
        assert tokens == [-3, -4, '+']

    def test_parse_with_parentheses(self):
        """Тестирование токенизации правильных скобок"""
        tokens = self.parser.parse('( 3 4 + )')
        assert tokens == ['(', 3, 4, '+', ')']

        tokens = self.parser.parse('3 ( 4 5 + ) *')
        assert tokens == [3, '(', 4, 5, '+', ')', '*']

    def test_invalid_rpn_inside_parentheses(self):
        """Проверка некорректного RPN внутри скобок"""
        with pytest.raises(ParserError) as excinfo:
            self.parser.parse('( 3 5 ) +')
        assert 'Некорректное выражение внутри скобок' in str(excinfo.value)

        with pytest.raises(ParserError) as excinfo:
            self.parser.parse('3 ( 4 + 5 ) *')
        assert 'Некорректное выражение внутри скобок' in str(excinfo.value)

    def test_unbalanced_parentheses(self):
        """Проверка непарных скобок"""
        with pytest.raises(ParserError) as excinfo:
            self.parser.parse('( ( 3 4 + )')
        assert 'Лишняя открывающая скобка' in str(excinfo.value)

        with pytest.raises(ParserError) as excinfo:
            self.parser.parse('3 4 + )')
        assert 'Лишняя закрывающая скобка' in str(excinfo.value)

    def test_empty_parentheses(self):
        """Проверка пустых скобок"""
        with pytest.raises(ParserError) as excinfo:
            self.parser.parse('( )')
        assert 'Некорректное выражение внутри скобок' in str(excinfo.value)
