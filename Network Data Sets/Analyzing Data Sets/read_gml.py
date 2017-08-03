import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gml('karate.gml')

print nx.info(G)
print nx.is_directed(G)
