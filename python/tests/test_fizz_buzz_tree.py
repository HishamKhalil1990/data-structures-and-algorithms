import pytest
from code_challenges.fizz_buzz_tree.fizz_buzz_tree import __version__
from code_challenges.fizz_buzz_tree.fizz_buzz_tree.fizz_buzz_tree import Fizz_Buzz_Tree
from code_challenges.fizz_buzz_tree.fizz_buzz_tree.tree import Tree_Node,BinaryTree,EmptyTreeException

def test_version():
    assert __version__ == '0.1.0'

def test_fizz_buzz_tree_one():
    #          [1, 13,   27,     33,   56,     15,        9,   17, 37]
    expected = [1, 13, 'Fizz', 'Fizz', 56, 'FizzBuzz', 'Fizz', 17, 37]
    node1 = Tree_Node(1) # ---> h0 root
    node1.left = Tree_Node(13) # ---> h1 left
    node1.right = Tree_Node(27) # ---> h1 right
    node1.left.left = Tree_Node(33) # ---> h2 left root 7
    node1.left.right = Tree_Node(56) # ---> h2 right root 7
    node1.right.right = Tree_Node(15) # ---> h2 left root 5
    node1.left.right.left = Tree_Node(9) # ---> h3 left root 6
    node1.left.right.right = Tree_Node(17) # ---> h3 right root 6
    node1.right.right.left = Tree_Node(37) # ---> h3 left root 9
    bt = BinaryTree(node1)
    new_bt = Fizz_Buzz_Tree(bt)
    actual = new_bt.breadth_first(new_bt)
    assert actual == expected

def test_fizz_buzz_tree_two():
    #          [   3,   8,    5,   2,    6,     10,      9,     24,   34,   5,    11, 4,     15    ]
    expected = ['Fizz', 8, 'Buzz', 2, 'Fizz', 'Buzz', 'Fizz', 'Fizz', 34, 'Buzz', 11, 4, 'FizzBuzz']
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
    bt = BinaryTree(node1)
    new_bt = Fizz_Buzz_Tree(bt)
    actual = new_bt.breadth_first(new_bt)
    assert actual == expected

def test_fizz_buzz_tree_empty_input_tree():
    with pytest.raises(EmptyTreeException):
        binary_tree = BinaryTree()
        Fizz_Buzz_Tree(binary_tree)
