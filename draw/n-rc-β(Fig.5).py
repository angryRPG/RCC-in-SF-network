import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

os.chdir('F:\\Data') # Enter the disk location of the resulting data
ss = np.loadtxt('SF-n-β(3,4).txt')
x = 1000+np.arange(10)*1000
s_ave=s_max=s_min= np.empty(shape=[1,0])
for i in np.arange(len(ss)):
    s = np.sort(ss[i])
    mean, std = s.mean(), s.std(ddof=1)
    conf = stats.norm.interval(0.68, loc=mean, scale=std)
    s_max = np.append(s_max, conf[1])
    s_min = np.append(s_min, conf[0])
    s_ave = np.append(s_ave, mean)

plt.scatter(x,s_ave,s=100)
yerr = np.zeros([2,len(s_ave)])
yerr[0,:] = s_ave - s_min
yerr[1,:] = s_max - s_ave
plt.errorbar(x,s_ave,yerr=yerr[:,:],ecolor='k',elinewidth=1,
            mew=1,ms=10,alpha=1,capsize=5,capthick=3,linestyle="none")
plt.yticks([0.0,0.5,1.0,1.5,1.8,2.00])
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(linestyle='--')
plt.title('SSF Network(${n}$,${γ}$=3,${m}$=4)',fontsize=22)
#plt.title('BA Network(${n}$,${m}$=4)',fontsize=22)
plt.plot([0,11000],[1.8,1.8],'r--',lw=1)
plt.xlabel('${n}$',fontsize=30)
plt.ylabel('${β}$',fontsize=30)
plt.ylim(1,2)
plt.xlim(0,11000)
plt.show()

