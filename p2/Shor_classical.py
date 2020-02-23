import numpy as np
import random
import sys
from sympy.ntheory.primetest import isprime
from sympy import prime
def classical_find_r(x,N):
    y=x
    for r in range(2,2*15):
        y=y*x
        if (y%N==1):
            return r
    return -1

def shor(N):
    if isprime(N): 
        print('{} is a prime'.format(N))
        return -1
    if N%2==0: 
        print('{}: N is even'.format(N))
        return 2
    for i in range(3,int(np.log2(N))):
        j=i
        while(j<=N):
            if j==N: 
                print(str(N)+': trivially, N={}^a for some int a'.format(i))
                return i
            j*=i
    while(1):
        x=random.randint(2,int(np.sqrt(N)))
        if (np.gcd(x,N)!=1): 
            print('{}: by randoming, got factor {}'.format(N,np.gcd(x,N)))
            return(np.gcd(x,N))
        #print('Attempting: N={}, x={}'.format(N,x))
        r=classical_find_r(x,N)
        #print('found r={}'.format(r))
        if (r%2==1): continue
        #print('(N,x,r)=({},{},{})'.format(N,x,r))
        a=np.gcd(x**(int(r/2))-1,N)
        #print('a={}, ie {}'.format(a, int(a)))
        if (a==1): continue
        print('{}: Found (N,x,r)={},{},{} with factor {}'.format(N,N,x,r,np.gcd(int(a),N)))
        return np.gcd(int(a), N)







N=prime(40)*prime(45)
if len(sys.argv)>1:
    N=int(sys.argv[1])
#shor(N)
for i in range(2,2**10,1):
    shor(i)

