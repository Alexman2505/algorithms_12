class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def put_x(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def get_head(self):
        if self.is_empty():
            return "error"
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return data

    def size_stek(self):
        return self.size


n = int(input())
queue = LinkedList()

for _ in range(n):
    command = input().split()

    if command[0] == "put":
        queue.put_x(int(command[1]))
    elif command[0] == "get":
        print(queue.get_head())
    elif command[0] == "size":
        print(queue.size_stek())
