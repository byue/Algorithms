import src.graphs.single_source_shortest_paths.bfs.bfs as bfs
from src.graphs.unweighted_shortest_path import unweighted_shorted_path
import networkx as nx

class TestUnweightedShortestPath:
    def test_unweighted_shortest_path_no_parent_for_destination(self):
        graph = nx.Graph()
        graph.add_node("A")

        _, actual_parent = bfs.get_sssp("A", graph)

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

        _, actual_parent = bfs.get_sssp("A", graph)

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

        _, actual_parent = bfs.get_sssp("A", graph)

        actual_path = unweighted_shorted_path(actual_parent, "D", "I")

        assert actual_path == expected_path
