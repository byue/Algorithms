import src.graphs.single_source_shortest_paths.bfs.bfs as bfs
import networkx as nx

class TestBFS:
    def test_bfs(self):
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

        expected_parent = {
            "A": None,
            "B": "A",
            "C": "A",
            "D": "A",
            "E": "D",
            "F": "D",
            "G": "D",
            "H": "F",
            "I": "F",
            "J": "I"
        }

        expected_distances = {
            "A": 0,
            "B": 1,
            "C": 1,
            "D": 1,
            "E": 2,
            "F": 2,
            "G": 2,
            "H": 3,
            "I": 3,
            "J": 4
        }

        actual_distances, actual_parent = bfs.get_sssp("A", graph)
        assert actual_parent == expected_parent
        assert actual_distances == expected_distances

    def test_level_bfs(self):
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

        expected_levels = [
            ["A"],
            ["B", "C", "D"],
            ["E", "F", "G"],
            ["H", "I"],
            ["J"]
        ]

        expected_parent = {
            "A": None,
            "B": "A",
            "C": "A",
            "D": "A",
            "E": "D",
            "F": "D",
            "G": "D",
            "H": "F",
            "I": "F",
            "J": "I"
        }

        actual_levels, actual_parent = bfs.level_bfs("A", graph)
        assert actual_levels == expected_levels
        assert actual_parent == expected_parent
