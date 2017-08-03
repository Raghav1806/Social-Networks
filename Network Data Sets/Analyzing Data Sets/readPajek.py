import networkx as nx
import matplotlib.pyplot as plt

def plot_deg_dist(G):
	all_degrees 	= nx.degree(G).values()		# all the degrees
	unique_degrees 	= list(set(all_degrees))	# all unique degrees

	count_of_degrees = []	

	for i in unique_degrees:
		x = all_degrees.count(i)
		count_of_degrees.append(x)

	plt.plot(unique_degrees, count_of_degrees)
	plt.show() 	

G = nx.read_pajek('football.net')

print nx.info(G)
print 'Density is ', nx.density(G)
print 'Diameter is ', nx.diameter(G)
plot_deg_dist(G)
