from src.graphs.dfs import dfs_iterative, dfs_recursive, dfs_recursive_topo_sort
from src.graphs.node import Node

class TestDFS:
    def test_dfs_recursive_topo_sort(self):
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

        expected_topo_sorting = [
            Node("A"),
            Node("D"),
            Node("G"),
            Node("F"), 
            Node("I"),
            Node("J"),
            Node("H"),
            Node("E"),
            Node("C"),
            Node("B")
        ]

        actual_topo_sorting = dfs_recursive_topo_sort(graph)
        print(actual_topo_sorting)
        assert actual_topo_sorting == expected_topo_sorting

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
