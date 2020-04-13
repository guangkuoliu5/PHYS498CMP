import numpy as np
import matplotlib.pyplot as plt
from makeImage import MakeFace, MakeTree
from utils import *
class Net:
    def __init__(self, size=3, W=None, s=None, b=None):
        self.size=size
        if W is None: 
            tmp=np.random.random((size,size))
            self.W=tmp+tmp.T-1 
        else: self.W=W
        if s is None: self.s=np.ones(size) 
        else: self.s=s
        if b is None: self.b=np.zeros(size) 
        else: self.b=b
    def step(self):
        i=np.random.randint(self.size)
        self.s[i]=int(((self.W@self.s)[i]-self.W[i,i]*self.s[i])>self.b[i])*2-1
    def E(self):
        return -self.s@self.W@self.s/2+self.b@self.s

face=MakeFace().flatten()*2-1
tree=MakeTree().flatten()*2-1
corrupted_face=np.hstack((np.ones(50), face[50:]))
corrupted_tree=np.hstack((np.ones(50), tree[50:]))

net=Net(size=100, W=(np.outer(face, face)+np.outer(tree,tree))/2)
net.s=corrupted_tree
matshowstr(net.s)
for i in range(100*20):
    net.step()
    if i==20: matshowstr(net.s)
matshowstr(net.s)
plt.show()
