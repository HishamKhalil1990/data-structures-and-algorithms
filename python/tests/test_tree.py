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
    tree = Binary_search_tree('23')
    actual = tree.add(8)  # ----> left to root (5)
    actual += "   " + tree.add(42) # ----> right to root (24)
    assert actual == expected

@pytest.fixture
def tree():
    node1 = Tree_Node('A')
    node1.left = Tree_Node('B')
    node1.right = Tree_Node('C')
    node1.left.left = Tree_Node('D')
    node1.left.right = Tree_Node('E')
    node1.right.left = Tree_Node('F')
    binary_tree = BinaryTree(node1)
    return binary_tree
