import pytest
from challenges.graph.graph import Graph, Vertex, Edge

def test_add_vertex_pass():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'a'
    assert actual == expected

def test_add_vertex_fail():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'b'
    assert actual != expected

def test_add_node():
    graph = Graph()
    expected = 'a'
    actual = graph.add_node('a').value
    assert expected == actual
    
def test_add_edge_true():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    assert True

def test_size():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 2
    actual = graph.size()
    assert actual == expected
 
def test_size_fail():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 3
    actual = graph.size()
    assert actual != expected

def test_get_nodes():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, b)
    actual = graph.get_nodes()
    expected = ['a', 'b', 'c']
    assert actual == expected

def test_get_nodes_with_empty_graph():
    g = Graph()
    actual = g.get_nodes()
    expected = 'NULL'
    assert actual == expected

def test_get_neighbor():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, b)
    graph.add_edge(b, a)
    graph.add_edge(b, c)

    actual = graph.get_neighbor(b)

    expected = [('a', 1), ('c', 1)]

    assert actual == expected

def test_one_node_and_edge():
    graph = Graph()
    a = graph.add_node('a')
    graph.add_edge(a, a)
    actual = graph.get_neighbor(a)
    expected = [('a',1)]
    assert actual == expected

def test_breadth_first_circle_start_a():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, b)
    graph.add_edge(b, c)
    graph.add_edge(c, a)
    actual = graph.breadth_first(a)
    expected = ['a', 'b', 'c']
    assert actual == expected

def test_breadth_first_circle_start_b():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, b)
    graph.add_edge(b, c)
    graph.add_edge(c, a)
    actual = graph.breadth_first(b)
    expected = ['b', 'c', 'a']
    assert actual == expected

def test_breadth_first_code_challenge_example():
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
    actual = graph.breadth_first(a)
    expected = ['Pandora', 'Arendelle', 'Monstropolis', 'Metroville', 'Naboo', 'Narnia']
    assert actual == expected