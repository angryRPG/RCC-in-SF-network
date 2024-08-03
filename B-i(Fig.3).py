import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns
import os

def betweenness(G):
    B = nx.betweenness_centrality(G)
    B_sorted = dict(sorted(B.items(), key=lambda x: x[1]))
    B_values = list(B_sorted.values())
    return B_values

G1 = nx.random_graphs.barabasi_albert_graph(3000,4,seed=1)
x1 = np.arange(len(G1.nodes))
y1 = betweenness(G1)

G2 = nx.random_graphs.barabasi_albert_graph(4000,4,seed=1)
x2 = np.arange(len(G2.nodes))
y2 = betweenness(G2)

G3 = nx.random_graphs.barabasi_albert_graph(5000,4,seed=1)
x3 = np.arange(len(G3.nodes))
y3 = betweenness(G3)

plt.scatter(x3,y3,color='w',label='BA(5000, 4)',marker='^',edgecolor='deepskyblue')
plt.scatter(x2,y2,color='w',label='BA(4000, 4)',marker='s',edgecolor='darkorange')
plt.scatter(x1,y1,color='w',label='BA(3000, 4)',marker='o',edgecolor='red')

plt.grid(linestyle='--')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(loc='best',fontsize=15)
plt.title('BA Network(${n}$,${m}$=4)',fontsize=15)
plt.xlabel('${i}$',fontsize=20)
plt.ylabel('${Betweenness}$',fontsize=15)
plt.show()