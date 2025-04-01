import src.graphs.all_pairs_shortest_paths.floyd_warshall.floyd_warshall as floyd_warshall
import networkx as nx

class TestDjikstra:
    def test_get_apsp_negative_cycle(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B", weight=-5)
        graph.add_edge("B", "A", weight=-5)

        actual_result = floyd_warshall.get_apsp(graph)

        assert actual_result is None

    def test_get_apsp_acyclic(self):
        graph = nx.DiGraph()
        graph.add_edge("A", "B", weight=-2)
        graph.add_edge("C", "A", weight=4)
        graph.add_edge("B", "C", weight=-1)
        graph.add_edge("C", "X", weight=2)
        graph.add_edge("C", "Y", weight=-3)
        graph.add_edge("Z", "X", weight=1)
        graph.add_edge("Z", "Y", weight=-4)

        expected_result = {'A': ({'A': 0, 'B': -2, 'C': -3, 'X': -1, 'Y': -6, 'Z': float('inf')},
                                 {'A': None, 'B': 'A', 'C': 'B', 'X': 'C', 'Y': 'C'}),
                           'B': ({'A': 3, 'B': 0, 'C': -1, 'X': 1, 'Y': -4, 'Z': float('inf')},
                                 {'B': None, 'C': 'B', 'A': 'C', 'X': 'C', 'Y': 'C'}),
                           'C': ({'A': 4, 'B': 2, 'C': 0, 'X': 2, 'Y': -3, 'Z': float('inf')},
                                 {'C': None, 'A': 'C', 'X': 'C', 'Y': 'C', 'B': 'A'}),
                           'X': ({'A': float('inf'),'B': float('inf'), 'C': float('inf'), 'X': 0, 'Y': float('inf'), 'Z': float('inf')},
                                 {'X': None}),
                           'Y': ({'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'X': float('inf'), 'Y': 0, 'Z': float('inf')},
                                 {'Y': None}),
                           'Z': ({'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'X': 1, 'Y': -4, 'Z': 0},
                                 {'Z': None, 'X': 'Z', 'Y': 'Z'})}

        actual_result = floyd_warshall.get_apsp(graph)

        assert actual_result == expected_result
