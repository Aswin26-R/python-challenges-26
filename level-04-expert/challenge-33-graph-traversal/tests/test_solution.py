import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from starter import Graph


def make_sample_graph():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")
    return g


class TestGraphBasics:
    def test_add_node(self):
        g = Graph()
        g.add_node("A")
        assert "A" in g.adjacency_list

    def test_add_edge_creates_nodes(self):
        g = Graph()
        g.add_edge("A", "B")
        assert "A" in g.adjacency_list
        assert "B" in g.adjacency_list

    def test_add_edge_bidirectional(self):
        g = Graph()
        g.add_edge("A", "B")
        assert "B" in g.get_neighbors("A")
        assert "A" in g.get_neighbors("B")

    def test_get_neighbors_empty(self):
        g = Graph()
        g.add_node("A")
        assert g.get_neighbors("A") == []

    def test_get_neighbors_missing_node(self):
        g = Graph()
        assert g.get_neighbors("X") == []


class TestBFS:
    def test_bfs_visits_all(self):
        g = make_sample_graph()
        result = g.bfs("A")
        assert sorted(result) == ["A", "B", "C", "D", "E"]

    def test_bfs_starts_with_start(self):
        g = make_sample_graph()
        result = g.bfs("A")
        assert result[0] == "A"

    def test_bfs_returns_list(self):
        g = make_sample_graph()
        assert isinstance(g.bfs("A"), list)

    def test_bfs_single_node(self):
        g = Graph()
        g.add_node("X")
        assert g.bfs("X") == ["X"]

    def test_bfs_missing_start(self):
        g = Graph()
        assert g.bfs("Z") == []


class TestDFS:
    def test_dfs_visits_all(self):
        g = make_sample_graph()
        result = g.dfs("A")
        assert sorted(result) == ["A", "B", "C", "D", "E"]

    def test_dfs_starts_with_start(self):
        g = make_sample_graph()
        result = g.dfs("A")
        assert result[0] == "A"

    def test_dfs_returns_list(self):
        g = make_sample_graph()
        assert isinstance(g.dfs("A"), list)

    def test_dfs_missing_start(self):
        g = Graph()
        assert g.dfs("Z") == []


class TestHasPath:
    def test_direct_path(self):
        g = make_sample_graph()
        assert g.has_path("A", "B") is True

    def test_indirect_path(self):
        g = make_sample_graph()
        assert g.has_path("A", "E") is True

    def test_no_path(self):
        g = Graph()
        g.add_node("A")
        g.add_node("B")
        assert g.has_path("A", "B") is False

    def test_missing_node(self):
        g = make_sample_graph()
        assert g.has_path("A", "X") is False


class TestShortestPath:
    def test_same_node(self):
        g = make_sample_graph()
        assert g.shortest_path("A", "A") == ["A"]

    def test_direct_neighbor(self):
        g = make_sample_graph()
        path = g.shortest_path("A", "B")
        assert path[0] == "A"
        assert path[-1] == "B"
        assert len(path) == 2

    def test_path_exists(self):
        g = make_sample_graph()
        path = g.shortest_path("A", "E")
        assert path[0] == "A"
        assert path[-1] == "E"
        assert len(path) == 4

    def test_no_path_returns_empty(self):
        g = Graph()
        g.add_node("A")
        g.add_node("Z")
        assert g.shortest_path("A", "Z") == []

    def test_path_is_connected(self):
        g = make_sample_graph()
        path = g.shortest_path("A", "E")
        for i in range(len(path) - 1):
            assert path[i+1] in g.get_neighbors(path[i])
