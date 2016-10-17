
#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division


from pygraphviz import *
from networkx.drawing.nx_agraph import to_agraph


class PygraphvitzPlotter:

    def plot (self, G):
        A = to_agraph(G)
        A.node_attr['style'] = 'filled'
        A.node_attr['fillcolor'] = '#000033'
        A.node_attr['shape'] = 'circle'
        #A.node_attr['fixedsize'] = 'true'
        A.node_attr['fontcolor'] = '#FFFFFF'
        A.draw('chart.png', prog= 'fdp')
