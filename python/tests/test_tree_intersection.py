# import pytest
# from code_challenges.tree_intersection.tree_intersection import tree_intersection
# from code_challenges.tree.tree import BinaryTree,Tree_Node

# def test_tree_intersection_1(first_setup_trees):
#     expected = [7, 11, 5]
#     tree1,tree2 = first_setup_trees
#     actual = tree_intersection(tree1,tree2)
#     assert expected == actual

# def test_tree_intersection_2(second_setup_trees):
#     expected = [100, 160, 125, 175, 200, 350, 500]
#     tree1,tree2 = second_setup_trees
#     actual = tree_intersection(tree1,tree2)
#     assert expected == actual

# def test_no_intersection(third_setup_trees):
#     tree1,tree2 = third_setup_trees
#     actual = tree_intersection(tree1,tree2)
#     assert not actual

# @pytest.fixture
# def first_setup_trees():
#     node1 = Tree_Node(2)
#     node1.left = Tree_Node(33)
#     node1.right = Tree_Node(5)
#     node1.left.left = Tree_Node(2)
#     node1.left.right = Tree_Node(6)
#     node1.left.right.left = Tree_Node(7)
#     node1.left.right.right = Tree_Node(11)
#     node1.right.right = Tree_Node(9)
#     node1.right.right.left = Tree_Node(4)
#     node2 = Tree_Node(3)
#     node2.left = Tree_Node(8)
#     node2.right = Tree_Node(5)
#     node2.left.left = Tree_Node(10)
#     node2.left.right = Tree_Node(23)
#     node2.left.right.left = Tree_Node(7)
#     node2.left.right.right = Tree_Node(11)
#     node2.right.right = Tree_Node(100)
#     node2.right.right.left = Tree_Node(61)
#     tree1 = BinaryTree(node1)
#     tree2 = BinaryTree(node2)
#     return tree1,tree2

# @pytest.fixture
# def second_setup_trees():
#     node3 = Tree_Node(150)
#     node3.left = Tree_Node(100)
#     node3.left.left = Tree_Node(75)
#     node3.left.right = Tree_Node(160)
#     node3.left.right.left = Tree_Node(125)
#     node3.left.right.right = Tree_Node(175)
#     node3.right = Tree_Node(250)
#     node3.right.left = Tree_Node(200)
#     node3.right.right = Tree_Node(350)
#     node3.right.right.left = Tree_Node(300)
#     node3.right.right.right = Tree_Node(500)
#     node4 = Tree_Node(42)
#     node4.left = Tree_Node(100)
#     node4.left.left = Tree_Node(15)
#     node4.left.right = Tree_Node(160)
#     node4.left.right.left = Tree_Node(125)
#     node4.left.right.right = Tree_Node(175)
#     node4.right = Tree_Node(600)
#     node4.right.left = Tree_Node(200)
#     node4.right.right = Tree_Node(350)
#     node4.right.right.left = Tree_Node(4)
#     node4.right.right.right = Tree_Node(500)
#     tree3 = BinaryTree(node3)
#     tree4 = BinaryTree(node4)
#     return tree3,tree4

# @pytest.fixture
# def third_setup_trees():
#     node1 = Tree_Node(1)
#     node1.left = Tree_Node(2)
#     node1.right = Tree_Node(3)
#     node1.left.left = Tree_Node(4)
#     node1.left.right = Tree_Node(5)
#     node1.left.right.left = Tree_Node(6)
#     node1.left.right.right = Tree_Node(7)
#     node2 = Tree_Node(8)
#     node2.left = Tree_Node(9)
#     node2.right = Tree_Node(10)
#     node2.left.left = Tree_Node(11)
#     node2.left.right = Tree_Node(12)
#     node2.left.right.left = Tree_Node(13)
#     node2.left.right.right = Tree_Node(14)
#     node2.right.right = Tree_Node(15)
#     node2.right.right.left = Tree_Node(16)
#     tree1 = BinaryTree(node1)
#     tree2 = BinaryTree(node2)
#     return tree1,tree2
