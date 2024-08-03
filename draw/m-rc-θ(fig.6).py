import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

os.chdir('F:\\Data') # Enter the disk location of the resulting data
ss = np.loadtxt('BA-m-θ(3,4).txt')
x = 1 + np.arange(10)
s_ave=s_max=s_min= np.empty(shape=[1,0])
for i in np.arange(len(ss)):
    s = np.sort(ss[i])
    mean, std = s.mean(), s.std(ddof=1)
    conf = stats.norm.interval(0.68, loc=mean, scale=std)
    s_max = np.append(s_max, mean+std)
    s_min = np.append(s_min, mean-std)
    s_ave = np.append(s_ave, mean)

plt.scatter(x,s_ave,s=100)
yerr = np.zeros([2,len(s_ave)])
yerr[0,:] = s_ave - s_min
yerr[1,:] = s_max - s_ave
plt.errorbar(x,s_ave,yerr=yerr[:,:],ecolor='k',elinewidth=0.5,
             mec='k',mew=1,ms=10,alpha=1,capsize=5,capthick=3,linestyle="none")

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(linestyle='--')
#plt.title('SSF Network(${n}$=5000,${γ}$=3,${m}$)',fontsize=22)
plt.title('BA Network(${n}$=5000,${m}$)',fontsize=22)
plt.xlabel('${m}$',fontsize=30)
plt.ylabel('${θ}$',fontsize=30)
plt.xlim(0,10.5)
plt.show()
