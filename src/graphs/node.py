class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        if type(other) is type(self):
            return self.value == other.value
        return False

    def append(self, child):
        self.children.append(child)
