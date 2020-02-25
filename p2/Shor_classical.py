import numpy as np
from utils import *
from fractions import Fraction
import random
import sys
from sympy.ntheory.primetest import isprime
from sympy import prime
np.set_printoptions(linewidth=300, precision=3, suppress=True, threshold=100)
def classical_find_r(x,N):
    y=x
    for r in range(2,2*15):
        y=y*x
        if (y%N==1):
            return r
    return -1

def UxNArray(x,N):
    if np.gcd(x,N)!=1: 
        print("ERROR: x, N are not coprime")
        return 0
    def get_basis(j,d):
        ret=[0+0j for i in range(d)]
        ret[j]=1
        return ret
    ret=[]
    d=int(2**np.ceil(np.log2(N)))
    for i in range(d):
        if i<N:
            ret.append(get_basis((i*x)%N, d))
        else:
            ret.append(get_basis(i,d))
    return np.array(ret).T

def classical_find_r_U(x,N):
    #print('(x,N)=',x,N)
    U=UxNArray(x,N)
    (w,v)=np.linalg.eig(U)
    e=(np.angle(w)/(2*np.pi))
    for i in range(20):
        r=abs(Fraction(random.choice(e)).limit_denominator(e.size).denominator)
        #print('trying r=',r)
        if (x**r)%N==1 and r!=0:
            return int(r)
    return -1


def shor(N):
    if isprime(N): 
        #print('{} is a prime'.format(N))
        return -1
    if N%2==0: 
        #print('{}: N is even'.format(N))
        return 2
    for i in range(3,int(np.log2(N))):
        j=i
        while(j<=N):
            if j==N: 
                #print(str(N)+': trivially, N={}^a for some int a'.format(i))
                return i
            j*=i
    while(1):
        x=random.randint(2,int(np.sqrt(N)))
        if (np.gcd(x,N)!=1): 
            #print('{}: by randoming, got factor {}'.format(N,np.gcd(x,N)))
            return(np.gcd(x,N))
        #print('Attempting: N={}, x={}'.format(N,x))
        r=classical_find_r_U(x,N)
        #print('found r={}'.format(r))
        if (r%2==1): continue
        #print('(N,x,r)=({},{},{})'.format(N,x,r))
        a=np.gcd((x**(int(r/2))-1)%N,N)
        #print('a={}, ie {}'.format(a, int(a)))
        if (a==1 or a==N): continue
        print('{}: Found (N,x,r)={},{},{} with factor {}'.format(N,N,x,r,np.gcd(int(a),N)))
        return np.gcd(int(a), N)







if len(sys.argv)>1:
    N=int(sys.argv[1])
    shor(N)
for i in range(3,2**10,2):
    shor(i)
'''
(N,x,r)=(28,23,6)
U=UxNArray(x,N)
print(U)
print(U.shape)
(w,v)=np.linalg.eig(U)

for i in range(len(w)):
    #if np.isclose(2,np.angle(w[i])/(2*np.pi)*4):
    print('eval: ',w[i])
    PrettyPrintInteger(VecToState(v[:,i]))
    #print('evec: ',v[i])
    print()


e=(np.angle(w)/(2*np.pi))
print(e)
print(e*r)
while(1):
    r=abs(Fraction(random.choice(e)).limit_denominator(e.size).denominator)
    if (x**r)%N==1 and r!=0:
        break

print(r)
#print(v[:,-2])
#print(U@v[:,-2])
'''
