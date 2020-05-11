from lattice1d import *
from lattice2d import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(precision=3, suppress=True,linewidth=200)
N1=27
N2=27
M=2
Mh=1.2
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
yarr=[]
evecs=[]
for j in range(N1):
    evecs.append([])
    xarr.append([])
    yarr.append([])
    for k in range(N2):
        xarr[-1].append(graphene.momentumlabeltoK(((j,k),0))[0])
        yarr[-1].append(graphene.momentumlabeltoK(((j,k),0))[1])
        i=graphene.labeltoIndex(((j,k),0))
        mat=HK[i:i+2, i:i+2]
        eigs=np.linalg.eigh(mat)
        evec1=eigs[1][:,0]
        evecs[-1].append(evec1)
bflux=[]
for j in range(N1):
    bflux.append([])
    for k in range(N2):
        bflux[-1].append(np.angle(evecs[j][k].H@evecs[(j+1)%N1][k] * evecs[(j+1)%N1][k].H@evecs[(j+1)%N1][k-1] * evecs[(j+1)%N1][k-1].H@evecs[j][k-1] * evecs[j][k-1].H@evecs[j][k])[0,0])

bflux=np.array(bflux)
xarr=np.array(xarr)
yarr=np.array(yarr)
#print(xarr)
#print(bflux)
plt.contour(xarr,yarr, bflux, 10)
plt.xlabel(r'$k_x$')
plt.ylabel(r'$k_y$')
plt.title('Berry Curvature')
#plt.show()
plt.savefig('img/berryflux2d_{:.2f}.png'.format(Mh),dpi=300)
plt.close()
    


