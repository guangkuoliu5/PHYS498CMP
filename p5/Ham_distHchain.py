from lattice1d import *
from lattice2d import *
import numpy as np
np.set_printoptions(precision=3, suppress=True,linewidth=200)
N=18
M=2
Hchain=lattice1d(N,M,2,[0,0.8])
H=np.matrix(np.zeros((N*M,N*M)))
labels=Hchain.labels()
for i in range(N*M):
    cur=labels[i]
    if cur[1]==0:
        H[i, Hchain.labeltoIndex((cur[0], 1))]=-1
        H[i, Hchain.labeltoIndex(((cur[0]-1)%N, 1))]=-0.1
    if cur[1]==1:
        H[i, Hchain.labeltoIndex((cur[0], 0))]=-1
        H[i, Hchain.labeltoIndex(((cur[0]+1)%N, 0))]=-0.1

F=np.matrix(np.zeros((N*M,N*M))+1j)
for i in range(N*M):
    for j in range(N*M):
        ri=Hchain.labeltoR(labels[i])[0]
        kj=Hchain.momentumlabeltoK(labels[j])[0]
        delta=int(labels[i][1]==labels[j][1])
        F[i,j]=np.exp(1j*kj*ri)*delta/np.sqrt(N)
#print()
#print(F.H@F-np.eye(N*M))
HK=F.H@H@F
#print(HK)
#print(np.linalg.eigh(H)[0])
xarr=[]
yarr1=[]
yarr2=[]
for i in range(N):
    xarr.append(Hchain.momentumlabeltoK((i,0))[0])
    yarr1.append(np.linalg.eigh(HK[2*i:2*i+2, 2*i:2*i+2])[0][0])
    yarr2.append(np.linalg.eigh(HK[2*i:2*i+2, 2*i:2*i+2])[0][1])

#print(xarr,yarr1,yarr2)
plt.plot(xarr, yarr1, 'ro',label='Filled Energy levels')
plt.plot(xarr, yarr2, 'bo',label='Unfilled Energy levels')
plt.axhline(0,label='Fermi Energy')
plt.legend()
plt.xlabel('k')
plt.ylabel('E')
plt.title('E(k) vs. k for Distorted Hydrogen chain')
plt.savefig('img/Ham_disthchain.png', dpi=300)
plt.close()

