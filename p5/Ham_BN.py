from lattice1d import *
from lattice2d import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
np.set_printoptions(precision=3, suppress=True,linewidth=200)
N1=27
N2=27
M=2
Mh=-0.1
graphene=lattice2d(N1,N2,M,[1,0],[1/2,np.sqrt(3)/2], [[0,0],[0,1/np.sqrt(3)]])
labels=graphene.labels()
H=np.matrix(np.zeros((len(labels),len(labels))))
for i in range(len(labels)):
    cur=labels[i]
    other=(cur[1]+1)%2
    nei1=(cur[0][0], (cur[0][1]-1+cur[1]*2)%N2)
    nei2=((cur[0][0]+1-cur[1]*2)%N1, (cur[0][1]-1+cur[1]*2)%N2)
    H[i,i]=Mh*(1-2*cur[1])
    H[i, graphene.labeltoIndex((cur[0], other))]=-1
    H[i, graphene.labeltoIndex((nei1, other))]=-1
    H[i, graphene.labeltoIndex((nei2, other))]=-1
'''
for i in range(0,N1):
    for j in range(0,N2):
        idx=graphene.labeltoIndex(((i,j),0))
        for jdx in range(len(labels)):
            if H[idx,jdx]==-1:
                arr=np.array([graphene.labeltoR(labels[idx]),graphene.labeltoR(labels[jdx])]).T
                plt.plot(arr[0],arr[1],'y-')
                plt.plot(arr[0,0],arr[1,0],'bo')
                plt.plot(arr[0,1],arr[1,1],'ro')

plt.show()
'''
F=np.matrix(np.zeros((len(labels),len(labels)))+1j)
for i in range(len(labels)):
    for j in range(len(labels)):
        ri=graphene.labeltoR(labels[i])
        kj=graphene.momentumlabeltoK(labels[j])
        delta=int(labels[i][1]==labels[j][1])
        F[i,j]=np.exp(1j*kj.dot(ri))*delta/np.sqrt(N1*N2)
#print()
print(np.linalg.norm(H.H-H))
#print(np.linalg.norm(F.H@F-np.eye(len(labels))))
#print(np.linalg.eigh(H)[0])
HK=F.H@H@F
#print(HK)
#plt.matshow(np.abs(HK)); plt.show()
#print((np.linalg.eigh(HK)[0]))
#print(np.linalg.norm(np.linalg.eigh(HK)[0]-np.linalg.eigh(H)[0]))
xarr=[]
yarr1=[]
yarr2=[]
for j in range(N1):
    for k in range(N2):
        xarr.append(graphene.momentumlabeltoK(((j,k),0)))
        i=graphene.labeltoIndex(((j,k),0))
        yarr1.append(np.linalg.eigh(HK[i:i+2, i:i+2])[0][0])
        yarr2.append(np.linalg.eigh(HK[i:i+2, i:i+2])[0][1])

#print(xarr,yarr1,yarr2)
xarr=np.array(xarr)
yarr1=np.array(yarr1)
yarr2=np.array(yarr2)
#print(xarr[:,0])
#print(yarr1)
#print(yarr2)
plot3d=0
if (plot3d) :
    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    ax.plot_trisurf(xarr[:,0],xarr[:,1], yarr1)
    ax.plot_trisurf(xarr[:,0],xarr[:,1], yarr2)
    ax.set_xlabel(r'$k_x$')
    ax.set_ylabel(r'$k_y$')
    ax.set_zlabel(r'$E$')
    ax.view_init(20,30)
    plt.title('E vs. (kx,ky) for Boron Nitride')
    plt.savefig('img/Ham_BN3d.png',dpi=300)
    plt.close()
else:
    for i in range(0,N1,4):
        kx=xarr[i*N2][0]
        plt.plot(xarr[i*N2:(i+1)*N2,1], yarr1[i*N2:(i+1)*N2],'ro')
        plt.plot(xarr[i*N2:(i+1)*N2,1], yarr2[i*N2:(i+1)*N2],'bo')
        plt.xlabel('ky')
        plt.ylabel('E')
        plt.title('E vs. ky for Boron Nitride at kx={:.2f}'.format(kx))
        plt.savefig('img/Ham_BN2d/'+str(i)+'.png', dpi=300)
        plt.close()

