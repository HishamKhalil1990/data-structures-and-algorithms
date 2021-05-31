# import pytest
# from code_challenges.tree.tree.tree import Tree_Node,BinaryTree,EmptyTreeException

# def test_find_maximum_value_1():
#     expected = 11
#     node1 = Tree_Node(2)
#     node1.left = Tree_Node(7)
#     node1.right = Tree_Node(5)
#     node1.left.left = Tree_Node(2)
#     node1.left.right = Tree_Node(6)
#     node1.left.right.left = Tree_Node(5)
#     node1.left.right.left = Tree_Node(11)
#     node1.right.right = Tree_Node(9)
#     node1.right.right.left = Tree_Node(4)
#     binary_tree = BinaryTree(node1)
#     actual = binary_tree.find_maximum_value()
#     assert actual == expected

# def test_find_maximum_value_2():
#     expected = 25
#     node1 = Tree_Node(2)
#     node1.left = Tree_Node(7)
#     node1.right = Tree_Node(5)
#     node1.left.left = Tree_Node(2)
#     node1.left.right = Tree_Node(6)
#     node1.left.right.left = Tree_Node(5)
#     node1.left.right.left = Tree_Node(11)
#     node1.right.right = Tree_Node(9)
#     node1.right.right.left = Tree_Node(4)
#     node1.right.right.right = Tree_Node(13)
#     node1.right.right.left.left = Tree_Node(25)
#     node1.right.right.left.right = Tree_Node(3)
#     binary_tree = BinaryTree(node1)
#     actual = binary_tree.find_maximum_value()
#     assert actual == expected

# def test_find_maximum_value_in_empty_tree():
#     binary_tree = BinaryTree()
#     with pytest.raises(EmptyTreeException):
#         binary_tree.find_maximum_value()
