from src.trie.trie import Trie
import pytest

class TestTrie:
    def test_put_null_key(self):
        trie = Trie()
        with pytest.raises(ValueError):
            trie.put(None, None)

    def test_get_null_key(self):
        trie = Trie()
        with pytest.raises(ValueError):
            trie.get(None)

    def test_put_key(self):
        trie = Trie()
        trie.put("foo", 10)

    def test_get_key_none(self):
        trie = Trie()
        assert trie.get("foo") is None

    def test_get_key(self):
        trie = Trie()
        trie.put("foo", 10)
        assert trie.get("fo") is None
        assert trie.get("foo") == 10

    def test_empty_size(self):
        trie = Trie()
        assert len(trie) == 0

    def test_size_two(self):
        trie = Trie()
        trie.put("foo", 10)
        trie.put("foo", 10)
        trie.put("baz", 12)
        assert len(trie) == 2

    def test_size_two_keys(self):
        trie = Trie()
        trie.put("foo", 10)
        trie.put("foo", 10)
        trie.put("baz", 12)
        expected_keys = set(["foo", "baz"])
        actual_keys = trie.keys()
        assert actual_keys == expected_keys

    def test_delete_leaf_node(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("app", 2)
        trie.put("apex", 3)
        trie.put("banana", 4)
        assert trie.delete("banana")
        assert trie.get("banana") is None
        assert "banana" not in trie.keys()
        assert len(trie) == 3

    def test_delete_prefix_non_value_node(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("app", 2)
        trie.put("apex", 3)
        trie.put("banana", 4)
        assert not trie.delete("ap")
        assert len(trie) == 4

    def test_delete_node_with_children(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("app", 2)
        trie.put("apex", 3)
        trie.put("banana", 4)
        assert len(trie) == 4
        assert trie.delete("app")
        assert trie.get("app") is None
        assert "apple" in trie.keys()
        assert "app" not in trie.keys()
        assert trie.get("apple") == 1
        assert len(trie) == 3

    def test_delete_node_that_is_extension_of_prefix(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("app", 2)
        trie.put("apex", 3)
        trie.put("banana", 4)
        assert trie.delete("apple")
        assert trie.get("apple") is None
        assert "apple" not in trie.keys()
        assert "app" in trie.keys()
        assert trie.get("app") == 2
        assert len(trie) == 3

    def test_delete_non_existent_key(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("app", 2)
        trie.put("apex", 3)
        trie.put("banana", 4)
        assert not trie.delete("orange")
        assert len(trie) == 4

    def test_delete_key_twice(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("app", 2)
        trie.put("apex", 3)
        trie.put("banana", 4)
        assert trie.delete("apex")
        assert not trie.delete("apex")
        assert trie.get("apex") is None
        assert len(trie) == 3

    def test_delete_empty_key(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("app", 2)
        trie.put("apex", 3)
        trie.put("banana", 4)
        with pytest.raises(ValueError):
            trie.delete(None)

    def test_prefix_keys(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("app", 2)
        trie.put("apex", 3)
        trie.put("banana", 4)
        assert trie.prefix_keys("ap") == set(["app", "apple", "apex"])

    def test_exact_key(self):
        trie = Trie()
        trie.put("a", 1)
        trie.put("app", 2)
        trie.put("apple", 3)
        trie.put("applet", 4)
        trie.put("banana", 5)

        result = trie.longest_prefix("apple")
        assert result == "apple"

    def test_longer_word(self):
        trie = Trie()
        trie.put("a", 1)
        trie.put("app", 2)
        trie.put("apple", 3)
        trie.put("applet", 4)
        trie.put("banana", 5)

        result = trie.longest_prefix("applesauce")
        assert result == "apple"
        
        result = trie.longest_prefix("application")
        assert result == "app"

    def test_single_char_match(self):
        trie = Trie()
        trie.put("a", 1)
        trie.put("app", 2)
        trie.put("apple", 3)
        trie.put("applet", 4)
        trie.put("banana", 5)
        result = trie.longest_prefix("amazing")
        assert result == "a"

    def test_no_match(self):
        trie = Trie()
        trie.put("a", 1)
        trie.put("app", 2)
        trie.put("apple", 3)
        trie.put("applet", 4)
        trie.put("banana", 5)
        result = trie.longest_prefix("carrot")
        assert result is None

    def test_prefix_is_key_but_path_not_complete(self):
        trie = Trie()
        trie.put("a", 1)
        trie.put("app", 2)
        trie.put("apple", 3)
        trie.put("applet", 4)
        trie.put("banana", 5)
        result = trie.longest_prefix("appl")
        assert result == "app"  # "appl" is not a full key

    def test_key_starts_with_non_existing_letter(self):
        trie = Trie()
        trie.put("a", 1)
        trie.put("app", 2)
        trie.put("apple", 3)
        trie.put("applet", 4)
        trie.put("banana", 5)
        result = trie.longest_prefix("zebra")
        assert result is None

    def test_empty_input(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("app", 2)
        trie.put("apex", 3)
        trie.put("banana", 4)
        with pytest.raises(ValueError):
            trie.longest_prefix(None)

    def test_get_keys_matching_wildcard_none_expression(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("applet", 2)
        trie.put("banana", 3)
        trie.put("bat", 4)
        with pytest.raises(ValueError):
            trie.get_keys_matching_wildcard(None)

    def test_get_keys_matching_wildcard_exact_match(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("applet", 2)
        trie.put("banana", 3)
        trie.put("bat", 4)
        result = trie.get_keys_matching_wildcard("apple")
        assert result == {"apple"}

    def test_get_keys_matching_wildcard_wildcard_at_the_end(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("applet", 2)
        trie.put("banana", 3)
        trie.put("bat", 4)
        result = trie.get_keys_matching_wildcard("app*")
        assert result == {"apple", "applet"}

    def test_get_keys_matching_wildcard_wildcard_at_the_beginning(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("applet", 2)
        trie.put("banana", 3)
        trie.put("bat", 4)
        result = trie.get_keys_matching_wildcard("*let")
        assert result == {"applet"}

    def test_get_keys_matching_wildcard_wildcard_in_the_middle(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("applet", 2)
        trie.put("banana", 3)
        trie.put("bat", 4)
        result = trie.get_keys_matching_wildcard("a*le")
        assert result == {"apple"}

    def test_get_keys_matching_wildcard_wildcard_that_matches_no_letters(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("applet", 2)
        trie.put("banana", 3)
        trie.put("bat", 4)
        result = trie.get_keys_matching_wildcard("z*")
        assert result == set()

    def test_get_keys_matching_wildcard_wildcard_matching_multiple_letters(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("applet", 2)
        trie.put("banana", 3)
        trie.put("bat", 4)
        result = trie.get_keys_matching_wildcard("b*t")
        assert result == {"bat"}

    def test_get_keys_matching_wildcard_wildcard_matching_with_multiple_segments(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("applet", 2)
        trie.put("banana", 3)
        trie.put("bat", 4)
        result = trie.get_keys_matching_wildcard("b*n*n*")
        assert result == {"banana"}

    def test_get_keys_matching_wildcard_wildcard_matching_empty_prefix(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("applet", 2)
        trie.put("banana", 3)
        trie.put("bat", 4)
        result = trie.get_keys_matching_wildcard("*")
        assert result == {"apple", "applet", "banana", "bat"}

    def test_get_keys_matching_wildcard_wildcard_in_the_middle_and_at_the_end(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("applet", 2)
        trie.put("banana", 3)
        trie.put("bat", 4)
        result = trie.get_keys_matching_wildcard("a*e*")
        assert result == {"apple", "applet"}

    def test_get_keys_matching_wildcard_non_matching_wildcard_at_the_beginning(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("applet", 2)
        trie.put("banana", 3)
        trie.put("bat", 4)
        result = trie.get_keys_matching_wildcard("z*e")
        assert result == set()

    def test_get_keys_matching_wildcard_wildcard_skip_and_continue(self):
        trie = Trie()
        trie.put("apple", 1)
        trie.put("applet", 2)
        trie.put("banana", 3)
        trie.put("bat", 4)
        result = trie.get_keys_matching_wildcard("a*p*le")
        assert result == {"apple"}