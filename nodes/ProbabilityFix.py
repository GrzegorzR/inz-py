

def fixProbabilities(nodes):
    #create node name : node object dictionary
    nodesDic = {nodes[i].name: nodes[i] for i in range(0, len(nodes))}
    for node in nodes:
        if len(node.parents )> 0:
            statesProb = []
            statesNum = len(node.states)
            for i in range(0, len(node.probabilities)/len(node.states)):
                ar = []
                for j in range(0, len(node.states)):
                    ar.append(node.probabilities[i*statesNum + j])
                statesProb.append(ar)
            node.fixProbs = statesProb
