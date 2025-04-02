from src.graphs.strongly_connected_components.koseraju import get_scc
import networkx as nx

class TestKoseraju:
    def test_dfs_topo_sort(self):
        graph = nx.DiGraph()
        graph.add_edge("1", "7")
        graph.add_edge("7", "4")
        graph.add_edge("4", "1")
        graph.add_edge("7", "9")
        graph.add_edge("9", "6")
        graph.add_edge("6", "3")
        graph.add_edge("3", "9")
        graph.add_edge("6", "8")
        graph.add_edge("8", "2")
        graph.add_edge("2", "5")
        graph.add_edge("5", "8")
        expected_result = [['4', '7', '1'], ['3', '6', '9'], ['5', '2', '8']]
        actual_result = get_scc(graph)
        assert expected_result == actual_result
