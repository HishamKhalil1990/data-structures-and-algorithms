# import pytest
# from code_challenges.tree.tree.tree import Tree_Node,BinaryTree,EmptyTreeException

# def test_breadth_first_one():
#     expected = [2,7,5,2,6,9,5,11,4]
#     node1 = Tree_Node(2) # ---> h0 root
#     node1.left = Tree_Node(7) # ---> h1 left
#     node1.right = Tree_Node(5) # ---> h1 right
#     node1.left.left = Tree_Node(2) # ---> h2 left root 7
#     node1.left.right = Tree_Node(6) # ---> h2 right root 7
#     node1.right.right = Tree_Node(9) # ---> h2 left root 5
#     node1.left.right.left = Tree_Node(5) # ---> h3 left root 6
#     node1.left.right.right = Tree_Node(11) # ---> h3 right root 6
#     node1.right.right.left = Tree_Node(4) # ---> h3 left root 9
#     binary_tree = BinaryTree(node1)
#     actual = binary_tree.breadth_first(binary_tree)
#     assert actual == expected

# def test_breadth_first_two():
#     expected = [3,8,5,2,6,10,9,24,34,5,11,4,16]
#     node1 = Tree_Node(3) # ---> h0 root
#     node1.left = Tree_Node(8) # ---> h1 left
#     node1.right = Tree_Node(5) # ---> h1 right
#     node1.left.left = Tree_Node(2) # ---> h2 left root 8
#     node1.left.right = Tree_Node(6) # ---> h2 right root 8
#     node1.right.left = Tree_Node(10) # ---> h2 left root 5
#     node1.right.right = Tree_Node(9) # ---> h2 right root 5
#     node1.left.left.left = Tree_Node(24) # ---> h3 left root 2
#     node1.left.left.right = Tree_Node(34) # ---> h3 right root 2
#     node1.left.right.left = Tree_Node(5) # ---> h3 left root 6
#     node1.left.right.right = Tree_Node(11) # ---> h3 right root 6
#     node1.right.right.left = Tree_Node(4) # ---> h3 left root 9
#     node1.right.right.right = Tree_Node(16) # ---> h3 right root 9
#     binary_tree = BinaryTree(node1)
#     actual = binary_tree.breadth_first(binary_tree)
#     assert actual == expected

# def test_breadth_first_empty():
#     with pytest.raises(EmptyTreeException):
#         binary_tree = BinaryTree()
#         binary_tree.breadth_first(binary_tree)
