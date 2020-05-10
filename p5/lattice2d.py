import numpy as np
import matplotlib.pyplot as plt
class lattice2d:
    def __init__(self, N1, N2, M, a1,a2, tau):
        self.N1=N1
        self.N2=N2
        self.M=M
        self.a1=np.array(a1)
        self.a2=np.array(a2)
        self.tau=np.array(tau)
        a2p=np.array([-a2[1],a2[0]])
        a1p=np.array([-a1[1],a1[0]])
        self.b1=2*np.pi/N1/(a2p.dot(self.a1))*a2p
        self.b2=2*np.pi/N2/(a1p.dot(self.a2))*a1p
    def labels(self,n1=None,n2=None):
        if n1==None: (n1,n2)=(self.N1,self.N2)
        ret=[]
        for i1 in range(n1):
            for i2 in range(n2):
                for j in range(self.M):
                    ret.append(((i1,i2),j))
        return ret

    def labeltoR(self,label):
        return label[0][0]*self.a1+label[0][1]*self.a2+self.tau[label[1]]

    def labeltoIndex(self,label):
        return self.M*(label[0][0]*self.N2+label[0][1])+label[1]

    def momentumlabels(self, n1=None, n2=None):
        if n1==None: (n1,n2)=(self.N1,self.N2)
        ret=[]
        for i1 in range(n1):
            for i2 in range(n2):
                for j in range(self.M):
                    ret.append(((i1,i2),j))
        return ret
    def momentumlabeltoK(self, label):
        return label[0][0]*self.b1+label[0][1]*self.b2



if __name__=="__main__":
    graphene=lattice2d(8,10,2,[1,0],[1/2,np.sqrt(3)/2], [[0,0],[0,1/np.sqrt(3)]])
    print(graphene.b1-np.array([1,-1/np.sqrt(3)])*2*np.pi/3)
    print(graphene.b2-np.array([0,2/np.sqrt(3)])*2*np.pi/4)
    print(graphene.labels())
    for label in graphene.labels():
        print(graphene.labeltoR(label))
    print(graphene.labels()[graphene.labeltoIndex(((2,3),1))])
    allR=np.array([graphene.labeltoR(label) for label in graphene.labels()])
    allK=np.array([graphene.momentumlabeltoK(label) for label in graphene.momentumlabels()])
    plt.plot(allR[:,0], allR[:,1],'o')
    plt.show()
    
