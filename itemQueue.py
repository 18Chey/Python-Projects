class itemQueue:
    def __init__(self):
        self.theItems = [None, None, None, None, None, None, None, None, None, None]
        self.head = 0
        self.tail = 0
        self.numItems = 0

    def enqueue(self, item):
        if self.numItems == 10:
            print("Error. Queue full!")
            return False
        else:
            self.theItems[self.tail] = item
            self.numItems += 1
            for i in range(10):
                if self.theItems[i] == None:
                    self.tail = i
                    break
            return True


class Item:
    def __init__(self, name: str, cost: float, arrival: str, transferred: bool):
        self.name = name
        self.cost = cost
        self.arrival = arrival
        self.transferred = transferred


myItems = itemQueue()


def insertItems(queue: itemQueue):
    name = input("Item name ")
    cost = input("Item cost ")
    arrival = input("Date of arrival")
    transferred = input("Transferred?: ")

    new_item = Item(name, cost, arrival, transferred)
    while queue.enqueue(new_item):
        name = input("Item name ")
        cost = input("Item cost ")
        arrival = input("Date of arrival")
        transferred = input("Transferred?: ")
        new_item = Item(name, cost, arrival, transferred)


insertItems(myItems)

print(myItems.theItems)
