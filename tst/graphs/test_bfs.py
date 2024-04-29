from src.graphs.bfs import bfs, level_bfs
from src.graphs.node import Node

class TestBFS:
    def test_bfs(self):
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

        expected_parent = {
            Node("A"): None,
            Node("B"): Node("A"),
            Node("C"): Node("A"),
            Node("D"): Node("A"),
            Node("E"): Node("D"),
            Node("F"): Node("D"),
            Node("G"): Node("D"),
            Node("H"): Node("F"),
            Node("I"): Node("F"),
            Node("J"): Node("I")
        }

        actual_parent = bfs(graph)
        assert actual_parent == expected_parent

    def test_level_bfs(self):
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

        expected_levels = [
            [Node("A")],
            [Node("B"), Node("C"), Node("D")],
            [Node("E"), Node("F"), Node("G")],
            [Node("H"), Node("I")],
            [Node("J")]
        ]

        expected_parent = {
            Node("A"): None,
            Node("B"): Node("A"),
            Node("C"): Node("A"),
            Node("D"): Node("A"),
            Node("E"): Node("D"),
            Node("F"): Node("D"),
            Node("G"): Node("D"),
            Node("H"): Node("F"),
            Node("I"): Node("F"),
            Node("J"): Node("I")
        }

        actual_levels, actual_parent = level_bfs(graph)
        assert actual_levels == expected_levels
        assert actual_parent == expected_parent
