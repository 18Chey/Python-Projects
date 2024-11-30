class Tree:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, data: int):
        self.left = Tree(data)

    def add_right(self, data: int):
        self.right = Tree(data)


def print_tree(tree, prefix="Root: ", level=0):
    """Prints the tree"""
    if tree:
        print((" " * 3) * level + prefix + str(tree.data))
        if tree.left:
            print_tree(tree.left, "L: ", level + 1)
        if tree.right:
            print_tree(tree.right, "R: ", level + 1)
    else:
        pass


def traverse(tree: Tree | None) -> None:
    """Prints in-order traversal of tree"""
    if tree:
        traverse(tree.left)
        print(tree.data, end=" ")
        traverse(tree.right)


def insert(tree: Tree | None, data: int) -> Tree:
    """Returns new version of tree with node inserted. If node data is equal to parent data, will be inserted on the left."""
    if tree == None:
        return Tree(data)
    elif data > tree.data:
        tree.right = insert(tree.right, data)
        return tree
    elif data <= tree.data:
        tree.left = insert(tree.left, data)
        return tree


def minimum(tree: Tree) -> Tree:
    """Returns minimum node of tree"""
    while tree.left:
        tree = tree.left
    return tree


def maximum(tree: Tree) -> Tree:
    """Returns maximum node of tree"""
    while tree.right:
        tree = tree.right
    return tree


def search(tree: Tree | None, data: int) -> Tree | None:
    """Returns subtree or None if not in tree."""
    if tree == None:
        return None
    elif tree.data == data:
        return tree
    elif tree.data < data:
        return search(tree.right, data)
    elif tree.data > data:
        return search(tree.left, data)


def delete(tree: Tree | None, data: int) -> Tree:
    """Returns new version of tree with node deleted"""

    # Traverse tree until target node found
    if tree == None:
        return None
    elif data < tree.data:
        tree.left = delete(tree.left, data)
    elif data > tree.data:
        tree.right = delete(tree.right, data)
    elif data == tree.data:

        # Case 3: Node has two children, node replaced with maximum node from left subtree
        if tree.left and tree.right:
            successor = maximum(tree.left)
            tree.data = successor.data
            tree.left = delete(tree.left, successor.data)

        # Case 2: Node has one child, node replaced with child
        elif tree.left:
            return tree.left
        elif tree.right:
            return tree.right

        # Case 1: Node has no children, node deleted
        else:
            return None

    return tree


def main() -> None:
    root = None
    for value in [10, 5, 15, 2, 8, 12, 20]:
        root = insert(root, value)

    print_tree(root)
    root = delete(root, 10)
    print_tree(root)


if __name__ == "__main__":
    main()
