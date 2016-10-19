import xml.etree.ElementTree as ET
from nodes.NodeObj import NodeObj



def getNodesList(location):
    result = []
    tree = ET.parse(location)
    root = tree.getroot()
    nodes = root.findall("./nodes/*")
    for child in nodes:
        nodeObject = mapToNodeObject(child)
        result.append(nodeObject)
    return result



def mapToNodeObject(xmlNode):
    name = getName(xmlNode)
    states = getStatesList(xmlNode)
    probabilities = getProbabilitiesList(xmlNode)
    parents = getParents(xmlNode)
    #print (name, states, probabilities, parents)
    return NodeObj(name, states, parents, probabilities)

def getStatesList(node):
    states = (node.findall('state'))
    result =[]
    for state in states:
        result.append(state.attrib['id'])
    return result

def getProbabilitiesList(node):
    probabilities = node.findall('probabilities')
    if (len(probabilities) > 0):
        return probabilities[0].text.split(" ")
    else:
       return []

def getName(node):
    return node.attrib['id']

def getParents(node):
    parents = node.findall('parents')
    if(len(parents) > 0):
        return parents[0].text.split(" ")
    else:
        return []

