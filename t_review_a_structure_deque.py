# 88088491
from typing import Tuple


class InputError(Exception):
    pass


class Deque:
    def __init__(self, size: int):
        self.size = size
        self.buffer = [None] * size
        self.head = 0  # указатель начала дека
        self.tail = 0  # указатель конца дека
        self.count = 0  # текущее количество элементов в деке

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.size

    def push_front(self, value: int) -> None:
        if self.is_full():
            print("error")
        else:
            self.head = (self.head - 1) % self.size
            self.buffer[self.head] = value
            self.count += 1

    def push_back(self, value: int) -> None:
        if self.is_full():
            print("error")
        else:
            self.buffer[self.tail] = value
            self.tail = (self.tail + 1) % self.size
            self.count += 1

    def pop_front(self) -> None:
        if self.is_empty():
            print("error")
        else:
            value = self.buffer[self.head]
            self.buffer[self.head] = None
            self.head = (self.head + 1) % self.size
            self.count -= 1
            print(value)

    def pop_back(self) -> None:
        if self.is_empty():
            print("error")
        else:
            self.tail = (self.tail - 1) % self.size
            value = self.buffer[self.tail]
            self.buffer[self.tail] = None
            self.count -= 1
            print(value)


def read_input() -> Tuple[int, int]:
    try:
        n = int(input())
    except ValueError:
        raise InputError(
            'Ошибка! Было введено не число. '
            'Введите число в диапазоне от 1 до 100000\n'
        )
    if not 1 <= n <= 100000:
        raise InputError(
            'Ошибка! Число должно быть в диапазоне от 1 до 100000\n'
        )
    try:
        m = int(input())
    except ValueError:
        raise InputError(
            'Ошибка! Было введено не число. '
            'Введите число в диапазоне от 1 до 50000\n'
        )
    if not 1 <= m <= 50000:
        raise InputError(
            'Ошибка! Число должно быть в диапазоне от 1 до 50000\n'
        )
    return n, m


def read_commands(n: int, m: int) -> None:
    deque = Deque(m)

    for _ in range(n):
        command = input().split()
        if len(command) == 1 and (
            command[0] == "push_front" or command[0] == "push_back"
        ):
            raise InputError(
                'Ошибка! Команды "push_front" и "push_back"'
                ' должны содержать числа\n'
            )
        elif command[0] == "push_front":
            deque.push_front(int(command[1]))
        elif command[0] == "push_back":
            deque.push_back(int(command[1]))
        elif command[0] == "pop_front":
            deque.pop_front()
        elif command[0] == "pop_back":
            deque.pop_back()
        else:
            raise InputError("Ошибка! Вы ввели недопустимый метод\n")


if __name__ == "__main__":
    try:
        n, m = read_input()
        read_commands(n, m)
    except InputError as e:
        print(e)
