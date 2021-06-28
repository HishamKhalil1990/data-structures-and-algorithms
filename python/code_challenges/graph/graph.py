from collections import deque
from typing import Set

class Vertex:

    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

class Edge:

    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight

class Queue():

    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

class  Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self,value):
        node = Vertex(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self,node1=None,node2=None,weight1=0):
        if node1 not in self.adjacency_list:
            raise KeyError
        elif node2 not in self.adjacency_list:
            raise KeyError
        else:
            edge = Edge(vertex=node2,weight=weight1)
            self.adjacency_list[node1].append(edge)
            edge = Edge(vertex=node1,weight=weight1)
            self.adjacency_list[node2].append(edge)

    def get_nodes(self):
       return self.adjacency_list.keys()

    def get_neighbors(self,node):
        return self.adjacency_list.get(node,[])

    def size(self):
        return len(self.adjacency_list)

    def breadth_first(self,node):
        queue = Queue()
        queue.enqueue(node)
        visited  = set()
        visited.add(node)
        node_list = []
        def inner_func(queue,visited,node_list):
            for index in range(len(queue)):
                node = queue.dequeue()
                node_list.append(node)
                neighbors = self.get_neighbors(node)
                for edge in neighbors:
                    if edge.vertex not in visited:
                        queue.enqueue(edge.vertex)
                        visited.add(edge.vertex)
            if len(queue) > 0:
                inner_func(queue,visited,node_list)
        inner_func(queue,visited,node_list)
        return node_list

if __name__ == '__main__':
    graph = Graph()
    node_a = graph.add_node('a')
    node_b = graph.add_node('b')
    node_c = graph.add_node('c')
    node_d = graph.add_node('d')
    node_e = graph.add_node('e')
    node_f = graph.add_node('f')
    graph.add_edge(node_a,node_c)
    graph.add_edge(node_a,node_d)
    graph.add_edge(node_b,node_c)
    graph.add_edge(node_b,node_f)
    graph.add_edge(node_c,node_e)
    graph.add_edge(node_d ,node_e)
    graph.add_edge(node_e,node_f)
    print(graph.get_nodes())
    print(graph.get_neighbors(node_a))
    print(graph.get_neighbors(node_b))
    print(graph.get_neighbors(node_c))
    print(graph.get_neighbors(node_d))
    print(graph.get_neighbors(node_e))
    print(graph.get_neighbors(node_f))
    print(graph.size())
    for node in graph.breadth_first(node_a):
        print(node.value)
    g = Graph()
    node1 = g.add_node('Pandora')
    node2 = g.add_node('Arendelle')
    node5 = g.add_node('Narnia')
    node3 = g.add_node('Metroville')
    node4 = g.add_node('Monstroplolis')
    node6 = g.add_node('Naboo')
    g.add_edge(node1, node2)
    g.add_edge(node2, node3)
    g.add_edge(node3, node4)
    g.add_edge(node3, node5)
    g.add_edge(node3, node6)
    g.add_edge(node4, node6)
    g.add_edge(node5, node6)
    for node in g.breadth_first(node1):
        print(node.value)