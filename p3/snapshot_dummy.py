import numpy as np
import matplotlib.pyplot as plt
L=9
#A=np.random.randint(0,2,(L,L))*2-1
A=np.zeros((L,L))-1
#outFileName='img81/snapshot_dummy_0_'+str(L)+'.png'
outFileName='img81/snapshot_dummy_inf_'+str(L)+'.png'
plt.matshow(A)
#plt.title('beta=0')
plt.title('beta='+r'$\infty$')
plt.savefig(outFileName)
plt.close()


