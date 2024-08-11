from src.graphs.topo import kahn_topo_sort
import networkx as nx

class TestTopo:
    def test_kahn_topo_sort_cycles(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "A")

        actual_cycles = kahn_topo_sort(graph)

        assert actual_cycles == None

    def test_kahn_topo_no_cycles(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B")
        graph.add_edge("B", "E")
        graph.add_edge("A", "D")
        graph.add_edge("D", "G")
        graph.add_edge("A", "F")

        expected_cycles = ["A", "B", "D", "F", "E", "G"]

        actual_cycles = kahn_topo_sort(graph)

        assert actual_cycles == expected_cycles
