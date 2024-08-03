import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def rc_avg(k,r):# RCC with the same degree value takes the mean
    a = b = c = np.empty(shape=[1, 0])
    for i in np.arange(len(k)-1):
        if k[i] == k[i+1]:
            c = np.append(c,r[i])
        else:
            c = np.append(c,r[i])
            a = np.append(a,k[i])
            b = np.append(b,np.average(c))
            c = np.empty(shape=[1,0])
    return a,b

def rc(G0): # Calculate the RCC value of the network
    G = G0.copy()
    K = nx.degree(G)
    K_sorted = dict(sorted(dict(K).items(), key=lambda x: x[1]))
    K_keys = list(K_sorted.keys())
    K_values = list(K_sorted.values())
    z = len(G.nodes)
    v = np.empty(shape=[1, 0])
    for i in np.arange(z - 2):# Make sure the final network is connected
        G.remove_node(K_keys[i])
        m = nx.density(G)
        v = np.append(v, m)
        x, y = rc_avg(K_values[0:len(v)], v)
    return x,y


G1 = nx.random_graphs.barabasi_albert_graph(2000, 4,seed=1)

G2 = nx.random_graphs.barabasi_albert_graph(5000, 4,seed=1)

G3 = nx.random_graphs.barabasi_albert_graph(10000, 4,seed=1)


k1,y1 = rc(G1)
k2,y2 = rc(G2)
k3,y3 = rc(G3)
plt.loglog(k1,y1,color='w',label='BA(2000, 4)',marker='o',markeredgecolor='red')
plt.loglog(k2,y2,color='w',label='BA(5000, 4)',marker='s',markeredgecolor='darkorange')
plt.loglog(k3,y3,color='w',label='BA(10000, 4)',marker='^',markeredgecolor='deepskyblue')

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(loc='best',fontsize=15)
plt.title('BA Network(${n}$,${m}$)',fontsize=20)
plt.xlabel('${k}$',fontsize=20)
plt.ylabel('${\phi(k)}$',fontsize=20)

plt.show()