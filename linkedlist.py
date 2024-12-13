class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse(linked_list: LinkedList):
    result = []
    while linked_list:
        result.append(linked_list.data)
        linked_list = linked_list.next
    print(result)


def insert_at_beginning(linked_list: LinkedList, data: int):
    new = LinkedList(data)
    new.next = linked_list
    return new


def delete_from_beginning(linked_list: LinkedList):
    return linked_list.next


def insert_at_end(linked_list: LinkedList, data: int):
    head = linked_list
    while linked_list.next:
        linked_list = linked_list.next
    linked_list.next = LinkedList(data)
    return head


def insert_at_position(linked_list: LinkedList, data: int, position: int):
    head = linked_list
    if position == 0:
        return insert_at_beginning(linked_list, data)
    for i in range(position - 1):
        linked_list = linked_list.next
    new = LinkedList(data)
    new.next = linked_list.next
    linked_list.next = new
    return head


def main():
    mylist = LinkedList(0)
    for i in range(1, 10):
        mylist = insert_at_beginning(mylist, i)
    traverse(mylist)
    mylist = delete_from_beginning(mylist)
    traverse(mylist)


if __name__ == "__main__":
    main()
