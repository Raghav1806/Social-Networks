# basic graph using networkx
import networkx as nx
import matplotlib.pyplot as plt

G = networkx.Graph()

G = add_node(1)
G = add_node(2)
G = add_node(3)
G = add_node(4)
G = add_node(5)
G = add_node(6)

G.nodes()

G.add_edge(1, 2)
G.add_edge(1, 4)
G.add_edge(4, 6)
G.add_edge(5, 4)
G.add_edge(2, 3)

G.edges()

nx.draw(G, with_labels = True)
plt.show()

# complete graph using networkx
import networkx as nx
import matplotlib.pyplot as plt

Z = nx.complete_graph(10)
Z.edges()
Z.size()

nx.draw(Z, with_labels = True)
plt.show()

# random graph with a certain probability of occurrence of an edge
import networkx as nx
import matplotlib.pyplot as plt

G = nx.gnp_random_graph(20, 0.5)
nx.draw(G)
plt.show()

