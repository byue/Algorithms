from src.graphs.min_cut_max_flow.ford_fulkerson import ford_fulkerson
import networkx as nx

class TestFordFulkerson:
    def test_ford_fulkerson(self):
        graph = nx.DiGraph()
        graph.add_edge("source", "A", weight=10)
        graph.add_edge("source", "B", weight=5)
        graph.add_edge("source", "C", weight=15)
        graph.add_edge("A", "B", weight=4)
        graph.add_edge("A", "D", weight=9)
        graph.add_edge("A", "E", weight=15)
        graph.add_edge("B", "C", weight=4)
        graph.add_edge("B", "E", weight=8)
        graph.add_edge("C", "F", weight=16)
        graph.add_edge("D", "E", weight=15)
        graph.add_edge("D", "sink", weight=10)
        graph.add_edge("E", "F", weight=15)
        graph.add_edge("E", "sink", weight=10)
        graph.add_edge("F", "B", weight=6)
        graph.add_edge("F", "sink", weight=10)
        
        expected_max_flow = 28

        expected_flows = {
            ("source", "A"): 10,
            ("source", "B"): 5,
            ("source", "C"): 13,
            ("A", "B"): 0,
            ("A", "D"): 9,
            ("A", "E"): 1,
            ("B", "C"): 0,
            ("B", "E"): 8,
            ("C", "F"): 13,
            ("D", "E"): 0,
            ("D", "sink"): 9,
            ("E", "sink"): 9,
            ("E", "F"): 0,
            ("F", "B"): 3,
            ("F", "sink"): 10,
        }

        expected_source_nodes = set(['source', 'B', 'C', 'F'])
        expected_sink_nodes = set(['A', 'D', 'E', 'sink'])
        expected_min_cut_edges = set([('B', 'E'), ('F', 'sink'), ('source', 'A')])

        actual_max_flow, actual_flows, actual_min_cut_edges, actual_source_nodes, actual_sink_nodes = ford_fulkerson(graph, "source", "sink")

        assert actual_max_flow == expected_max_flow
        assert actual_flows == expected_flows
        assert actual_min_cut_edges == expected_min_cut_edges
        assert actual_source_nodes == expected_source_nodes
        assert actual_sink_nodes == expected_sink_nodes
