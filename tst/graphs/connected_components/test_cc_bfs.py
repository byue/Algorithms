from src.graphs.connected_components.cc_bfs import connected_components
import networkx as nx

class TestConnectedComponents:
    def test_connected_components(self):
        graph = nx.Graph()
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "G")
        graph.add_edge("B", "I")
        graph.add_edge("I", "J")
        graph.add_edge("K", "L")

        expected_components = [
            ["A", "B", "C", "G", "I", "J"],
            ["K", "L"]
        ]

        actual_components = connected_components(graph)
        assert actual_components == expected_components
