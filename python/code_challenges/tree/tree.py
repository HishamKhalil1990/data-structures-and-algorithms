
class EmptyTreeException(Exception):
    def __init__(self):
        pass

class Node():
    def __init__(self,value=None):
        self.value = value
        self.next = None

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def is_empty(self):
        if not self.front:
            return False
        return True

    def enqueue(self,value):
        if not self.is_empty():
            self.front = Node(value)
            self.rear = self.front
        else:
            new_node = Node(value)
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    def dequeue(self):
        if not self.is_empty():
            raise EmptyTreeException
        else:
            value = self.front.value
            self.front = self.front.next
            self.length -= 1
            return value

    def peek(self):
        if not self.is_empty():
            raise EmptyTreeException
        else:
            return self.front.value

    def __str__(self):
        if not self.is_empty():
            raise EmptyTreeException
        else:
            string = ""
            current = self.front
            while current != None:
                string += str(current.value) + ' '
                current = current.next
            return string

    def __len__(self):
        return self.length

class Tree_Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"

class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.tree_list = []
        self.maximum = None
        self.roots = Queue()

    # Pre-order traversal
    def pre_order(self):
        self.tree_list = []
        def inner_func(root):
            self.tree_list.append(root.value)
            if root.left:
                inner_func(root.left)
            if root.right:
                inner_func(root.right)
        inner_func(self.root)
        return self.tree_list

    # in-order traversal
    def in_order(self):
        self.tree_list = []
        def inner_func(root):
            if root.left:
                inner_func(root.left)
            self.tree_list.append(root.value)
            if root.right:
                inner_func(root.right)
        inner_func(self.root)
        return self.tree_list

    # post-order traversal
    def post_order(self):
        self.tree_list = []
        def inner_func(root):
            if root.left:
                inner_func(root.left)
            if root.right:
                inner_func(root.right)
            self.tree_list.append(root.value)
        inner_func(self.root)
        return self.tree_list

    def find_maximum_value(self):
        self.maximum = None
        def inner_func(root):
            if not self.maximum:
                if not root:
                    raise EmptyTreeException
                else:
                    self.maximum = root.value
            elif root.value >= self.maximum:
                self.maximum = root.value
            if root.left:
                inner_func(root.left)
            if root.right:
                inner_func(root.right)
        inner_func(self.root)
        return self.maximum

    def breadth_first(self,tree):
        if not tree.root:
            raise EmptyTreeException
        self.roots = Queue()
        self.roots.enqueue(tree.root)
        self.tree_list = []
        self.tree_list.append(self.roots.peek().value)
        def inner_func(roots):
            for num in range(len(roots)):
                left = roots.peek().left
                right = roots.peek().right
                roots.dequeue()
                if left:
                    self.tree_list.append(left.value)
                    self.roots.enqueue(left)
                if right:
                    self.tree_list.append(right.value)
                    self.roots.enqueue(right)
            if len(roots) > 0:
                inner_func(roots)
        inner_func(self.roots)
        return self.tree_list

class Binary_search_tree:
    def __init__(self, root=None):
        if not root:
            self.root = None
        else:
            self.root = Tree_Node(int(root))
        self.tree_list = []
        self.found = False

    def add(self, value, root=None):
        self.tree_list = []
        def inner_function(value, root=None):
            if not self.root:
                self.root = Tree_Node(value)
                self.tree_list.append(f"[{self.root.value}]")
            elif not root:
                inner_function(value, self.root)
            else:
                self.tree_list.append(f"[{root.value}] ---edge--- ")
                if value < root.value:
                    if not root.left:
                        root.left = Tree_Node(value)
                        self.tree_list.append(f"[{root.left.value}]")
                    else:
                        inner_function(value, root.left)
                if value > root.value:
                    if not root.right:
                        root.right = Tree_Node(value)
                        self.tree_list.append(f"[{root.right.value}]")
                    else:
                        inner_function(value, root.right)
        inner_function(value)
        returned_string = ""
        for string in self.tree_list:
            returned_string += string
        return returned_string

    def contains(self, value, root=None):
        value = int(value)
        if not self.root:
            raise EmptyTreeException
        elif not root:
            self.contains(value, self.root)
        else:
            if value == root.value:
                self.found = True
            if value < root.value:
                if not root.left:
                    self.found = False
                else:
                    self.contains(value, root.left)
            if value > root.value:
                if not root.right:
                    self.found = False
                else:
                    self.contains(value, root.right)
        return self.found

if __name__ == "__main__":
    node1 = Tree_Node(2)
    node1.left = Tree_Node(7)
    node1.right = Tree_Node(5)
    node1.left.left = Tree_Node(2)
    node1.left.right = Tree_Node(6)
    node1.left.right.left = Tree_Node(5)
    node1.left.right.right = Tree_Node(11)
    node1.right.right = Tree_Node(9)
    node1.right.right.left = Tree_Node(4)
    binary_tree = BinaryTree(node1)
    print(binary_tree.breadth_first(binary_tree))
    # print(binary_tree.find_maximum_value())
    # print(binary_tree.pre_order())
    # print(binary_tree.in_order())
    # print(binary_tree.post_order())
    # tree = Binary_search_tree('23')
    # print(tree.add(8))
    # print(tree.add(42))
    # print(tree.add(4))
    # print(tree.add(16))
    # print(tree.add(27))
    # print(tree.add(85))
    # print(tree.add(15))
    # print(tree.add(22))
    # print(tree.add(105))
    # print('True section for contains method')
    # print(tree.contains(23))
    # print(tree.contains(8))
    # print(tree.contains(42))
    # print(tree.contains(4))
    # print(tree.contains(16))
    # print(tree.contains(27))
    # print(tree.contains(85))
    # print(tree.contains(15))
    # print(tree.contains(22))
    # print(tree.contains(105))
    # print('false section for contains method')
    # print(tree.contains(7))
    # print(tree.contains(40))
    # print(tree.contains(3))
    # print(tree.contains(106))
    # print(tree.contains(50))
    # print(tree.contains(65))
    # print(tree.contains(10))
    # print(tree.contains(78))
    # print(tree.contains(90))
