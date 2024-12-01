class Tree:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, data: int):
        self.left = Tree(data)

    def add_right(self, data: int):
        self.right = Tree(data)


def print_tree(tree: Tree | None, prefix="Root: ", level=0) -> None:
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
    """Returns in order traversal of tree"""
    result = []
    if tree:
        result.extend(traverse(tree.left))
        result.append(tree.data)
        result.extend(traverse(tree.right))
    return result


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


def binary_search_list(data: list[int]) -> list[int]:
    """Orders data list in optimal insert order for BST"""
    data.sort()
    length = len(data)

    # Base cases
    if length == 0:
        return []
    elif length == 1:
        return [data[0]]

    mid = length // 2
    result = []

    result.append(data[mid])
    result.extend(binary_search_list(data[:mid]))
    result.extend(binary_search_list(data[mid + 1 :]))

    return result


def create_tree(data: list[int]) -> Tree:
    """Returns balanced BST using values in data"""
    tree = None
    for value in binary_search_list(data):
        tree = insert(tree, value)
    return tree


def balanced_insert(tree: Tree, data: int) -> Tree:
    """Returns balanced BST with new node inserted"""
    tree_data = traverse(tree)
    tree_data.append(data)
    return create_tree(binary_search_list(tree_data))


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
    tree = None
    while True:
        tree = balanced_insert(tree, int(input("Input: ")))

        print_tree(tree)
        print(traverse(tree))


if __name__ == "__main__":
    main()
