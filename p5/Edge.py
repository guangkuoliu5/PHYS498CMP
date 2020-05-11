from lattice1d import *
from lattice2d import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(precision=3, suppress=True,linewidth=200)
N1=27
N2=27
M=2
Mh=0.2
t=0.3
phi=0.7
graphene=lattice2d(N1,N2,M,[1,0],[1/2,np.sqrt(3)/2], [[0,0],[0,1/np.sqrt(3)]])
labels=graphene.labels()
H=np.matrix(np.zeros((len(labels),len(labels)))+0j)
for i in range(len(labels)):
    cur=labels[i]
    other=(cur[1]+1)%2
    nei1=(cur[0][0], (cur[0][1]-1+cur[1]*2))
    nei2=((cur[0][0]+1-cur[1]*2)%N1, (cur[0][1]-1+cur[1]*2))
    neinei=[]
    neinei.append(((cur[0][0]+1)%N1, (cur[0][1]+0)))
    neinei.append(((cur[0][0]+0)%N1, (cur[0][1]+1)))
    neinei.append(((cur[0][0]-1)%N1, (cur[0][1]+1)))
    neinei.append(((cur[0][0]-1)%N1, (cur[0][1]+0)))
    neinei.append(((cur[0][0]+0)%N1, (cur[0][1]-1)))
    neinei.append(((cur[0][0]+1)%N1, (cur[0][1]-1)))
    curphi=phi*(1-2*cur[1])
    H[i,i]=Mh*(1-2*cur[1])
    H[i, graphene.labeltoIndex((cur[0], other))]=-1
    if 0<=nei1[1] and nei1[1]<=N2-1:
        H[i, graphene.labeltoIndex((nei1, other))]=-1
    if 0<=nei2[1] and nei2[1]<=N2-1:
        H[i, graphene.labeltoIndex((nei2, other))]=-1
    for j in [0,2,4]:
        if 0<=neinei[j][1] and neinei[j][1]<=N2-1:
            H[i, graphene.labeltoIndex((neinei[j], cur[1]))]=-t*np.exp(-1j*curphi)
    for j in [1,3,5]:
        if 0<=neinei[j][1] and neinei[j][1]<=N2-1:
            H[i, graphene.labeltoIndex((neinei[j], cur[1]))]=-t*np.exp(1j*curphi)

#print(H)
#print(np.linalg.norm(H.H-H))
print(np.min(np.abs(np.linalg.eigh(H)[0])))
'''
F=np.matrix(np.zeros((len(labels),len(labels)))+1j)
for i in range(len(labels)):
    for j in range(len(labels)):
        ri=graphene.labeltoR(labels[i])
        kj=graphene.momentumlabeltoK(labels[j])
        delta=int(labels[i][1]==labels[j][1])
        F[i,j]=np.exp(1j*kj.dot(ri))*delta/np.sqrt(N1*N2)
#print()
#print(np.linalg.norm(F.H@F-np.eye(len(labels))))
HK=F.H@H@F
#print(HK)
#plt.matshow(np.abs(HK)); plt.show()
#print((np.linalg.eigh(HK)[0]))
#print(np.linalg.norm(np.linalg.eigh(HK)[0]-np.linalg.eigh(H)[0]))
xarr=[]
yarrs=[]
for j in range(N1):
    xarr.append(graphene.momentumlabeltoK(((j,0),0))[0])
    i=graphene.labeltoIndex(((j,0),0))
    #if j==0: plt.matshow(np.abs(HK[i:i+4*N2, i:i+4*N2])); plt.show()
    yarrs.append(np.linalg.eigh(HK[i:i+2*N2, i:i+2*N2])[0])

xarr=np.array(xarr)
yarrs=np.array(yarrs)
for yarr in yarrs.T:
    plt.plot(xarr,yarr,'o-')
plt.xlabel('kx')
plt.ylabel('E')
plt.title('Energy Bands vs. kx for Edge Modes')
#plt.show()
plt.savefig('img/edge{:.2f}.png'.format(Mh), dpi=300)
plt.close()

'''
