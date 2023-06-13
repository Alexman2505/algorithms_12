# 88187285

import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class InputError(Exception):
    pass


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item: int) -> None:
        self._stack.append(item)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Стек пуст.")
        return self._stack.pop()

    def is_empty(self) -> bool:
        return len(self._stack) == 0

    def top(self) -> int:
        if self.is_empty():
            raise IndexError("Стек пуст.")
        return self._stack[-1]


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
    stack = Stack()

    for operation in expression.split():
        if operation not in ('+', '-', '*', '/'):
            stack.push(operation)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            op_func = OPERATIONS.get(operation)
            if op_func is None:
                raise InputError("Ошибка! Неподдерживаемая операция.\n")
            result = op_func(a, b)
            stack.push(result)

    print(stack.top())


if __name__ == "__main__":
    try:
        expression = input()
        calculator(validate_expression(expression))
    except (InputError, ZeroDivisionError, IndexError) as e:
        print(e)
