import numpy as np
import matplotlib.pyplot as plt
from utils import *
from hopfield import *
mysize=6
mem0=int2state(19, mysize) #np.random.randint(2, size=size)*2-1
mem1=int2state(10, mysize) #np.random.randint(2, size=size)*2-1
net=Net(mysize, (np.outer(mem0, mem0)+np.outer(mem1,mem1))/2)
net.b=[-0.5207193 ,-0.60105831 ,0.69290498, 0.16520802,-0.41677622,-0.88333467] #np.random.uniform(-1,1,size=mysize)
print(net.b)
Edict={}
Earr=[]
for i in range(2**mysize):
    net.s=int2state(i, mysize)
    Ei=net.E()
    Edict[i]=Ei
    Earr.append([i,Ei])
Earr=np.array(Earr)
plt.plot(Earr[:,0], Earr[:,1], 'o')
for i in range(2**mysize):
    for f in range(mysize):
        j=flipint(i,f,mysize)
        if i<j:
            plt.plot([i,j], [Edict[i], Edict[j]], '--')

plt.title('Energy Landscape')
plt.savefig('Energyland1.png',dpi=300)
plt.close()




