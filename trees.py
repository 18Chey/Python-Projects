class Tree:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, data: int):
        self.left = Tree(data)

    def add_right(self, data: int):
        self.right = Tree(data)


def traverse(tree) -> None:
    """Prints in-order traversal of tree"""
    if tree:
        traverse(tree.left)
        print(tree.data, end=" ")
        traverse(tree.right)


def insert(tree, data: int) -> Tree:
    """Returns new version of tree with node inserted. If node data is equal to parent data, will be inserted on the left."""
    if tree == None:
        return Tree(data)
    elif data > tree.data:
        tree.right = insert(tree.right, data)
        return tree
    elif data <= tree.data:
        tree.left = insert(tree.left, data)
        return tree


def search(tree, data) -> list[int | bool]:
    """Returns path through tree and whether or not the item was found."""
    if tree == None:
        return [False]
    elif tree.data == data:
        return [True]
    elif tree.data < data:
        return [1] + search(tree.right, data)
    elif tree.data > data:
        return [0] + search(tree.left, data)


def main() -> None:
    mytree = None

    while True:
        mytree = insert(mytree, int(input("Data: ")))
        traverse(mytree)
        print(search(mytree, int(input("\nSearch"))))


if __name__ == "__main__":
    main()
