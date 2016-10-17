
class NodeObj:
    def __init__(self, name, states, parents, probabilities):
        self.name = name
        self.states = states
        self.parents = parents
        self.probabilities = probabilities
    def __str__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, NodeObj) and self.name == other.name

    def __hash__(self):
        return hash(self.name)
