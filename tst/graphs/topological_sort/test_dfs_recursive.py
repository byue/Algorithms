from src.graphs.topological_sort.dfs_recursive import topo_sort
import networkx as nx
from collections import deque

class TestTopoDfs:

    def test_dfs_topo_sort(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "E")
        graph.add_edge("B", "E")
        graph.add_edge("E", "F")
        graph.add_edge("B", "F")
        graph.add_edge("B", "C")
        graph.add_edge("F", "C")
        graph.add_edge("F", "G")
        graph.add_edge("G", "H")
        graph.add_edge("H", "C")
        graph.add_edge("H", "D")
        graph.add_edge("D", "C")

        expected_topo_sorting = deque(['A', 'B', 'E', 'F', 'G', 'H', 'D', 'C'])
        actual_topo_sorting = topo_sort(graph)
        assert actual_topo_sorting == expected_topo_sorting

    def test_dfs_topo_sort_cycle(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "A")

        expected_topo_sorting = deque()

        actual_topo_sorting = topo_sort(graph)
        assert actual_topo_sorting == expected_topo_sorting