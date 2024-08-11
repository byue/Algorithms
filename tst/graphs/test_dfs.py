from src.graphs.dfs import dfs_iterative, dfs_recursive, dfs_recursive_topo_sort, dfs_get_all_cycles_undirected
import networkx as nx

class TestDFS:
    def test_dfs_get_all_cycles_undirected(self):
        graph = nx.Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "A")
        graph.add_edge("B", "B")
        graph.add_edge("A", "C")
        graph.add_edge("A", "D")
        graph.add_edge("D", "E")
        graph.add_edge("D", "F")
        graph.add_edge("F", "H")
        graph.add_edge("F", "I")
        graph.add_edge("F", "L")
        graph.add_edge("I", "A")
        graph.add_edge("I", "L")
        graph.add_edge("G", "J")
        graph.add_edge("G", "K")
        graph.add_edge("K", "G")

        expected_cycles = [
            ["A", "B"],
            ["B"],
            ["A"],
            ["A", "C"],
            ["A", "D"], 
            ["D", "E"],
            ["F", "D"],
            ["F", "H"],
            ["I", "F"],
            ["A", "D", "F", "I"],
            ["I", "F", "L"],
            ["I", "L"],
            ["L", "F"],
            ["A", "D", "F", "L", "I"],
            ["A", "I"],
            ["G", "J"],
            ["G", "K"]
        ]

        actual_cycles = dfs_get_all_cycles_undirected(graph)
        assert actual_cycles == expected_cycles

    def test_dfs_recursive_topo_sort(self):
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

        expected_topo_sorting = ["A", "D", "G", "F", "I", "J", "H", "E", "C", "B"]

        actual_topo_sorting = dfs_recursive_topo_sort(graph)
        assert actual_topo_sorting == expected_topo_sorting

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

        actual_parent = dfs_iterative(graph)
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

        actual_parent = dfs_recursive(graph)
        assert actual_parent == expected_parent
