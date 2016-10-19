
class NodeObj:
    def __init__(self, name, states, parents, probabilities):
        self.name = name
        self.states = states
        self.parents = parents
        self.probabilities = probabilities
        self.fixProbs = None
    def __str__(self):
        return self.toJson()

    def __eq__(self, other):
        return isinstance(other, NodeObj) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def toJson(self):
        result = '"name":"{0}"'.format(self.name)
        return result
