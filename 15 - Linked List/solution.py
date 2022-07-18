class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        temp = Node(data)

        if head is None:
            head = temp
            return head

        current = head

        while current.next:
            current = current.next
        current.next = temp

        return head

