from src.graphs.bfs import bfs
from src.graphs.unweighted_shortest_path import unweighted_shorted_path
from src.graphs.node import Node

class TestUnweightedShortestPath:
    def test_unweighted_shortest_path_no_parent_for_destination(self):
        graph = Node("A")

        actual_parent = bfs(graph)

        actual_path = unweighted_shorted_path(actual_parent, Node("D"), Node("A"))

        assert actual_path is None

    def test_unweighted_shortest_path_no_path(self):
        graph = Node("A", [
                    Node("B"),
                    Node("C"),
                    Node("D", [
                        Node("E"),
                        Node("F", [
                            Node("H"),
                            Node("I", [
                                Node("J")
                            ])
                        ]),
                        Node("G")
                    ]), 
                ])

        expected_path = [
            Node("D"),
            Node("F"),
            Node("I")
        ]

        actual_parent = bfs(graph)

        actual_path = unweighted_shorted_path(actual_parent, Node("Z"), Node("I"))

        assert actual_path is None

    def test_unweighted_shortest_path_middle(self):
        graph = Node("A", [
                    Node("B"),
                    Node("C"),
                    Node("D", [
                        Node("E"),
                        Node("F", [
                            Node("H"),
                            Node("I", [
                                Node("J")
                            ])
                        ]),
                        Node("G")
                    ]), 
                ])

        expected_path = [
            Node("D"),
            Node("F"),
            Node("I")
        ]

        actual_parent = bfs(graph)

        actual_path = unweighted_shorted_path(actual_parent, Node("D"), Node("I"))

        assert actual_path == expected_path
