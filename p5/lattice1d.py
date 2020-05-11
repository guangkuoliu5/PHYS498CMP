import numpy as np
import matplotlib.pyplot as plt
class lattice1d:
    def __init__(self, N, M, a, tau):
        self.N=N
        self.M=M
        self.a=a
        self.tau=tau
        self.b=2*np.pi/(N*a)
    def labels(self,n=None):
        if n==None: n=self.N
        ret=[]
        for i in range(n):
            for j in range(self.M):
                ret.append((i,j))
        return ret

    def labeltoR(self,label):
        return np.array([label[0]*self.a+self.tau[label[1]],0])

    def labeltoIndex(self,label):
        return label[0]*self.M+label[1]

    def momentumlabels(self, n=None):
        if n==None: n=self.N
        ret=[]
        for i in range(n):
            for j in range(self.M):
                ret.append((i,j))
        return ret
    def momentumlabeltoK(self, label):
        return np.array([label[0]*self.b,0])



if __name__=="__main__":
    Hchain=lattice1d(6,1,1,[0])

    print(Hchain.labels())
    print([Hchain.labeltoR(Hchain.labels()[i]) for i in range(6)])
    print([Hchain.momentumlabeltoK(Hchain.momentumlabels()[i]) for i in range(6)])
    print(Hchain.labeltoIndex(Hchain.labels()[3]))

    distHchain=lattice1d(3,2,2,[0,0.8])

    print()
    print(distHchain.labels())
    print([distHchain.labeltoR(distHchain.labels()[i]) for i in range(6)])
    print(distHchain.momentumlabels())
    print(distHchain.b)
    print([distHchain.momentumlabeltoK(distHchain.momentumlabels()[i]) for i in range(6)])
    print(distHchain.labeltoIndex(distHchain.labels()[3]))
