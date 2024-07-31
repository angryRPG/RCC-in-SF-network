import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

#按度分布构建无标度网络,固定尺寸
def sf_network(n,a,b): #节点数n，幂率指数a，平均度b
    k = nx.utils.powerlaw_sequence(n, a)
    K = np.round(k)
    while sum(K) % 2 != 0:
        k = nx.utils.powerlaw_sequence(n, a)
        K = np.round(k)
    K = [int(i) * b for i in K]
    G = nx.configuration_model(K)
    G = nx.Graph(G)  # remove parallel edges
    G.remove_edges_from(nx.selfloop_edges(G))
    return G

#计算网络节点参数
gamma = 2
G = sf_network(5000,gamma,4)
z = len(G.nodes)
d = int(z / (10**(gamma-1)))
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

#拟合直线
a_, b_ = B_values[n:(len(v)+n)],v
c_b = np.polyfit(a_, b_, 1)
y = c_b[0]*np.array(a_)+c_b[1]
print(c_b)

plt.plot(a_,y,'r')
plt.grid(linestyle='--')
plt.scatter(a_,b_,marker='.')
plt.title('Scale-Free Network(${n}$=1000,${γ}$=3)')
plt.xlabel('${b}$',fontsize=16)
plt.ylabel('${ρ_{>b}}$',fontsize=16)
#plt.text(0.0023,0.025,'slope=15.6',size=16)
#plt.ylim(min(b1)-0.05,0.1);plt.show()
plt.show()

'''
print(c_b)
print('min(v):',min(b_))
print('max(v):',max(b_))
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False
#sns.regplot(x='a_',y='b_',color='r')
plt.title('SF网络(10000,2.5)')
plt.scatter(a_,b_)
#plt.text(0.0017,0.02,'slope=25.03',size=18)
plt.xlabel('${b}$',fontsize=16)
plt.ylabel('${ρ_{>b}}$',fontsize=16)
plt.show()
'''