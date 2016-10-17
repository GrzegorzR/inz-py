import networkx as nx
import numpy.linalg
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
from networkx.readwrite import json_graph
import json



from json import JSONEncoder
class MyEncoder(JSONEncoder):
    def default(self, o):
        return str(o)


class NodesManager:

    def __init__(self, plotModule):
        self.plotModule = plotModule
        self.nodes = []
        self.graph = None

    def addNode(self, node):
        self.nodes.append(node)

    def setNodes(self, nodes):
        self.nodes = nodes

    def toJson(self):
        data = json_graph.node_link_data(self.graph)
        result = json_graph.node_link_graph(data)
        #data['nodes'] = dict(data['nodes'])

        s = json.dumps(data, cls=MyEncoder)
        return  s


    def createGraph(self):

        G = nx.DiGraph()
        self.graph = G
        self.addGraphNodes()
        self.addGraphEdges()


        G.add_edge(self.nodes[0], self.nodes[1])
        nx.draw(G)
        #nx.draw_graphviz(G)
        plt.show()

    def addGraphNodes(self):
        for node in self.nodes:
            self.graph.add_node(node)

    def addGraphEdges(self):
        nodesDir =  {self.nodes[i].name: self.nodes[i] for i in range(0, len(self.nodes))}
        for node in self.nodes:
            if( len(node.parents) > 0 ):
                for parent in node.parents:
                    self.graph.add_edge(nodesDir[parent], node)

    def plot(self):
        self.plotModule.plot(self.graph)
    def printf(self):
        print(self.nodes[1])




