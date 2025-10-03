from src.calculator import Calculator
from src.constants import HELP_TEXT
from src.exceptions import CalculatorError


def main():
    """
    Основная функция программы. Запрашивает у пользователя ввод в обратной польской
    нотации и вычисляет результат.
    """
    calculator = Calculator()

    print(HELP_TEXT)

    while True:
        try:
            user_input = input('\nВведите выражение: ')

            if user_input.lower() == 'q':
                print('Выход из калькулятора')
                break

            # Вычисление выражения и вывод в консоль
            result = calculator.evaluate(user_input)
            print(f'Результат: {result}')

        except CalculatorError as e:
            print(f'Ошибка: {str(e)}')
        except Exception as e:
            print(f'Непредвиденная ошибка: {str(e)}')


if __name__ == '__main__':
    main()
