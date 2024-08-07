from src.graphs.dfs import dfs_iterative, dfs_recursive, dfs_recursive_topo_sort, dfs_get_cycles
from src.graphs.node import Node

class TestDFS:
    def test_dfs_get_cycles(self):
        graph = Node("A", [
                    Node("B", [
                        Node("B")
                    ]),
                    Node("C"),
                    Node("D", [
                        Node("E"),
                        Node("F", [
                            Node("H"),
                            Node("I", [
                                Node("A")
                            ])
                        ]),
                        Node("G", [
                            Node("J"),
                            Node("K", [
                                Node("G")
                            ]),
                        ])
                    ]),
                ])

        expected_cycles = [
            [Node("B")],
            [Node("A"), Node("I"), Node("F"), Node("D")],
            [Node("G"), Node("K")],
        ]

        actual_cycles = dfs_get_cycles(graph)
        assert actual_cycles == expected_cycles

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
