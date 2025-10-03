# Лаба по Python №1
Вариант: M3

## Установка и запуск
```bash
uv venv

source .venv/bin/activate # Для Linux/MacOS
.venv\Scripts\activate # Для Windows

uv sync
```
```bash
uv run -m src.main # Запуск калькулятора
uv run -m pytest tests # Запуск тестов
```

## Структура проекта
```
.
├── README.md
├── pyproject.toml
├── uv.lock
├── src
│   ├── calculator.py # Класс калькулятора
│   ├── constants.py
│   ├── exceptions.py # Ошибки
│   ├── main.py
│   ├── operators.py # Операторы и их свойства
│   ├── rpn_evaluator.py # Вычисление RPN
│   └── token_parser.py # Разбивание на токены и проверка скобок
└── tests
    ├── calculator_test.py
    ├── operators_test.py
    ├── rpn_evaluator_test.py
    └── token_parser_test.py
```

## Допущения
- `@` - унарный плюс
- `~` - унарный минус
- `^` - возведение в степень
- Пользователь вводит выражение в обратной польской записи через пробелы

## Обработка ошибок
- `ParserError` – некорректные токены или пустой ввод.
- `EvaluationError` – ошибки при вычислении (например, нехватка операндов).
- `DivisionByZeroError` – деление на ноль.
- `InvalidOperandTypeError` – использование некорректных типов (// и % для вещественных чисел).
