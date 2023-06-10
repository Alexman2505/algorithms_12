# 88087820
class InputError(Exception):
    pass


def validate_expression(expression: str) -> str:
    values_expression = expression.split()
    if len(values_expression) < 3:
        return values_expression[-1]

    for operation in values_expression:
        if operation not in ('+', '-', '*', '/'):
            try:
                operand = int(operation)
                if abs(operand) > 10000:
                    raise InputError(
                        "Ошибка! Числа во входных данных должны быть "
                        "по модулю не превосходящими 10000.\n"
                    )
            except ValueError:
                raise InputError("Ошибка! Вы ввели не число.\n")
    return expression


def calculator(expression: str) -> None:
    stack = []

    for operation in expression.split():
        if operation not in ('+', '-', '*', '/'):
            stack.append(operation)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            if operation == '+':
                stack.append(a + b)
            if operation == '-':
                stack.append(a - b)
            if operation == '*':
                stack.append(a * b)
            if operation == '/':
                if b == 0:
                    raise ZeroDivisionError("Ошибка! Деление на ноль.\n")
                stack.append(a // b)
    print(stack[-1])


if __name__ == "__main__":
    try:
        expression = input()
        calculator(validate_expression(expression))
    except InputError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
