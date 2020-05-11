from lattice1d import *
from lattice2d import *
import numpy as np
np.set_printoptions(precision=3, suppress=True)
N=18
M=1
Hchain=lattice1d(N,M,1,[0])
H=np.matrix(np.zeros((N*M,N*M)))
labels=Hchain.labels()
for i in range(N*M):
    cur=labels[i]
    H[i, Hchain.labeltoIndex(((cur[0]-1)%N, 0))]=-1
    H[i, Hchain.labeltoIndex(((cur[0]+1)%N, 0))]=-1

print(H)
print(H.H-H)
F=np.matrix([[np.exp(1j*Hchain.momentumlabeltoK((j,0)).dot(Hchain.labeltoR((i,0))))/np.sqrt(N) for j in range(N*M)] for i in range(N*M)])
print()
print(F.H@F-np.eye(N))
HK=F.H@H@F
print(HK)
print(np.linalg.eigh(H)[0])
xarr=np.array([Hchain.momentumlabeltoK((j,0))[0] for j in range(N)])
yarr=np.array([np.real(HK[j,j]) for j in range(N)])
idx=np.argsort(yarr)
split=int(N/2)
plt.plot(xarr[idx[:split]],yarr[idx[:split]],'ro',label='Filled Energy levels')
plt.plot(xarr[idx[split:]],yarr[idx[split:]],'bo',label='Unfilled Energy levels')
plt.plot(xarr,-2*np.cos(xarr),'y-',label='Expected result\n E(k)=-2cos(k)')
plt.axhline((yarr[idx[split]]+yarr[idx[split-1]])/2,label='Fermi Energy')
plt.legend()
plt.xlabel('k')
plt.ylabel('E')
plt.title('E(k) vs. k for Hydrogen chain')
plt.savefig('img/Ham_hchain.png', dpi=300)
plt.close()

