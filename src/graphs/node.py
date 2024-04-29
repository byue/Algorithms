class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        if type(other) is type(self):
            return self.value == other.value
        return False
    
    def __repr__(self):
        return str(self.value)

    def append(self, child):
        self.children.append(child)
