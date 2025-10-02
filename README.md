# Лаба по Python №1
Вариант: M3

## Структура проекта
```
.
├── README.md
├── pyproject.toml
├── uv.lock
├── src
│   ├── calculator.py
│   ├── constants.py
│   ├── exceptions.py
│   ├── main.py
│   ├── operators.py
│   ├── rpn_evaluator.py
│   └── token_parser.py
└── tests
    ├── calculator_test.py
    ├── operators_test.py
    ├── rpn_evaluator_test.py
    └── token_parser_test.py
```
Тесты используют `pytest`

## Допущения
`@` - унарный плюс  
`~` - унарный минус  
`^` - возведение в степень