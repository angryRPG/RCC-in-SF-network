import numpy as np
import os
import  networkx as nx
import matplotlib.pyplot as plt

def rc_avg(k,r):
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

def rc(G0):
    G = G0.copy()
    K = nx.degree(G)
    K_sorted = dict(sorted(dict(K).items(), key=lambda x: x[1]))
    K_keys = list(K_sorted.keys())
    K_values = list(K_sorted.values())
    z = len(G.nodes)
    v = np.empty(shape=[1, 0])
    for i in np.arange(z - 3):
        G.remove_node(K_keys[i])
        m = nx.density(G)
        v = np.append(v, m)
        x, y = rc_avg(K_values[0:len(v)], v)
    return x,y


os.chdir('E:\data\Adja')
A = np.loadtxt('newyork_adja.txt')
G = nx.Graph()
G.add_nodes_from(np.arange(len(A)))

for i in np.arange(len(A)):
    for j in np.arange(i, len(A)):
        if A[i, j] > 0:
            G.add_edge(i, j)

k,y = rc(G)

a_K, b_K = np.log10(k), np.log10(y)
c_K = np.polyfit(a_K, b_K, 1)
x1 = np.array(k)
y1 = (10**c_K[1])*(x1**c_K[0])


plt.loglog(k,y,color='w',label='New York',marker='o',markeredgecolor='deepskyblue')
plt.plot(x1,y1,'r')
plt.title('Metro(New York)',fontsize=20)
plt.xlabel('${k}$',fontsize=18)
plt.ylabel('${\phi(k)}$',fontsize=18)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()
