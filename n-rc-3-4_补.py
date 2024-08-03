import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import os


os.chdir('C:\\Users\\LZH\\Desktop\\result\\n-rc')
x,s = np.loadtxt('BA-n-θ(4).txt')
x = 1000+np.arange(10)*1000
s_ave = s
mean = mean+0.01
std = std-0.005


i = 8
s = np.sort(ss[i])
mean, std = s.mean(), s.std(ddof=1)
s_max[i] = mean+std
s_min[i] = mean-std
s_ave[i] = mean