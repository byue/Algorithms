from src.graphs.connected_components import connected_components
from src.graphs.node import Node
import string

class TestConnectedComponents:
    def test_connected_components(self):
        nodes = {letter: Node(letter) for letter in string.ascii_uppercase}
        nodes["A"].children = [nodes["B"], nodes["C"]]
        nodes["B"].children = [nodes["G"], nodes["I"]]
        nodes["I"].children = [nodes["J"]]
        nodes["K"].children = [nodes["L"]]
        expected_components = [
            [Node("A"), Node("B"), Node("C"), Node("G"), Node("I"), Node("J")],
            [Node("D")],
            [Node("E")],
            [Node("F")],
            [Node("H")],
            [Node("K"), Node("L")],
            [Node("M")],
            [Node("N")],
            [Node("O")],
            [Node("P")],
            [Node("Q")],
            [Node("R")],
            [Node("S")],
            [Node("T")],
            [Node("U")],
            [Node("V")],
            [Node("W")],
            [Node("X")],
            [Node("Y")],
            [Node("Z")]
        ]
        actual_components = connected_components(nodes.values())
        assert actual_components == expected_components
