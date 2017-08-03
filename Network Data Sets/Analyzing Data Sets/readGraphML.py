import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_graphml('vecwiki-20091230-manual-coding.graphml')

print nx.info(G)

print nx.number_of_nodes(G)
print nx.number_of_edges(G)

print nx.is_directed(G)

nx.draw(G)
plt.show()
