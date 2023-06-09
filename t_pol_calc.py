class InputError(Exception):
    pass


def validate_expression(expression):
    values_expression = expression.split()
    if len(values_expression) <= 3 and values_expression[2] not in (
        '+',
        '-',
        '*',
        '/',
    ):
        raise InputError(
            "Ошибка! Некорректные входные данные. "
            "Введите минимум 2 числа и знак операции.\n"
        )
    if len(values_expression) % 2 == 0:
        raise InputError(
            "Ошибка! Некорректные входные данные. "
            "Неправильное количество цифр и знаков операций.\n"
        )

    for operation in values_expression:
        if operation not in ('+', '-', '*', '/'):
            try:
                operand = int(operation)
                if abs(operand) > 10000:
                    raise InputError(
                        "Числа во входных данные должны быть по модулю "
                        "не превосходящими 10000.\n"
                    )
            except ValueError:
                raise InputError("Ошибка! Вы ввели не число.\n")
    return expression


def calculator(expression):
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

    return stack[0]


if __name__ == "__main__":
    expression = input()
    try:
        result = calculator(validate_expression(expression))
        print(result)
    except InputError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
