class Deque:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.front = 0  # указатель начала дека
        self.rear = 0  # указатель конца дека
        self.count = 0  # текущее количество элементов в деке

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def push_front(self, value):
        if self.is_full():
            print("error")
        else:
            self.front = (self.front - 1) % self.size
            self.buffer[self.front] = value
            self.count += 1

    def push_back(self, value):
        if self.is_full():
            print("error")
        else:
            self.buffer[self.rear] = value
            self.rear = (self.rear + 1) % self.size
            self.count += 1

    def pop_front(self):
        if self.is_empty():
            print("error")
        else:
            value = self.buffer[self.front]
            self.front = (self.front + 1) % self.size
            self.count -= 1
            print(value)

    def pop_back(self):
        if self.is_empty():
            print("error")
        else:
            self.rear = (self.rear - 1) % self.size
            value = self.buffer[self.rear]
            self.count -= 1
            print(value)


def process_commands(n, m):
    deque = Deque(m)

    for _ in range(n):
        command = input().split()
        if command[0] == "push_front":
            deque.push_front(int(command[1]))
        elif command[0] == "push_back":
            deque.push_back(int(command[1]))
        elif command[0] == "pop_front":
            deque.pop_front()
        elif command[0] == "pop_back":
            deque.pop_back()


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    process_commands(n, m)
