import src.graphs.single_source_shortest_paths.dag.dag as dag
import networkx as nx

class TestDagRelaxationShortestPaths:
    def test_get_sssp_cycle(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B", weight=-5)
        graph.add_edge("B", "A", weight=-5)
        source = "A"

        expected_distances = {"A": 0,
                              "B": float("inf")}

        expected_parents = {"A": None}

        actual_distances, actual_parents = dag.get_sssp(source, graph)

        assert actual_parents == expected_parents
        assert actual_distances == expected_distances

    def test_get_sssp(self):
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

        actual_distances, actual_parents = dag.get_sssp(source, graph)

        assert actual_parents == expected_parents
        assert actual_distances == expected_distances
