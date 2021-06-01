from .tree import BinaryTree,Queue,EmptyTreeException,Tree_Node

def Fizz_Buzz_Tree(Binary_tree):

    def fuzz_buzz(value):
        if value % 3 == 0 and value % 5 == 0:
            return 'FizzBuzz'
        elif value % 3 == 0:
            return "Fizz"
        elif value % 5 == 0:
            return "Buzz"
        else:
            return value

    root = Binary_tree.root
    if not root:
            raise EmptyTreeException
    new_root = Tree_Node(root.value)
    new_tree = BinaryTree(new_root)
    roots = Queue()
    roots.enqueue(root)
    new_root.value = fuzz_buzz(new_root.value)
    new_rootsque = Queue()
    new_rootsque.enqueue(new_root)
    def inner_func(roots):
        for num in range(len(roots)):
            left = roots.peek().left
            right = roots.peek().right
            roots.dequeue()
            if left:
                new_left = Tree_Node(fuzz_buzz(left.value))
                new_rootsque.peek().left = new_left
                roots.enqueue(left)
                new_rootsque.enqueue(new_left)
            if right:
                new_right = Tree_Node(fuzz_buzz(right.value))
                new_rootsque.peek().right = new_right
                roots.enqueue(right)
                new_rootsque.enqueue(new_right)
            new_rootsque.dequeue()
        if len(roots) > 0:
            inner_func(roots)

    inner_func(roots)

    return new_tree

if __name__ == "__main__":
    node1 = Tree_Node(1)
    node1.left = Tree_Node(13)
    node1.right = Tree_Node(27)
    node1.left.left = Tree_Node(33)
    node1.left.right = Tree_Node(56)
    node1.left.right.left = Tree_Node(9)
    node1.left.right.right = Tree_Node(17)
    node1.right.right = Tree_Node(15)
    node1.right.right.left = Tree_Node(37)
    binary_tree = BinaryTree(node1)
    new_bt = Fizz_Buzz_Tree(binary_tree)
    print(new_bt.breadth_first(new_bt))
    print(binary_tree.breadth_first(binary_tree))
    print(binary_tree.pre_order())
    print(new_bt.pre_order())
    print(binary_tree.in_order())
    print(new_bt.in_order())
    print(binary_tree.post_order())
    print(new_bt.post_order())
    node1 = Tree_Node(3) # ---> h0 root
    node1.left = Tree_Node(8) # ---> h1 left
    node1.right = Tree_Node(5) # ---> h1 right
    node1.left.left = Tree_Node(2) # ---> h2 left root 8
    node1.left.right = Tree_Node(6) # ---> h2 right root 8
    node1.right.left = Tree_Node(10) # ---> h2 left root 5
    node1.right.right = Tree_Node(9) # ---> h2 right root 5
    node1.left.left.left = Tree_Node(24) # ---> h3 left root 2
    node1.left.left.right = Tree_Node(34) # ---> h3 right root 2
    node1.left.right.left = Tree_Node(5) # ---> h3 left root 6
    node1.left.right.right = Tree_Node(11) # ---> h3 right root 6
    node1.right.right.left = Tree_Node(4) # ---> h3 left root 9
    node1.right.right.right = Tree_Node(15) # ---> h3 right root 9
    binary_tree = BinaryTree(node1)
    new_bt = Fizz_Buzz_Tree(binary_tree)
    print(new_bt.breadth_first(new_bt))
    print(binary_tree.breadth_first(binary_tree))
