import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gexf('EuroSiS_Generale_Pays.gexf')

print nx.info(G)
print nx.is_directed(G)


