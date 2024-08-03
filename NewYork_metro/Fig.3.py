import numpy as np
import os
import  networkx as nx
from scipy.optimize import curve_fit
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

def fund(x,a):
    return a/(z-1-x)

os.chdir('E:\data\Adja')
A = np.loadtxt('newyork_adja.txt')
G = nx.Graph()
G.add_nodes_from(np.arange(len(A)))

for i in np.arange(len(A)):
    for j in np.arange(i, len(A)):
        if A[i, j] > 0:
            G.add_edge(i, j)


B = nx.betweenness_centrality(G)
B_sorted = dict(sorted(B.items(), key=lambda x: x[1]))
B_keys = list(B_sorted.keys())
B_values = list(B_sorted.values())
z = len(G.nodes)
G_b = G.copy()
v = np.empty(shape=[1, 0])
n = 0
for i in np.arange(z - 3):
    G_b.remove_node(B_keys[i])
    m = nx.density(G_b)
    v = np.append(v, m)
x = np.arange(len(v))

popt, pcov=curve_fit(fund, x, v)
a = popt[0]
y = a/(z-1-x)

fig = plt.figure()
plt.scatter(x,v,color='w',label='New York',marker='o',edgecolor='deepskyblue')
plt.title('Metro(New York)',fontsize=20)
plt.plot(x,y,'r',label='${f(i)=1.76/(595-i)}$')
plt.legend(loc='best',fontsize=15)
plt.xlabel('${i}$',fontsize=18)
plt.ylabel('${\phi(i)}$',fontsize=18)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.grid(linestyle='--')

left,bottom,width,height=0.30,0.35,0.35,0.35
fig.add_axes([left,bottom,width,height])
plt.plot(x,y,'r')
plt.scatter(x,v,color='w',label='$New York$',marker='o',edgecolor='deepskyblue')
plt.ylim(0,0.4)
plt.xlim(500,600)
plt.xlabel('${i}$',fontsize=18)
plt.ylabel('${\phi(i)}$',fontsize=18)
plt.show()