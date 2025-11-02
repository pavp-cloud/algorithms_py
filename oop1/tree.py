class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.value}({self.left},{self.right})'


class Tree:
    def __init__(self):
        self.root = None

    def add(self, node, current):
        if current.value > node.value:
            if current.left is None:
                current.left = node
            else:
                self.add(node, current.left)
        else:
            if current.right is None:
                current.right = node
            else:
                self.add(node, current.right)

    def __add__(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            self.add(node, self.root)

    def __repr__(self):
        return repr(self.root)


def main():
    NodeA = Node(5)
    NodeB = Node(4)
    NodeC = Node(6)
    NodeA.left = NodeB
    NodeA.right = NodeC
    print(NodeA)

    TreeA = Tree()
    TreeA + 1
    TreeA + 3
    TreeA + 2
    TreeA + 6
    TreeA + 1
    TreeA + 2
    print(TreeA)

if __name__ == "__main__":
    main()