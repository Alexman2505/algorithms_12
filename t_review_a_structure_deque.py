# 88182880
from typing import Tuple


class InputError(Exception):
    pass


class Deque:
    def __init__(self, size: int):
        self.size = size
        self._buffer = [None] * size
        self._head = 0  # указатель начала дека
        self._tail = 0  # указатель конца дека
        self._count = 0  # текущее количество элементов в деке

    def is_empty(self) -> None:
        if self._count == 0:
            raise IndexError("error")

    def _calculate_index(self, index: int, offset: int) -> int:
        return (index + offset) % self.size

    def is_full(self) -> None:
        if self._count == self.size:
            raise IndexError("error")

    def push_front(self, value: int) -> None:
        self.is_full()
        self._head = self._calculate_index(self._head, -1)
        self._buffer[self._head] = value
        self._count += 1

    def push_back(self, value: int) -> None:
        self.is_full()
        self._buffer[self._tail] = value
        self._tail = self._calculate_index(self._tail, 1)
        self._count += 1

    def pop_front(self) -> None:
        self.is_empty()
        value = self._buffer[self._head]
        self._head = self._calculate_index(self._head, 1)
        self._count -= 1
        print(value)

    def pop_back(self) -> None:
        self.is_empty()
        self._tail = self._calculate_index(self._tail, -1)
        value = self._buffer[self._tail]
        self._count -= 1
        print(value)


def read_input() -> Tuple[int, int]:
    try:
        n = int(input())
    except ValueError:
        raise InputError(
            'Ошибка! Было введено не число. Введите число в диапазоне от 1 до 100000\n'
        )
    if not 1 <= n <= 100000:
        raise InputError(
            'Ошибка! Число должно быть в диапазоне от 1 до 100000\n'
        )
    try:
        m = int(input())
    except ValueError:
        raise InputError(
            'Ошибка! Было введено не число. Введите число в диапазоне от 1 до 50000\n'
        )
    if not 1 <= m <= 50000:
        raise InputError(
            'Ошибка! Число должно быть в диапазоне от 1 до 50000\n'
        )
    return n, m


def read_commands(n: int, m: int) -> None:
    deque = Deque(m)

    for _ in range(n):
        command, *args = input().split()
        try:
            getattr(deque, command)(*map(int, args))
        except AttributeError:
            print("Ошибка! Вы ввели недопустимый метод")
        except IndexError:
            print("error")


if __name__ == "__main__":
    try:
        n, m = read_input()
        read_commands(n, m)
    except InputError as e:
        print(e)
