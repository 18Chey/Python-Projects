class Node:
    def __init__(self, data: int, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head: Node):
        self.head = head

    def traverse(self):
        current_node = self.head
        while current_node.next != None:
            print(current_node.data)
            current_node = current_node.next

    def insert(self, value: int, position: int):
        # Create a new node
        new_node = Node(value)

        # If inserting at the start
        if position == 0:
            new_node.next = self.head
            self.head = new_node

        # If inserting at the end
        elif position == -1:
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

        # Traverse until position reached
        else:
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next

            new_node.next = current_node.next
            current_node.next = new_node

    def delete(self, target: int):
        current_node = self.head

        while current_node.next.data != target:
            current_node = current_node.next

        current_node.next = current_node.next.next


head_node = Node(0, None)
mylist = LinkedList(head_node)
