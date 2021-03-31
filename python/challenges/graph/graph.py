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

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex 
        self.weight = weight

if __name__ == '__main__':
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, b)
    graph.add_edge(b, a)
    graph.add_edge(b, c)
    
    g = Graph()
    print(g.get_nodes())
    # print(graph.get_neighbor(b))
