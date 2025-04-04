from src.graphs.min_cut_max_flow.bipartite_matching import bipartite_matching
import networkx as nx

class TestBipartiteMatching:
    def test_bipartite_matching_no_matches(self):
        graph = nx.Graph()
        graph.add_edge("A", "1")
        graph.add_edge("B", "1")
        graph.add_edge("C", "2")
        U = ["A", "B", "C"]
        V = ["1", "2"]

        actual_matches = bipartite_matching(U, V, graph)

        assert actual_matches is None

    def test_bipartite_matching_matches_2(self):
        graph = nx.Graph()
        graph.add_edge("A", "1")
        graph.add_edge("B", "1")
        graph.add_edge("B", "3")
        graph.add_edge("C", "2")
        graph.add_edge("D", "3")
        graph.add_edge("D", "4")
        graph.add_edge("D", "5")
        graph.add_edge("E", "4")

        U = ["A", "B", "C", "D", "E"]
        V = ["1", "2", "3", "4", "5"]

        actual_matches = bipartite_matching(U, V, graph)
        expected_matches = {'A': '1', 'B': '3', 'C': '2', 'D': '5', 'E': '4'}
        assert actual_matches == expected_matches