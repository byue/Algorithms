import src.graphs.single_source_shortest_paths.bellman_ford.bellman_ford as bellman_ford
import networkx as nx

class TestBellmanFord:
    def test_get_sssp_negative_cycle(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B", weight=-5)
        graph.add_edge("B", "A", weight=-5)
        source = "A"

        expected_distances = None

        expected_parents = None

        actual_distances, actual_parents = bellman_ford.get_sssp(source, graph)

        assert actual_parents == expected_parents
        assert actual_distances == expected_distances

    def test_get_sssp_acyclic(self):
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

        actual_distances, actual_parents = bellman_ford.get_sssp(source, graph)

        assert actual_parents == expected_parents
        assert actual_distances == expected_distances

    def test_get_sssp_positive_cycles(self):
        graph = nx.DiGraph()
        graph.add_edge("S", "A", weight=10)
        graph.add_edge("S", "E", weight=8)
        graph.add_edge("E", "D", weight=1)
        graph.add_edge("D", "A", weight=-4)
        graph.add_edge("D", "C", weight=-1)
        graph.add_edge("A", "C", weight=2)
        graph.add_edge("C", "B", weight=-2)
        graph.add_edge("B", "A", weight=1)

        source = "S"

        expected_distances = {"S": 0,
                              "A": 5,
                              "B": 5,
                              "C": 7,
                              "D": 9,
                              "E": 8}

        expected_parents = {"S": None,
                            "E": "S",
                            "A": "D",
                            "D": "E",
                            "C": "A",
                            "B": "C"}

        actual_distances, actual_parents = bellman_ford.get_sssp(source, graph)

        assert actual_parents == expected_parents
        assert actual_distances == expected_distances
