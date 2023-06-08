# n = int(input())
# a = [input() for _ in range(n)][::-1]
# a.pop(int(input()))
# for i in a:
#     print(i)


# make
# def solution(node, idx):
#     def get_node_by_index(node, index):
#         while index:
#             node = node.next_item
#             index -= 1
#         return node

#     if idx == 0:
#         node = node.next_item
#     else:
#         previous_node = get_node_by_index(node, idx - 1)
#         next_node = get_node_by_index(node, idx + 1)
#         previous_node.next_item = next_node
#     return node


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def create_linked_list(n):
    head = None
    for _ in range(n):
        data = input()
        new_node = Node(data)
        new_node.next = head
        head = new_node
    return head


def delete_node(head, index):
    if index == 0:
        return head.next

    curr = head
    prev = None
    count = 0

    while curr and count != index:
        prev = curr
        curr = curr.next
        count += 1

    if curr:
        prev.next = curr.next

    return head


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next


if __name__ == '__main__':
    n = int(input())
    linked_list = create_linked_list(n)
    index = int(input())
    updated_list = delete_node(linked_list, index)
    print_linked_list(updated_list)
