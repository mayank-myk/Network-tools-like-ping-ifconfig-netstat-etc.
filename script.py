import sys
import string
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import matplotlib.mlab as mlab
import math
import seaborn as sns


l = list()

ff = open('Q3b.txt','r')
next(ff)
for line in ff:
	words = line.split()
	if(len(words)>0 and words[1] == "bytes"):
		time = words[6][5:]
		#print(time)
	val = float(time)
	l.append(val)
	#print(val)

l = sorted(l)
val1 = l[99]
val2 = l[100]
# print val1, val2
# print(float((val1+val2)/2))

# print(np.mean(l))
# print(np.std(l))
fit = stats.norm.pdf(l, np.mean(l), np.std(l))
plt.plot(l,fit,'-')
# sns.distplot(l,rug = False,hist = True)
#plt.hist(l,normed=True)
plt.show()
