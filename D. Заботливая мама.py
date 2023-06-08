# make
# def solution(node, elem):
#     count = 0
#     while elem != count:
#         if node == None:
#             return -1
#         if elem == node.value:
#             return count
#         else:
#             node = node.next_item
#             count += 1


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(value, linked_list):
    node = linked_list
    count = 0
    while node is not None:
        if value == node.value:
            return count
        node = node.next_item
        count += 1
    return -1


if __name__ == "__main__":
    n = int(input())  # Читаем количество элементов в списке
    linked_list = None
    for _ in range(n):
        item = input()  # Читаем каждый элемент списка
        node = Node(item, linked_list)
        linked_list = node

    value = input()  # Читаем значение, которое нужно найти

    index = solution(value, linked_list)
    print(index)
