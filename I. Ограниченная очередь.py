class MyQueueSized:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def push(self, x):
        if len(self.queue) >= self.max_size:
            print("error")
        else:
            self.queue.append(x)

    def pop(self):
        if len(self.queue) == 0:
            print("None")
        else:
            print(self.queue.pop(0))

    def peek(self):
        if len(self.queue) == 0:
            print("None")
        else:
            print(self.queue[0])

    def size(self):
        print(len(self.queue))


num_commands = int(input())
max_size = int(input())

queue = MyQueueSized(max_size)

for _ in range(num_commands):
    command = input().split()

    if command[0] == "push":
        queue.push(int(command[1]))
    elif command[0] == "pop":
        queue.pop()
    elif command[0] == "peek":
        queue.peek()
    elif command[0] == "size":
        queue.size()
