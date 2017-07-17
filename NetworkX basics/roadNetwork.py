# modelling a road network

import networkx as nx
import matplotlib as plt
import random
G = nx.Graph()	# undirected graph

# for directed graphs, use: G = nx.DiGraph()

city_set = ['Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Surat', 'Pune', 'Jaipur']

for each in city_set:
	G.add_node(each)

nx.draw(G)
plt.show()

costs = []
value = 100
while (value <= 2000):
	costs.append(value)
	value += 100
print costs

# we are going to add 16 edges
while(G.number_of_edges() < 16):
	c1 = random.choice(G.nodes())
	c2 = random.choice(G.nodes())
	if(c1 != c2) and G.has_edge(c1, c2) == False:
		w = random.choice(costs)
		G.add_edge(c1, c2, weight = w)

for u in G.nodes():
	for v in G.nodes():
		print u, v, nx.has_path(G, u, v)

pos = nx.circular_layout(G)
nx.draw(G, pos)
nx.draw_networkx_edge_labels(G, pos)
plt.show()

print nx.is_connected(G)

# printing path lengths using networkx


