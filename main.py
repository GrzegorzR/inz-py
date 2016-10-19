import parser.parser as prs
import nodes.NodesManagerFactory as fact
import json



if __name__ == "__main__":
    nodes = prs.getNodesList('./xdsl_data/Credit.xdsl')
    nodesManager = fact.getPygraphManager()
    nodesManager.setNodes(nodes)
    nodesManager.createGraph()
    print (nodesManager.toJson())
    #nodesManager.plot()
