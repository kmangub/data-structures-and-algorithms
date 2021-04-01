class Graph:

    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v
    
    def add_edge(self, start_vertex, end_vertex, weight =1):
        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in Graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in Graph')

        edge = Edge(end_vertex, weight)

        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)
        return (start_vertex.value, end_vertex.value, weight)

    def get_nodes(self):
        list_of_nodes = []
        if self.size() == 0:
            return 'NULL'
        for node in self._adjacency_list:
            list_of_nodes.append(node.value)
        return list_of_nodes

    def get_neighbor(self, node):
        neighbor_list = []
        neighbors = self._adjacency_list[node]

        for edge in neighbors:
            node = []
            node.append(edge.vertex.value)
            node.append(edge.weight)
            tup = tuple(node)
            neighbor_list.append(tup)

        return neighbor_list

    def size(self):
        return len(self._adjacency_list)
    
    def breadth_first(self, vertex):
        breadth = []
        visited = []

        breadth.append(vertex)
        visited.append(vertex.value)

        while len(breadth) != 0:
            node = breadth.pop()
            neighbor = self._adjacency_list[node]
            for edge in neighbor:
                if edge.vertex.value not in visited:
                    visited.append(edge.vertex.value)
                    breadth.append(edge.vertex)
        return visited


class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex 
        self.weight = weight

if __name__ == '__main__':
    # graph = Graph()
    # a = graph.add_node('a')
    # b = graph.add_node('b')
    # c = graph.add_node('c')
    # graph.add_edge(a, b)
    # graph.add_edge(b, c)
    # graph.add_edge(c, a)
    # print(graph.breadth_first(b))
    # g = Graph()
    # print(g.get_nodes())
    # print(graph.get_neighbor(b))
    graph = Graph()
    a = graph.add_node('Pandora')
    b = graph.add_node('Arendelle')
    c = graph.add_node('Metroville')
    d = graph.add_node('Monstropolis')
    e = graph.add_node('Naboo')
    f = graph.add_node('Narnia')
    graph.add_edge(a, b)
    graph.add_edge(b, d)
    graph.add_edge(b, c)
    graph.add_edge(c, d)
    graph.add_edge(c, e)
    graph.add_edge(c, f)
    graph.add_edge(f, e)
    print(graph.breadth_first(a))

 
