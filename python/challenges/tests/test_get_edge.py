import pytest
from challenges.get_edge.get_edge import Graph, Vertex, Edge

def test_get_edge_with_one_way_flight():
    graph = Graph()
    a = graph.add_node('a')
    c = graph.add_node('c')
    graph.add_edge(a, c, 345)
    actual = graph.get_edge([a,c])
    expected = (True, '$345')
    assert actual == expected

def test_get_edge_with_connecting_flight():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, b, 10)
    graph.add_edge(b, c, 345)
    actual = graph.get_edge([a,b,c])
    expected = (True, '$355')
    assert actual == expected

def test_get_edge_with_no_flight_available():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, c, 345)
    actual = graph.get_edge([a,b])
    expected = (False, '$0')
    assert actual == expected