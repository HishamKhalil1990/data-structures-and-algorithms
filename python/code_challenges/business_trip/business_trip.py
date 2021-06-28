from ..graph.graph import Graph

def business_trip(graph, city_arr):
    node_list = graph.get_nodes()
    node_dict = {}
    weight = 0
    for node in node_list:
        node_dict[node.value] = node
    for index in range(len(city_arr) - 1):
        first_city = city_arr[index]
        second_city = city_arr[index + 1]
        first_node = node_dict[first_city]
        second_node = node_dict[second_city]
        first_city_neighbors = graph.get_neighbors(first_node)
        linked = False
        for edge in first_city_neighbors:
            if edge.vertex == second_node:
                weight += edge.weight
                linked = True
        if not linked:
            return None
    return weight

if __name__ == "__main__":
    g = Graph()
    node1 = g.add_node('Pandora')
    node2 = g.add_node('Arendelle')
    node3 = g.add_node('Metroville')
    node4 = g.add_node('Monstropolis')
    node5 = g.add_node('Narnia')
    node6 = g.add_node('Naboo')
    g.add_edge(node1, node2, 150)
    g.add_edge(node1, node3, 82)
    g.add_edge(node2, node3, 99)
    g.add_edge(node2, node4, 42)
    g.add_edge(node3, node4, 105)
    g.add_edge(node3, node5, 37)
    g.add_edge(node3, node6, 26)
    g.add_edge(node4, node6, 73)
    g.add_edge(node5, node6, 250)
    print(business_trip(g,['Metroville','Pandora']))
    print('new---------------------------------')
    print(business_trip(g,['Arendelle','Monstropolis','Naboo']))
    print('new---------------------------------')
    print(business_trip(g,['Naboo','Pandora']))
    print('new---------------------------------')
    print(business_trip(g,['Narnia','Arendelle','Naboo']))
