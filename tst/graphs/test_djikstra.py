from src.graphs.djikstra import get_weighted_shortest_paths
import networkx as nx

class TestDjikstra:
    def test_get_weighted_shortest_paths_acyclic(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B", weight=-5)
        graph.add_edge("A", "E", weight=7)
        graph.add_edge("B", "E", weight=6)
        graph.add_edge("E", "F", weight=3)
        graph.add_edge("B", "F", weight=-4)
        graph.add_edge("B", "C", weight=-1)
        graph.add_edge("F", "C", weight=8)
        graph.add_edge("F", "G", weight=2)
        graph.add_edge("G", "H", weight=-2)
        graph.add_edge("H", "C", weight=9)
        graph.add_edge("H", "D", weight=4)
        graph.add_edge("D", "C", weight=5)
        source = "E"

        expected_distances = {"A": float("inf"),
                              "B": float("inf"),
                              "E": 0,
                              "F": 3,
                              "C": 11,
                              "G": 5,
                              "H": 3,
                              "D": 7}

        expected_parents = {"E": None,
                            "F": "E",
                            "C": "F",
                            "G": "F",
                            "H": "G",
                            "D": "H"}

        actual_distances, actual_parents = get_weighted_shortest_paths(source, graph)

        assert actual_parents == expected_parents
        assert actual_distances == expected_distances
    
    def test_get_weighted_shortest_paths_positive_cycles(self):
        graph = nx.DiGraph()
        graph.add_edge("S", "A", weight=10)
        graph.add_edge("S", "C", weight=3)
        graph.add_edge("C", "A", weight=4)
        graph.add_edge("A", "C", weight=1)
        graph.add_edge("A", "B", weight=2)
        graph.add_edge("C", "B", weight=8)
        graph.add_edge("C", "D", weight=2)
        graph.add_edge("D", "B", weight=5)
        graph.add_edge("B", "D", weight=7)
        source = "S"

        expected_distances = {"S": 0,
                              "A": 7,
                              "B": 9,
                              "C": 3,
                              "D": 5}

        expected_parents = {"S": None,
                            "A": "C",
                            "D": "C",
                            "C": "S",
                            "B": "A"}

        actual_distances, actual_parents = get_weighted_shortest_paths(source, graph)

        assert actual_parents == expected_parents
        assert actual_distances == expected_distances
