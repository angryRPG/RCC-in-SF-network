import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

def rc(G0):
    G = G0.copy()
    z = len(G.nodes)
    d = int(z*1/500)
    B = nx.betweenness_centrality(G)
    B_sorted = dict(sorted(B.items(), key=lambda x: x[1]))
    B_keys = list(B_sorted.keys())
    B_values = list(B_sorted.values())
    G_b = G.copy()
    n = 0
    v = np.empty(shape=[1, 0])
    for i in np.arange(z - d):
        if B_values[i] == 0:
            G_b.remove_node(B_keys[i])
            n += 1
        else:
            G_b.remove_node(B_keys[i])
            m = nx.density(G_b)  # 记录边数
            v = np.append(v, m)
    # 拟合直线
    a_, b_ = B_values[n:(len(v) + n)], v
    return a_, b_

G1 = nx.random_graphs.barabasi_albert_graph(5000, 2,seed=1)

G2 = nx.random_graphs.barabasi_albert_graph(5000, 4,seed=1)

G3 = nx.random_graphs.barabasi_albert_graph(5000, 6,seed=1)

b1,y1 = rc(G1)
b2,y2 = rc(G2)
b3,y3 = rc(G3)
plt.scatter(b1,y1,color='w',label='BA(5000, 2)',marker='o',edgecolor='red')
plt.scatter(b2,y2,color='w',label='BA(5000, 4)',marker='s',edgecolor='darkorange')
plt.scatter(b3,y3,color='w',label='BA(5000, 6)',marker='^',edgecolor='deepskyblue')

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(loc='best',fontsize=15)
plt.title('BA Network(${n}$,${m}$)',fontsize=20)
plt.xlabel('${b}$',fontsize=20)
plt.ylabel('${\phi(b)}$',fontsize=20)

plt.show()