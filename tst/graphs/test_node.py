from src.graphs.node import Node

class TestNode:
    def test_create_node_only_value(self):
        node = Node(3)
        assert node.value == 3

    def test_repr(self):
        node = Node(3)
        assert repr(node) == "3"

    def test_create_node_with_children(self):
        node = Node(3, [])
        assert node.value == 3
        assert node.children == []

    def test_equal_nodes(self):
        node_1 = Node(3)
        node_2 = Node(3)
        assert node_1.value == node_2.value
        assert node_1 == node_2
        assert node_2 == node_1
        assert hash(node_1) == hash(node_2)

    def test_non_equal_value_nodes(self):
        node_1 = Node(3)
        node_2 = Node(4)
        assert node_1.value != node_2.value
        assert node_1 != node_2
        assert node_2 != node_1
        assert hash(node_1) != hash(node_2)

    def test_non_equal_type_nodes(self):
        node_1 = Node(3)
        node_2 = "foo"
        assert node_1 != node_2
        assert node_2 != node_1
        assert hash(node_1) != hash(node_2)

    def test_append_child(self):
        node_1 = Node(3)
        node_2 = Node(4)
        node_1.append(node_2)
        assert len(node_1.children) == 1
        assert node_1.children[0] == node_2
