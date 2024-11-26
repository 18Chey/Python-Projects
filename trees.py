class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, data):
        self.left = Tree(data)

    def add_right(self, data):
        self.right = Tree(data)

    def show_tree(self):
        left = None
        right = None
        if self.left != None:
            left = self.left.data
        if self.right != None:
            right = self.right.data

        print(f"{self.data} Left: {left} Right: {right}")
        if self.left != None:
            self.left.show_tree()
        if self.right != None:
            self.right.show_tree()


def traverse(tree):
    if tree:
        traverse(tree.left)
        print(tree.data)
        traverse(tree.right)


mytree = Tree(8)
mytree.add_left(2)
mytree.add_right(34)
mytree.left.add_left(1)
mytree.left.add_right(5)
mytree.left.left.add_left(1)
mytree.add_right(34)
mytree.right.add_left(21)
mytree.right.add_right(55)
mytree.right.left.add_left(13)
mytree.left.right.add_left(3)

traverse(mytree)
