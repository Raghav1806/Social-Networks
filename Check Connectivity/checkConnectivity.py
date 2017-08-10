import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy

# add 'n' nodes in a graph
def add_nodes(n):
	G = nx.Graph()
	G.add_nodes_from(range(n))
	return G

# add one random edge
def add_random_edge(G):
	v1 = random.choice(G.nodes())
	v2 = random.choice(G.nodes())
	if v1 != v2:
		G.add_edge(v1, v2)
	return G

# keeps adding random edges in G till it becomes connected
def add_till_connectivity(G):
	while(nx.is_connected(G) == False):
		G = add_random_edge(G)
	return G

# takes input as number of nodes and returns number of nodes needed to make a connected graph
def create_instance(n):
	G = add_nodes(n)
	G = add_till_connectivity(G)
	return G.number_of_edges()

# average the graph over 100 instances
def create_avg_instance(n):
	list1 = []
	for i in range(0, 100):		
		list1.append(create_instance(n))
	return numpy.average(list1)

# plot the desired number of edges for connected graph
def plot_connectivity():
	x = []
	y = []
	# 'i' is number of nodes
	i = 10
	while(i <= 400):
		x.append(i)
		y.append(i*numpy.log(i))
		i = i+10
	plt.xlabel('Number of nodes')
	plt.ylabel('Number of edges required to connect the graph')
	plt.title('Emergence of connectivity')
	plt.plot(x, y)
	plt.show()

