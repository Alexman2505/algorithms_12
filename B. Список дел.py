# make
# def solution(node):
#     while node:
#         print(node.value)
#         node = node.next_item


def print_todo_list():
    def solution(node):
        values = []
        while node is not None:
            values.append(node)
            node = node["next_item"]
        for value in reversed(values):
            print(value["value"])

    n = int(input())
    head = None
    prev_node = None
    for _ in range(n):
        value = input()
        node = {"value": value, "next_item": None}
        if prev_node is not None:
            prev_node["next_item"] = node
        if head is None:
            head = node
        prev_node = node
    solution(head)


if __name__ == '__main__':
    print_todo_list()
