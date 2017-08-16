import networkx as nx
import matplotlib.pyplot as plt
import itertools

def communities_brute(G):
	nodes = G.nodes()
	n = G.number_of_nodes()

	first_community = []
	for i in range (1, n/2 + 1):
		comb = [list(x) for x in itertools.combinations(nodes, i)]
		first_community.extend(comb)

	second_community = []
	for i in range(len(first_community)):
		l = list(set(nodes) - set(first_community[i]))
		second_community.append(l)

	# which division is the best
	num_intra_edges1 = []
	num_intra_edges2 = []
	num_inter_edges = []
	# ratio of number of intra and number of inter community edges
	ratio = []

	for i in range(len(first_community)):

		num_intra_edges1.append(G.subgraph(first_community[i]).number_of_edges())

	for i in range(len(second_community)):

		num_intra_edges2. append(G.subgraph(second_community[i]).number_of_edges())

	e = G.number_of_edges()	

	for i in range (len(first_community)):
	
		num_inter_edges.append(e - num_intra_edges1[i] - num_intra_edges2[i])

	# find the ratio
	for i in range(len(first_community)):
		ratio.append((float)(num_intra_edges1[i] + num_intra_edges2[i])/num_inter_edges[i])

	max_value = max(ratio)
	max_index = ratio.index(max_value)

	print '(', first_community[max_index], '), (', second_community[max_index], ')'

G = nx.barbell_graph(5, 0)
communities_brute(G)
nx.draw(G)
plt.show()
