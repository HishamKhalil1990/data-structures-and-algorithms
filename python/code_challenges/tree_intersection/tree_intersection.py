from ..hashtable.hashtable import HashTable
from ..tree.tree import BinaryTree,Tree_Node

def tree_intersection(tree1,tree2):
    tree1_list = tree1.pre_order()
    tree2_list = tree2.pre_order()
    common = []
    hashtable = HashTable()
    for counter in range(len(tree1_list)):
        hashtable.add(str(tree1_list[counter]),1)
    for num in tree2_list:
        if hashtable.contains(str(num)):
            common += [num]
    if len(common) > 0:
        return common
    return False

if __name__ == '__main__':
    node1 = Tree_Node(2)
    node1.left = Tree_Node(33)
    node1.right = Tree_Node(5)
    node1.left.left = Tree_Node(2)
    node1.left.right = Tree_Node(6)
    node1.left.right.left = Tree_Node(7)
    node1.left.right.right = Tree_Node(11)
    node1.right.right = Tree_Node(9)
    node1.right.right.left = Tree_Node(4)
    node2 = Tree_Node(3)
    node2.left = Tree_Node(8)
    node2.right = Tree_Node(5)
    node2.left.left = Tree_Node(10)
    node2.left.right = Tree_Node(23)
    node2.left.right.left = Tree_Node(7)
    node2.left.right.right = Tree_Node(11)
    node2.right.right = Tree_Node(100)
    node2.right.right.left = Tree_Node(61)
    tree1 = BinaryTree(node1)
    tree2 = BinaryTree(node2)
    print(tree_intersection(tree1,tree2))
    node3 = Tree_Node(150)
    node3.left = Tree_Node(100)
    node3.left.left = Tree_Node(75)
    node3.left.right = Tree_Node(160)
    node3.left.right.left = Tree_Node(125)
    node3.left.right.right = Tree_Node(175)
    node3.right = Tree_Node(250)
    node3.right.left = Tree_Node(200)
    node3.right.right = Tree_Node(350)
    node3.right.right.left = Tree_Node(300)
    node3.right.right.right = Tree_Node(500)
    node4 = Tree_Node(42)
    node4.left = Tree_Node(100)
    node4.left.left = Tree_Node(15)
    node4.left.right = Tree_Node(160)
    node4.left.right.left = Tree_Node(125)
    node4.left.right.right = Tree_Node(175)
    node4.right = Tree_Node(600)
    node4.right.left = Tree_Node(200)
    node4.right.right = Tree_Node(350)
    node4.right.right.left = Tree_Node(4)
    node4.right.right.right = Tree_Node(500)
    tree3 = BinaryTree(node3)
    tree4 = BinaryTree(node4)
    print(tree_intersection(tree3,tree4))
