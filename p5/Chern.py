from lattice1d import *
from lattice2d import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(precision=3, suppress=True,linewidth=200)
def chern(Mh):
    N1=27
    N2=27
    M=2
    t=0.3
    phi=0.7
    graphene=lattice2d(N1,N2,M,[1,0],[1/2,np.sqrt(3)/2], [[0,0],[0,1/np.sqrt(3)]])
    labels=graphene.labels()
    H=np.matrix(np.zeros((len(labels),len(labels)))+0j)
    for i in range(len(labels)):
        cur=labels[i]
        other=(cur[1]+1)%2
        nei1=(cur[0][0], (cur[0][1]-1+cur[1]*2)%N2)
        nei2=((cur[0][0]+1-cur[1]*2)%N1, (cur[0][1]-1+cur[1]*2)%N2)
        neinei=[]
        neinei.append(((cur[0][0]+1)%N1, (cur[0][1]+0)%N2))
        neinei.append(((cur[0][0]+0)%N1, (cur[0][1]+1)%N2))
        neinei.append(((cur[0][0]-1)%N1, (cur[0][1]+1)%N2))
        neinei.append(((cur[0][0]-1)%N1, (cur[0][1]+0)%N2))
        neinei.append(((cur[0][0]+0)%N1, (cur[0][1]-1)%N2))
        neinei.append(((cur[0][0]+1)%N1, (cur[0][1]-1)%N2))
        curphi=phi*(1-2*cur[1])
        H[i,i]=Mh*(1-2*cur[1])
        H[i, graphene.labeltoIndex((cur[0], other))]=-1
        H[i, graphene.labeltoIndex((nei1, other))]=-1
        H[i, graphene.labeltoIndex((nei2, other))]=-1
        for j in [0,2,4]:
            H[i, graphene.labeltoIndex((neinei[j], cur[1]))]=-t*np.exp(-1j*curphi)
        for j in [1,3,5]:
            H[i, graphene.labeltoIndex((neinei[j], cur[1]))]=-t*np.exp(1j*curphi)

    F=np.matrix(np.zeros((len(labels),len(labels)))+1j)
    for i in range(len(labels)):
        for j in range(len(labels)):
            ri=graphene.labeltoR(labels[i])
            kj=graphene.momentumlabeltoK(labels[j])
            delta=int(labels[i][1]==labels[j][1])
            F[i,j]=np.exp(1j*kj.dot(ri))*delta/np.sqrt(N1*N2)
    HK=F.H@H@F
    xarr=[]
    evecs=[]
    for j in range(N1):
        evecs.append([])
        for k in range(N2):
            xarr.append(graphene.momentumlabeltoK(((j,k),0)))
            i=graphene.labeltoIndex(((j,k),0))
            mat=HK[i:i+2, i:i+2]
            eigs=np.linalg.eigh(mat)
            evec1=eigs[1][:,0]
            evecs[-1].append(evec1)
    bflux=[]
    for j in range(N1):
        for k in range(N2):
            bflux.append(np.angle(evecs[j][k].H@evecs[(j+1)%N1][k] * evecs[(j+1)%N1][k].H@evecs[(j+1)%N1][k-1] * evecs[(j+1)%N1][k-1].H@evecs[j][k-1] * evecs[j][k-1].H@evecs[j][k])[0,0])

    bflux=np.array(bflux)
    return np.sum(bflux)/2/np.pi

Mhlist=[0,0.5,0.8,0.9,1.0,1.005,1.1,1.2,1.5,2.0]
clist=[chern(i) for i in Mhlist]
plt.plot(Mhlist, clist, 'o-')
plt.xlabel('M')
plt.ylabel('Chern number')
plt.title('Chern number vs. M')
#plt.show()
plt.savefig('img/chern.png', dpi=300)
plt.close()

