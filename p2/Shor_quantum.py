import numpy as np
from utils import *
from fractions import Fraction
from II_pkg import *
from QFT import *
from precompiler import *
import random
import sys
from sympy.ntheory.primetest import isprime
from sympy import prime
np.set_printoptions(linewidth=300, precision=3, suppress=True, threshold=np.inf)
def quantum_find_r_sped(x,N):
    with open('circuits/QPF_temp.circuit', 'w') as out:
        numQubit=int((np.ceil(np.log2(N))*2+1)+np.ceil(np.log2(N)))
        topwires=int((np.ceil(np.log2(N))*2+1))
        out.write('{}\n'.format(numQubit))
        out.write('INITSTATE BASIS |'+'0'*(numQubit-1)+'1>\n')
        for i in range(topwires):
            out.write('H {}\n'.format(i))
        for i in range(topwires):
            x1=(x**(2**(topwires-i-1)))%N
            out.write('CFUNC {} {} {} xyModN {} {}\n'.format(i,topwires, numQubit-topwires, x1,N))
            #phase=np.pi/4
            #out.write('CPHASE {} {} {}\n'.format(i,numQubit-1, phase*2**(topwires-1-i)))
        out.write(get_QFT_inv(topwires))
        out.write('MEASURE\n')
    precompile('circuits/QPF_temp.circuit')
    result=II_run('circuits/QPF_temp.circuit.compiled')
    newresult=np.zeros(2**topwires)
    for i in range(len(result)):
        newresult[int(np.floor(i/(2**(numQubit-topwires))))]+=result[i]
    print(newresult)
    #d=np.argmax(newresult)/(2**topwires)
    #darray=[i/(2**topwires) for i in range(len(newresult))]
    for j in range(20):
        d=np.random.choice(range(len(newresult)), p=np.array(newresult)/np.sum(newresult))
        r=abs(Fraction(d/(2**topwires)).limit_denominator(N).denominator)
        print('d/topwire=',(d/(2**topwires)))
        print('trying r=',r)
        if (x**r)%N==1 and r!=0:
            return int(r)
    return -1
'''
def quantum_find_r(x,N):
    with open('circuits/QPF_temp.circuit', 'w') as out:
        numQubit=int((np.ceil(np.log2(N))*2+1)+np.ceil(np.log2(N)))
        topwires=int((np.ceil(np.log2(N))*2+1))
        out.write('{}\n'.format(numQubit))
        out.write('INITSTATE BASIS |'+'0'*(numQubit-1)+'1>\n')
        for i in range(topwires):
            out.write('H {}\n'.format(i))
        for i in range(topwires):
            for j in (2**(topwires-i-1))):
                out.write('CFUNC {} {} {} xyModN {} {}\n'.format(i,topwires, numQubit-topwires, x,N))
            #phase=np.pi/4
            #out.write('CPHASE {} {} {}\n'.format(i,numQubit-1, phase*2**(topwires-1-i)))
        out.write(get_QFT_inv(topwires))
        out.write('MEASURE\n')
    precompile('circuits/QPF_temp.circuit')
    result=II_run('circuits/QPF_temp.circuit.compiled')
    newresult=np.zeros(2**topwires)
    for i in range(len(result)):
        newresult[int(np.floor(i/(2**(numQubit-topwires))))]+=result[i]
    #print(newresult)
    #d=np.argmax(newresult)/(2**topwires)
    #darray=[i/(2**topwires) for i in range(len(newresult))]
    for j in range(20):
        d=np.random.choice(range(len(newresult)), p=np.array(newresult)/np.sum(newresult))
        r=abs(Fraction(d/(2**topwires)).limit_denominator(N).denominator)
        print('trying r=',r)
        if (x**r)%N==1 and r!=0:
            return int(r)
    return -1

'''
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
        r=quantum_find_r_sped(x,N)
        #print('found r={}'.format(r))
        if (r%2==1): continue
        #print('(N,x,r)=({},{},{})'.format(N,x,r))
        a=np.gcd((x**(int(r/2))-1)%N,N)
        #print('a={}, ie {}'.format(a, int(a)))
        if (a==1 or a==N): continue
        print('{}: Found (N,x,r)={},{},{} with factor {}'.format(N,N,x,r,np.gcd(int(a),N)))
        return np.gcd(int(a), N)






#print(quantum_find_r_sped(8,21))
(shor(21))
if len(sys.argv)>1:
    N=int(sys.argv[1])
    shor(N)
#for i in range(3,2**10,2):
#    shor(i)

