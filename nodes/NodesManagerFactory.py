from NodesManager import NodesManager
from ploters.PygraphvitzPlotter import PygraphvitzPlotter




def getPygraphManager():
    return NodesManager(PygraphvitzPlotter())

