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

def Hamming(a,b):
    ret=0
    for i in range(len(a)):
        if a[i]!=b[i]: ret+=1
        
    return ret
def genhammingdata(pmax=10,kmax=60):
    pstep=1
    kstep=1
    indices=np.arange(100)
    mem=np.random.randint(2, size=100)*2-1
    W=np.outer(mem,mem)
    outfile=open('hamming.dat', 'w')
    for p in range(1,pmax,pstep):
        if p>1:
            new_mem=np.random.randint(2, size=100)*2-1
            mem=np.vstack((mem, new_mem))
            W+=np.outer(new_mem,new_mem)
        net=Net(size=100, W=W/p)
        print('p={}'.format(p),mem)
        for k in range(0,kmax, kstep):
            print('(p,k)={}, {}'.format(p,k,mem.shape))
            ###run and compute hamming###
            attempted_hamming=[]
            if p==1:
                memlist=[mem]
            else:
                np.random.shuffle(mem)
                memlist=mem[:5]
            for picked_mem in memlist:
                corrupted_mem=picked_mem.copy()
                np.random.shuffle(indices)
                for picked_index in indices[:k]:
                    corrupted_mem[picked_index]=-picked_mem[picked_index]
                for trials in range(20):
                    net.s=corrupted_mem
                    cur_E=net.E()
                    for sweep in range(30):
                        for i in range(100): net.step()
                        new_E=net.E()
                        if abs(cur_E-new_E)<0.0001:
                            break
                    attempted_hamming.append(Hamming(picked_mem, net.s))
            print(len(attempted_hamming))
            outfile.write('{} {} {}\n'.format(k,p,np.mean(attempted_hamming)))
            #print(attempted_hamming)
    outfile.close()
def plot_hamming(pmax=10,kmax=60):
    infile=open('hamming.dat', 'r')
    Hamming_data=np.zeros((kmax,pmax-1))
    for line in infile.readlines():
        words=line.split()
        Hamming_data[int(words[0]), int(words[1])-1]=float(words[2])
    plt.matshow(Hamming_data, interpolation='bilinear')
    plt.colorbar(label='Hamming distance')
    plt.xlabel('Number of images')
    plt.ylabel('Fraction of Corrupted Bits')
    plt.xticks(np.arange(4,95,5), np.arange(5,96,5)) 
    #plt.title('How well memories can be remembered')
    plt.savefig('img/hamming.png', dpi=300)
    plt.show()




genhammingdata(100,65)
#plot_hamming(100,65)

        

