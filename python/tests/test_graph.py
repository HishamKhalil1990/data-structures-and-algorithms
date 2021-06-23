import pytest
from code_challenges.graph.graph import Adjacency_list

def test_add_node():
    expected = 'a'
    aj_list = Adjacency_list()
    actual = aj_list.add_node('a')
    assert str(actual) == expected

def test_add_edge():
    aj_list = Adjacency_list()
    aj_list.add_node('a')
    aj_list.add_node('b')
    aj_list.add_edge('a','b')
    expected = ['b',0]
    edge = aj_list.node_list[0].head.edges[0]
    actual = [str(edge[0]),edge[1]]
    assert actual == expected
    aj_list.add_node('c')
    aj_list.add_node('d')
    aj_list.add_edge('c','d',3)
    expected = ['d',3]
    edge = aj_list.node_list[2].head.edges[0]
    actual = [str(edge[0]),edge[1]]
    assert actual == expected

def test_get_nodes(adjacency_list):
    expected = ['a', 'b', 'c', 'd', 'e', 'f']
    actual = adjacency_list.get_nodes()
    assert actual == expected

def test_get_neighbors(adjacency_list):
    expected = ['c', ['a', 0], ['b', 0], ['e', 0]]
    actual = adjacency_list.get_neighbors('c')
    assert actual == expected

def test_get_neighbors_with_wieght(adjacency_list_2):
    expected = ['c', ['a', 5], ['b', 7], ['e', 4]]
    actual = adjacency_list_2.get_neighbors('c')
    assert actual == expected

def test_get_size(adjacency_list):
    expected = 6
    actual = adjacency_list.size()
    assert actual == expected

def test_one_node_one_edge():
    expected = ['a', ['None', 0]]
    aj_list = Adjacency_list()
    aj_list.add_node('a')
    aj_list.add_edge('a')
    actual = aj_list.get_neighbors('a')
    assert actual == expected

def test_empty_graph():
    aj_list = Adjacency_list()
    actual = aj_list.get_nodes()
    assert not actual

@pytest.fixture
def adjacency_list():
    aj_list = Adjacency_list()
    aj_list.add_node('a')
    aj_list.add_node('b')
    aj_list.add_node('c')
    aj_list.add_node('d')
    aj_list.add_node('e')
    aj_list.add_node('f')
    aj_list.add_edge('a','c')
    aj_list.add_edge('a','d')
    aj_list.add_edge('b','c')
    aj_list.add_edge('b','f')
    aj_list.add_edge('c','e')
    aj_list.add_edge('d','e')
    aj_list.add_edge('e','f')
    return aj_list

@pytest.fixture
def adjacency_list_2():
    aj_list = Adjacency_list()
    aj_list.add_node('a')
    aj_list.add_node('b')
    aj_list.add_node('c')
    aj_list.add_node('d')
    aj_list.add_node('e')
    aj_list.add_node('f')
    aj_list.add_edge('a','c',5)
    aj_list.add_edge('a','d',3)
    aj_list.add_edge('b','c',7)
    aj_list.add_edge('b','f',1)
    aj_list.add_edge('c','e',4)
    aj_list.add_edge('d','e',8)
    aj_list.add_edge('e','f',2)
    return aj_list
