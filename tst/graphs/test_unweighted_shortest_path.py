from src.graphs.bfs import bfs
from src.graphs.unweighted_shortest_path import unweighted_shorted_path
import networkx as nx

class TestUnweightedShortestPath:
    def test_unweighted_shortest_path_no_parent_for_destination(self):
        graph = nx.Graph()
        graph.add_node("A")

        actual_parent = bfs("A", graph)

        actual_path = unweighted_shorted_path(actual_parent, "D", "A")

        assert actual_path is None

    def test_unweighted_shortest_path_no_path(self):
        graph = nx.Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("A", "D")
        graph.add_edge("D", "E")
        graph.add_edge("D", "F")
        graph.add_edge("D", "G")
        graph.add_edge("F", "H")
        graph.add_edge("F", "I")
        graph.add_edge("I", "J")

        actual_parent = bfs("A", graph)

        actual_path = unweighted_shorted_path(actual_parent, "Z", "I")

        assert actual_path is None

    def test_unweighted_shortest_path_middle(self):        
        graph = nx.Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("A", "D")
        graph.add_edge("D", "E")
        graph.add_edge("D", "F")
        graph.add_edge("D", "G")
        graph.add_edge("F", "H")
        graph.add_edge("F", "I")
        graph.add_edge("I", "J")

        expected_path = ["D", "F", "I"]

        actual_parent = bfs("A", graph)

        actual_path = unweighted_shorted_path(actual_parent, "D", "I")

        assert actual_path == expected_path
