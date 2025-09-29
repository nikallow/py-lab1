class CalculatorError(Exception):
    """Базовое исключение для всех ошибок калькулятора."""
    pass

class ParserError(CalculatorError):
    """Ошибка при разборе выражения на токены."""
    pass

class EvaluationError(CalculatorError):
    """Ошибка при вычислении выражения."""
    pass

class DivisionByZeroError(EvaluationError):
    """Ошибка деления на ноль."""
    pass

class InvalidOperandTypeError(EvaluationError):
    """Ошибка неверного типа операнда."""
    pass