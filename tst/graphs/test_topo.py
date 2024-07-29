from src.graphs.topo import kahn_topo_sort
from src.graphs.node import Node

class TestTopo:
    def test_kahn_topo_sort_cycles(self):
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

        expected_cycles = None
        actual_cycles = kahn_topo_sort([graph])
        assert actual_cycles == expected_cycles

    def test_kahn_topo_no_cycles(self):
        graph = Node("A", [
                    Node("B", [
                        Node("E")
                    ]),
                    Node("D", [
                        Node("G")
                    ]),
                    Node("F")
                ])
        expected_cycles = [
            Node("A"),
            Node("B"),
            Node("D"),
            Node("F"),
            Node("E"),
            Node("G")
        ]
        actual_cycles = kahn_topo_sort([graph])
        assert actual_cycles == expected_cycles
