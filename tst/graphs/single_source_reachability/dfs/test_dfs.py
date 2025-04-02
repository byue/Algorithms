from src.graphs.single_source_reachability.dfs.dfs import dfs_iterative, dfs_recursive
import networkx as nx

class TestDFS:
    def test_dfs_iterative(self):
        graph = nx.Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("A", "D")
        graph.add_edge("D", "E")
        graph.add_edge("D", "F")
        graph.add_edge("F", "H")
        graph.add_edge("F", "I")
        graph.add_edge("F", "I")
        graph.add_edge("I", "J")
        graph.add_edge("D", "G")
        
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

        actual_parent = dfs_iterative("A", graph)
        assert actual_parent == expected_parent

    def test_dfs_recursive(self):
        graph = nx.Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("A", "D")
        graph.add_edge("D", "E")
        graph.add_edge("D", "F")
        graph.add_edge("F", "H")
        graph.add_edge("F", "I")
        graph.add_edge("F", "I")
        graph.add_edge("I", "J")
        graph.add_edge("D", "G")

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

        actual_parent = dfs_recursive("A", graph)
        assert actual_parent == expected_parent
