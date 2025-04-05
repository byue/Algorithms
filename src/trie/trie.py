from collections import deque

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.assigned_value = False

class Trie:
    def __init__(self):
        self.root = Node()
        self.size = 0

    def put(self, key, value):
        if not key:
            raise ValueError()
        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        if not node.assigned_value:
            self.size += 1
        node.value = value
        node.assigned_value = True

    def _find_node(self, key):
        if not key:
            raise ValueError()
        node = self.root
        for c in key:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def get(self, key):
        node = self._find_node(key)
        return None if not node or not node.assigned_value else node.value
    
    def __len__(self):
        return self.size

    def _get_keys(self, prefix, node):
        keys = set()
        stack = deque([(prefix, node)])
        while stack:
            prefix, node = stack.pop()
            if node.assigned_value:
                keys.add(prefix)
            for c, child in node.children.items():
                stack.append((prefix + c, child))
        return keys

    def keys(self):
        return self._get_keys('', self.root)

    def delete(self, key):
        if not key:
            raise ValueError()
        node = self.root
        stack = deque()
        for c in key:
            if c not in node.children:
                return False
            stack.append((node, c))
            node = node.children[c]
        if not node.assigned_value:
            return False
        node.assigned_value = False
        node.value = None
        self.size -= 1
        while stack:
            node, c = stack.pop()
            child = node.children[c]
            if child.assigned_value or len(child.children) > 0:
                return True
            del node.children[c]
        return True

    def prefix_keys(self, prefix):
        node = self._find_node(prefix)
        return self._get_keys(prefix, node)

    def get_keys_matching_wildcard(self, expression):
        if not expression:
            raise ValueError()
        result = set()
        stack = [(self.root, '', 0)]
        while stack:
            node, prefix, expression_index = stack.pop()
            if expression_index == len(expression):
                if node.assigned_value:
                    result.add(prefix)
                continue
            c = expression[expression_index]
            if c == '*':
                # skip wildcard (wildcard matches no characters)
                stack.append((node, prefix, expression_index + 1))
                for child_c, child_node in node.children.items():
                    # child satisfies wildcard and progresses past wildcard (wildcard matches 1 character)
                    stack.append((child_node, prefix + child_c, expression_index + 1))
                    # child satisfies wildcard and does not progress past wildcard (wildcard matches multiple characters)
                    stack.append((child_node, prefix + child_c, expression_index))
            elif c in node.children:
                # normal character match
                stack.append((node.children[c], prefix + c, expression_index + 1))
        return result

    def longest_prefix(self, key):
        if not key:
            raise ValueError()
        node = self.root
        longest = None
        current_prefix = ""
        for c in key:
            if c not in node.children:
                break
            node = node.children[c]
            current_prefix += c
            if node.assigned_value:
                longest = current_prefix
        return longest if longest else None