from src.union_find.union_find import UnionFind

class TestUnionFind:
    def test_find_new_entry(self):
        union_find = UnionFind()
        assert union_find.find(3) == 3

    def test_find_not_connected(self):
        union_find = UnionFind()
        assert union_find.find(3) == 3
        assert union_find.find(5) == 5
        assert not union_find.connected(3, 5)

    def test_find_connected(self):
        union_find = UnionFind()
        assert union_find.find(3) == 3
        assert union_find.find(5) == 5
        union_find.union(3, 5)
        assert union_find.connected(3, 5)
        assert union_find.connected(5, 3)

    def test_find_connected_reverse(self):
        union_find = UnionFind()
        assert union_find.find(3) == 3
        assert union_find.find(5) == 5
        union_find.union(5, 3)
        assert union_find.connected(3, 5)
        assert union_find.connected(5, 3)
    
    def test_union_self(self):
        union_find = UnionFind()
        union_find.union(3, 3)
        assert union_find.connected(3, 3)
    
    def test_union_greater_rank(self):
        union_find = UnionFind()
        union_find.union(3, 5)
        union_find.union(5, 7)
        assert union_find.connected(3, 5)
        assert union_find.connected(5, 3)
        assert union_find.connected(3, 7)
        assert union_find.connected(7, 3)
        assert union_find.connected(5, 7)
        assert union_find.connected(7, 5)

    def test_union_less_rank(self):
        union_find = UnionFind()
        union_find.union(3, 5)
        union_find.union(7, 5)
        assert union_find.connected(3, 5)
        assert union_find.connected(5, 3)
        assert union_find.connected(3, 7)
        assert union_find.connected(7, 3)
        assert union_find.connected(5, 7)
        assert union_find.connected(7, 5)