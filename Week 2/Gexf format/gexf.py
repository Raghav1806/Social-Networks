import networkx as nx
import matplotlib.pyplot as plt

def plot_deg_dist(G):
	all_degrees = nx.degree(G).values()
	unique_degrees = list(set(all_degrees))
	
	count_of_degrees = []
	
	for i in unique_degrees:
		x = all_degrees.count(i)
		count_of_degrees.append(x)
		
	plt.plot(unique_degrees, count_of_degrees, 'yo-')
	plt.xlabel('Degrees')
	plt.ylabel('Number of nodes')
	plt.title('Degree distribution of a network')
	plt.show()	

G = nx.read_gexf('yeast.gexf')

print nx.info(G)

nx.draw(G)
plt.show()

plot_deg_dist(G)
