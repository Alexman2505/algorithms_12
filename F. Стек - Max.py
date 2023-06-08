class StackMax:
    def __init__(self):
        self.stack = []  # стек элементов
        self.max_stack = []  # стек текущих максимумов

    def push(self, x):
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if not self.stack:
            return "error"
        x = self.stack.pop()
        if x == self.max_stack[-1]:
            self.max_stack.pop()

    def get_max(self):
        if not self.max_stack:
            return "None"
        return self.max_stack[-1]


n = int(input())  # количество команд
stack = StackMax()
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        stack.push(int(command[1]))
    elif command[0] == "pop":
        result = stack.pop()
        if result == "error":
            print(result)
    elif command[0] == "get_max":
        print(stack.get_max())
