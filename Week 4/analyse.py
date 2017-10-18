import networkx as nx
import matplotlib.pyplot as plt

def plot_density():
	x = []
	y = []
	for i in range (0, 11):
		G = nx.read_gml('evolution_' + str(i) + '.gml')
		x.append(i)
		y.append(nx.density(G))
	plt.xlabel('Time')
	plt.ylabel('Density')
	plt.title('Change in Density')
	plt.plot(x, y)	
	plt.show()
	
def obesity(G):
	num = 0
	for each in G.nodes():
		if G.node[each]['name'] == 40:
			num = num + 1
	return num
	
def lean(G):
	num = 0
	for each in G.nodes():
		if G.node[each]['name'] == 15:
			num = num + 1
	return num	
				

def plot_obesity():
	x = []
	y = []
	for i in range (0, 11):
		G = nx.read_gml('evolution_' + str(i) + '.gml')
		x.append(i)
		y.append(obesity(G))
	plt.xlabel('Time')
	plt.ylabel('Obesity')
	plt.title('Change in Obesity')
	plt.plot(x, y)	
	plt.show()
	
def plot_lean():
	x = []
	y = []
	for i in range (0, 11):
		G = nx.read_gml('evolution_' + str(i) + '.gml')
		x.append(i)
		y.append(lean(G))
	plt.xlabel('Time')
	plt.ylabel('Lean')
	plt.title('Change in Lean people')
	plt.plot(x, y)	
	plt.show()
		
plot_density()
plot_obesity()
plot_lean()
