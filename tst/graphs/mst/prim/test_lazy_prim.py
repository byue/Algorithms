from src.graphs.mst.prim.lazy_prim import get_mst
import networkx as nx

class TestLazyPrim:
    def test_lazy_prim(self):
        graph = nx.Graph()
        graph.add_edge(0, 7, weight=0.16)
        graph.add_edge(2, 3, weight=0.17)
        graph.add_edge(1, 7, weight=0.19)
        graph.add_edge(0, 2, weight=0.26)
        graph.add_edge(5, 7, weight=0.28)
        graph.add_edge(1, 3, weight=0.29)
        graph.add_edge(1, 5, weight=0.32)
        graph.add_edge(2, 7, weight=0.34)
        graph.add_edge(4, 5, weight=0.35)
        graph.add_edge(1, 2, weight=0.36)
        graph.add_edge(4, 7, weight=0.37)
        graph.add_edge(0, 4, weight=0.38)
        graph.add_edge(6, 2, weight=0.40)
        graph.add_edge(3, 6, weight=0.52)
        graph.add_edge(6, 0, weight=0.58)
        graph.add_edge(6, 4, weight=0.93)

        expected_mst = nx.Graph()
        expected_mst.add_edge(0, 7, weight=0.16)
        expected_mst.add_edge(2, 3, weight=0.17)
        expected_mst.add_edge(1, 7, weight=0.19)
        expected_mst.add_edge(0, 2, weight=0.26)
        expected_mst.add_edge(5, 7, weight=0.28)
        expected_mst.add_edge(4, 5, weight=0.35)
        expected_mst.add_edge(6, 2, weight=0.40)

        total_cost, mst = get_mst(graph)

        assert total_cost == 1.81
        assert mst.graph == expected_mst.graph