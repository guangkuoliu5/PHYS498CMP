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
    filename='QPF/QPF_{}_sped.circuit'.format(N)
    with open(filename, 'w') as out:
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
    return -1
def quantum_find_r(x,N):
    filename='QPF/QPF_{}.circuit'.format(N)
    with open(filename, 'w') as out:
        numQubit=int((np.ceil(np.log2(N))*2+1)+np.ceil(np.log2(N)))
        topwires=int((np.ceil(np.log2(N))*2+1))
        print('(N,x,top)', N,x,topwires)
        out.write('{}\n'.format(numQubit))
        out.write('INITSTATE BASIS |'+'0'*(numQubit-1)+'1>\n')
        for i in range(topwires):
            out.write('H {}\n'.format(i))
        for i in range(topwires):
            for j in range(2**(topwires-i-1)):
                out.write('CFUNC {} {} {} xyModN {} {}\n'.format(i,topwires, numQubit-topwires, x,N))
            #phase=np.pi/4
            #out.write('CPHASE {} {} {}\n'.format(i,numQubit-1, phase*2**(topwires-1-i)))
        out.write(get_QFT_inv(topwires))
        out.write('MEASURE\n')
    return -1






for N in range(3,30):
    quantum_find_r_sped(8,N)
    quantum_find_r(8,N)
numLine=[]
numLine_sped=[]
Nlist=[]
for N in range(3,30):
    Nlist.append(N)
    filename_sped='QPF/QPF_{}_sped.circuit'.format(N)
    filename='QPF/QPF_{}.circuit'.format(N)
    with open(filename,'r') as circuit:
        with open(filename_sped,'r') as circuit_sped:
            numLine.append(len(circuit.readlines()))
            numLine_sped.append(len(circuit_sped.readlines()))

plt.plot(Nlist,numLine,'-',label='non-sped-up version')
plt.plot(Nlist,numLine_sped,'-',label='sped-up version')
plt.plot(Nlist,2*(np.array(Nlist))**2,'--',label=r'$2N^2$')
plt.plot(Nlist,8*(np.array(Nlist))**2,'--',label=r'$8N^2$')
plt.xlabel('n')
plt.ylabel('Number of Lines in the Quantum Period Finding Circuit')
plt.title('Effect of Speeding up the Quantum Period Finding Circuit')
plt.legend()
#plt.show()
plt.savefig('img/QPF.png', dpi=300)


    

#for i in range(3,2**10,2):
#    shor(i)

