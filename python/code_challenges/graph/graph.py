from ..Data_Structures.linked_list.linked_list.linked_list  import Linked_List,Node

# class  Adjacency_list:

#     def __init__(self):
#         self.node_list = []

#     def add_node(self,value):
#         node = Node(value)
#         linked = Linked_List()
#         linked.head = node
#         self.node_list.append(linked)
#         return node

#     def add_edge(self,node1=None,node2=None,weight=0):
#         first_linked = None
#         second_linked = None
#         for linked in self.node_list:
#             if linked.head.data == node1:
#                 first_linked = linked
#             elif linked.head.data == node2:
#                 second_linked = linked
#         if first_linked or second_linked:
#             if first_linked:
#                 if second_linked:
#                     first_linked.append({second_linked.head.data:weight})
#                 else:
#                     first_linked.append({second_linked:weight})
#             if second_linked:
#                 if first_linked:
#                     second_linked.append({first_linked.head.data:weight})
#                 else:
#                     second_linked.append({first_linked:weight})

#     def get_nodes(self):
#         nodes = []
#         for linked in self.node_list:
#             nodes.append(linked.head.data)
#         if len(nodes) == 0:
#             return None
#         return nodes

#     def get_neighbors(self,node):
#         neigbhors = []
#         for linked in self.node_list:
#             if linked.head.data == node:
#                 current = linked.head
#                 while current:
#                     neigbhors.append(current.data)
#                     current = current.next
#         return neigbhors

#     def size(self):
#         return len(self.node_list)

class ANode:

    def __init__(self,data):
        self.data = data
        self.edges = []

    def __str__(self):
        return f"{self.data}"

class  Adjacency_list:

    def __init__(self):
        self.node_list = []

    def add_node(self,value):
        node = ANode(value)
        linked = Linked_List()
        linked.head = node
        self.node_list.append(linked)
        return node

    def add_edge(self,node1=None,node2=None,weight=0):
        first_linked = None
        second_linked = None
        for linked in self.node_list:
            if linked.head.data == node1:
                first_linked = linked
            elif linked.head.data == node2:
                second_linked = linked
        if first_linked or second_linked:
            if first_linked:
                if second_linked:
                    first_linked.head.edges.append([second_linked.head,weight])
                else:
                    first_linked.head.edges.append([second_linked,weight])
            if second_linked:
                if first_linked:
                    second_linked.head.edges.append([first_linked.head,weight])
                else:
                    second_linked.head.edges.append([first_linked,weight])

    def get_nodes(self):
        nodes = []
        for linked in self.node_list:
            nodes.append(linked.head.data)
        if len(nodes) == 0:
            return None
        return nodes

    def get_neighbors(self,node):
        neigbhors = []
        for linked in self.node_list:
            if linked.head.data == node:
                current = linked.head
                neigbhors.append(current.data)
                for edge in current.edges:
                    neigbhors.append([str(edge[0]),edge[1]])
        return neigbhors

    def size(self):
        return len(self.node_list)

if __name__ == '__main__':
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
    print(aj_list.get_nodes())
    print(aj_list.get_neighbors('a'))
    print(aj_list.get_neighbors('b'))
    print(aj_list.get_neighbors('c'))
    print(aj_list.get_neighbors('d'))
    print(aj_list.get_neighbors('e'))
    print(aj_list.get_neighbors('f'))
    print(aj_list.size())
