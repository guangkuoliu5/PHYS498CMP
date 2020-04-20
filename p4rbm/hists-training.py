import numpy as np
import matplotlib.pyplot as plt
dat1=np.loadtxt('pv.dat')
dat2=np.loadtxt('qv.dat')
errs=np.sqrt(dat1)
errs/=dat1.sum()
dat1/=dat1.sum()
dat2/=dat2.sum()
plt.bar(np.arange(dat1.size)-0.33/2, dat1,0.33, yerr=errs,label=r'$p(v)$')
plt.bar(np.arange(dat2.size)+0.33/2, dat2,0.33, label=r'$q(v)$')
plt.xticks(np.arange(dat1.size),rotation=60)
plt.title(r'$q(v)$'+' vs '+r'$p(v)$')
plt.xlabel('v represented by integers')
plt.ylabel('Probabilities')
plt.legend()
#plt.show()
plt.savefig('img/training.png', dpi=300)
plt.close()