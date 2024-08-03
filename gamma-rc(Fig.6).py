import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

#os.chdir('C:\\Users\\LZH\\Desktop\\result')
os.chdir('F:\\Data')
ss = np.loadtxt('SF-γ-θ(5000,4).txt')
#ss = ss[1:11]
x = 2.1+np.arange(10)*0.1
s_ave=s_max=s_min= np.empty(shape=[1,0])
for i in np.arange(len(ss)):
    s = np.sort(ss[i])[10:90]
    #s = np.sort(ss[i])
    mean, std = s.mean(), s.std(ddof=1)
    conf = stats.norm.interval(0.68, loc=mean, scale=std)
    s_max = np.append(s_max, mean+std)
    s_min = np.append(s_min, mean-std)
    s_ave = np.append(s_ave, mean)

plt.scatter(x,s_ave,s=100)
yerr = np.zeros([2,len(s_ave)])
yerr[0,:] = s_ave - s_min
yerr[1,:] = s_max - s_ave
plt.errorbar(x,s_ave,yerr=yerr[:,:],ecolor='k',elinewidth=1,
             mew=1,alpha=1,capsize=5,capthick=3,linestyle="none")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(linestyle='--')
#plt.title('SSF Network(${n}$=5000,${γ}$,${m}$=4)',fontsize=22)
plt.title('SSF Network(${n}$=10000,${γ}$,${m}$=4)',fontsize=22)
plt.xlabel('${γ}$',fontsize=30)
plt.ylabel('${β}$',fontsize=30)
#plt.ylabel('${θ}$',fontsize=30)
#plt.ylim(0,700)
plt.show()

'''
s_max[i] = mean+std
s_min[i] = mean-std
s_ave[i] = mean
'''