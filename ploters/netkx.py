
#!/usr/bin/env python
"""
Create an G{n,m} random graph and compute the eigenvalues.
Requires numpy and matplotlib.
"""
import networkx as nx
import numpy.linalg
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph

n = 100 # 1000 nodes
m = 20 # 5000 edges
G = nx.gnm_random_graph(n, m)

L = nx.normalized_laplacian_matrix(G)
e = numpy.linalg.eigvals(L.A)
print("Largest eigenvalue:", max(e))
print("Smallest eigenvalue:", min(e))
A = to_agraph(G)
A.layout() # layout with default (neato)
A.draw('simple.png')
plt.show()