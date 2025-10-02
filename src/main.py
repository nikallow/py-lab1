from src.calculator import Calculator
from src.exceptions import CalculatorError
from src.constants import HELP_TEXT


def main():
    """
    Основная функция программы. Запрашивает у пользователя ввод в обратной польской
    нотации и вычисляет результат.
    """
    calculator = Calculator()

    print(HELP_TEXT)

    while True:
        try:
            user_input = input("\nВведите выражение: ")

            if user_input.lower() == 'q':
                print("Выход из программы")
                break

            # Вычисление выражения
            result = calculator.evaluate(user_input)

            # Форматирование вывода результата
            if isinstance(result, int) or result.is_integer():
                # Если результат целочисленный, выводим без десятичной части
                print(f"Результат: {int(result)}")
            else:
                print(f"Результат: {result}")

        except CalculatorError as e:
            print(f"Ошибка: {str(e)}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {str(e)}")


if __name__ == "__main__":
    main()
