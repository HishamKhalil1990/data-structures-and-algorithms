import pytest
from code_challenges.tree.tree.tree import Tree_Node,BinaryTree,Binary_search_tree,EmptyTreeException


def test_empty_tree():
    tree = Binary_search_tree()
    with pytest.raises(EmptyTreeException):
        tree.contains('1')

def test_instantiate_tree_with_root():
    expected = '5'
    tree = Binary_search_tree('5')
    actual = str(tree.root)
    assert actual == expected

def test_add_left_child_and_right_child_to_root_node():
    expected = '[23] ---edge--- [8]   [23] ---edge--- [42]'
    tree = Binary_search_tree('23') # ----> root
    actual = tree.add(8)  # ----> left to root (23)
    actual += "   " + tree.add(42) # ----> right to root (23)
    assert actual == expected

def test_check_if_value_exists_in_tree_true_1(tree):
    expected = True
    actual = tree.contains('16')
    assert actual == expected

def test_check_if_value_exists_in_tree_true_2(tree):
    expected = True
    actual = tree.contains('15')
    assert actual == expected

def test_check_if_value_exists_in_tree_false_1(tree):
    expected = False
    actual = tree.contains('7')
    assert actual == expected

def test_check_if_value_exists_in_tree_false_2(tree):
    expected = False
    actual = tree.contains('76')
    assert actual == expected

def test_collection_pre_order_traversal():
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    node1 = Tree_Node('A')
    node1.left = Tree_Node('B')
    node1.right = Tree_Node('C')
    node1.left.left = Tree_Node('D')
    node1.left.right = Tree_Node('E')
    node1.right.left = Tree_Node('F')
    binary_tree = BinaryTree(node1)
    actual = binary_tree.pre_order()
    assert actual == expected

def test_collection_in_order_traversal():
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    node1 = Tree_Node('A')
    node1.left = Tree_Node('B')
    node1.right = Tree_Node('C')
    node1.left.left = Tree_Node('D')
    node1.left.right = Tree_Node('E')
    node1.right.left = Tree_Node('F')
    binary_tree = BinaryTree(node1)
    actual = binary_tree.in_order()
    assert actual == expected

def test_collection_post_order_traversal():
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
    node1 = Tree_Node('A')
    node1.left = Tree_Node('B')
    node1.right = Tree_Node('C')
    node1.left.left = Tree_Node('D')
    node1.left.right = Tree_Node('E')
    node1.right.left = Tree_Node('F')
    binary_tree = BinaryTree(node1)
    actual = binary_tree.post_order()
    assert actual == expected

@pytest.fixture
def tree():
    tree = Binary_search_tree('23')
    tree.add(8)
    tree.add(42)
    tree.add(4)
    tree.add(16)
    tree.add(27)
    tree.add(85)
    tree.add(15)
    tree.add(22)
    tree.add(105)
    return tree
