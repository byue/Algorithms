from src.graphs.dfs import dfs_iterative, dfs_recursive
from src.graphs.node import Node

class TestDFS:
    def test_dfs_iterative(self):
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

        actual_parent = dfs_iterative(graph)
        assert actual_parent == expected_parent

    def test_dfs_recursive(self):
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

        actual_parent = dfs_recursive(graph)
        assert actual_parent == expected_parent
