import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

def rc_avg(k,rc):#一一对应
    a = b = c = np.empty(shape=[1, 0])
    for i in np.arange(len(k)-1):
        if k[i] == k[i+1]:
            c = np.append(c,rc[i])
        else:
            c = np.append(c,rc[i])
            a = np.append(a,k[i])
            b = np.append(b,np.average(c))
            c = np.empty(shape=[1,0])
    return a,b

def del0(a, b):#去除B的0值，方便作对数
    a1 = b1 = np.empty(shape=[1,0])
    for i in np.arange(len(b)):
        if b[i] == 0:
            continue
        else:
            a1 = np.append(a1,a[i])
            b1 = np.append(b1,b[i])
    return a1,b1


G = nx.random_graphs.barabasi_albert_graph(5000,4)
K = nx.degree(G)
K_sorted = dict(sorted(dict(K).items(), key=lambda x: x[1]))
K_keys = list(K_sorted.keys())
K_values = list(K_sorted.values())
B = nx.betweenness_centrality(G)
B_values_bk = list(B.values())
B_sorted = dict(sorted(B.items(), key=lambda x: x[1]))
B_keys = list(B_sorted.keys())
B_values = list(B_sorted.values())
z = len(G.nodes)
d = int(z * 1/10)

#slope_B_K
G1 = G.copy()
a_bk1 = a_bk2 = b_bk = np.empty(shape=[1, 0])
for i in np.arange(len(K_keys) - 1):
    if K_values[i] == K_values[i + 1]:
        b_bk = np.append(b_bk, B_values_bk[K_keys[i]])
    else:
        b_bk = np.append(b_bk, B_values_bk[K_keys[i]])
        a_bk1 = np.append(a_bk1, K_values[i])
        a_bk2 = np.append(a_bk2, np.average(b_bk))
        b_bk = np.empty(shape=[1, 0])
K_bk, B_bk = del0(a_bk1, a_bk2)
c = np.polyfit(np.log10(K_bk)[5:len(np.log10(K_bk))], np.log10(B_bk)[5:len(np.log10(K_bk))], 1)

#slope_RC_K
G3 = G.copy()
v_K = np.empty(shape=[1, 0])
for i in np.arange(z - 10):
    G3.remove_node(K_keys[i])
    m_K = nx.density(G3)  # 记录边数
    v_K = np.append(v_K, m_K)
# 双对数坐标下拟合直线
a3, b3 = rc_avg(K_values[0:len(v_K)], v_K)
a_K, b_K = np.log10(a3), np.log10(b3)
c_K = np.polyfit(a_K, b_K, 1)


x1 = np.array(K_bk)
y1 = (10**c[1])*(x1**c[0])

x2 = np.array(a3)
y2 = (10**c_K[1])*(x2**c_K[0])


c3 = np.polyfit(B_bk[0:len(b3)],b3, 1)
y3 = c3[0]*B_bk[0:len(b3)]+c3[1]
'''
#slope_RC_B
G2 = G.copy()
n_B = 0
v_B = np.empty(shape=[1, 0])
for i in np.arange(z - d):
    if B_values[i] == 0:
        G2.remove_node(B_keys[i])
        n_B += 1
    else:
        G2.remove_node(B_keys[i])
        m_B = nx.density(G2)  # 记录边数
        v_B = np.append(v_B, m_B)
a_B, b_B = B_values[n_B:(len(v_B) + n_B)], v_B
c_B = np.polyfit(a_B, b_B, 1)
'''
plt.loglog(a3, b3,color='w',label='${\phi(k)}$,  slope=1.739',marker='s',markeredgecolor='deepskyblue')
plt.loglog(K_bk, B_bk,color='w',label='${b_{k}}$,  slope=1.722',marker='o',markeredgecolor='red')
plt.plot(x1,y1,'k')
plt.plot(x2,y2,'k')
#plt.loglog(k3,v3,color='w',label='(5000, 500)',marker='^',markeredgecolor='b')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(loc='best',fontsize=15)
plt.xlabel('${k}$',fontsize=15)
#plt.ylabel('${ρ_{>k}}$',fontsize=18)
plt.title('BA Network(${n}$=5000,${m}$=4)',fontsize=15)
plt.show()

#画图（\phi(k)---b_{k}）
#plt.scatter(B_bk[0:len(b3)],b3,s=10);plt.text(0.017,0.2,'slope=1.97',size=15);plt.plot(B_bk[0:len(b3)],y3,'r');plt.title('BA Network(${n}$=5000,${m}$=4)',fontsize=15);plt.xlabel('$b_{k}$',fontsize=15);plt.ylabel('${\phi(k)}$',fontsize=15);plt.yticks(fontsize=15);plt.xticks(fontsize=15);plt.show()
