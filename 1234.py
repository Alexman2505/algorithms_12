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
            raise InputError("error")

    def is_full(self) -> None:
        if self._count == self.size:
            raise InputError("error")

    def push_front(self, value: int) -> None:
        self.is_full()
        self._head = (self._head - 1) % self.size
        self._buffer[self._head] = value
        self._count += 1

    def push_back(self, value: int) -> None:
        self.is_full()
        self._buffer[self._tail] = value
        self._tail = (self._tail + 1) % self.size
        self._count += 1

    def pop_front(self) -> None:
        self.is_empty()
        value = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = (self._head + 1) % self.size
        self._count -= 1
        print(value)

    def pop_back(self) -> None:
        self.is_empty()
        self._tail = (self._tail - 1) % self.size
        value = self._buffer[self._tail]
        self._buffer[self._tail] = None
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
        raise InputError('Ошибка! Число должно быть в диапазоне от 1 до 100000\n')
    try:
        m = int(input())
    except ValueError:
        raise InputError(
            'Ошибка! Было введено не число. Введите число в диапазоне от 1 до 50000\n'
        )
    if not 1 <= m <= 50000:
        raise InputError('Ошибка! Число должно быть в диапазоне от 1 до 50000\n')
    return n, m


def read_commands(n: int, m: int) -> None:
    deque = Deque(m)

    for _ in range(n):
        command = input().split()
        if len(command) == 1 and (
            command[0] == "push_front" or command[0] == "push_back"
        ):
            print('Ошибка! Команды "push_front" и "push_back" должны содержать числа')
        elif command[0] == "push_front":
            try:
                deque.push_front(int(command[1]))
            except InputError:
                print("error")
        elif command[0] == "push_back":
            try:
                deque.push_back(int(command[1]))
            except InputError:
                print("error")
        elif command[0] == "pop_front":
            try:
                deque.pop_front()
            except InputError:
                print("error")
        elif command[0] == "pop_back":
            try:
                deque.pop_back()
            except InputError:
                print("error")
        else:
            print("Ошибка! Вы ввели недопустимый метод")


if __name__ == "__main__":
    try:
        n, m = read_input()
        read_commands(n, m)
    except InputError as e:
        print(e)
