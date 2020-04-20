import numpy as np
import matplotlib.pyplot as plt
fname='v'
dat1=np.loadtxt(fname+'.dat')
dat2=np.loadtxt("al_"+fname+'.dat')

plt.bar(np.arange(dat1.size)-0.33/2, dat1,0.33, label='Sampling')
plt.bar(np.arange(dat2.size)+0.33/2, dat2,0.33, label='Analytic')
plt.xticks(np.arange(dat1.size),rotation=60)
plt.title('Comparison of '+r'$p(v)$')
plt.xlabel('v represented by integers')
plt.ylabel('Probabilities')
plt.legend()
plt.savefig('img/'+fname+'.png', dpi=300)
plt.close()
