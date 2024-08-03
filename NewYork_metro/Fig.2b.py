import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os

def rc(G0):
    G = G0.copy()
    z = len(G.nodes)
    B = nx.betweenness_centrality(G)
    B_sorted = dict(sorted(B.items(), key=lambda x: x[1]))
    B_keys = list(B_sorted.keys())
    B_values = list(B_sorted.values())
    G_b = G.copy()
    n = 0
    v = np.empty(shape=[1, 0])
    for i in np.arange(z - 3):
        if B_values[i] == 0:
            G_b.remove_node(B_keys[i])
            n += 1
        else:
            G_b.remove_node(B_keys[i])
            m = nx.density(G_b)
            v = np.append(v, m)

    x, y = B_values[n:(len(v) + n)], v
    return x, y

os.chdir('E:\data\Adja')
A = np.loadtxt('newyork_adja.txt')
G = nx.Graph()
G.add_nodes_from(np.arange(len(A)))

for i in np.arange(len(A)):
    for j in np.arange(i, len(A)):
        if A[i, j] > 0:
            G.add_edge(i, j)

x,y = rc(G)
c = np.polyfit(x, y, 1)
x1 = np.array(x)
y1 = c[0]*x1 + c[1]

plt.scatter(x,y,color='w',label='metro',marker='o',edgecolor='deepskyblue')
plt.plot(x1,y1,'r')
plt.title('Metro(New York)',fontsize=20)
plt.xlabel('${b}$',fontsize=18)
plt.ylabel('${\phi(b)}$',fontsize=18)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()