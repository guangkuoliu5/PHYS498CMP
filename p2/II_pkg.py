from utils import *
from datetime import datetime
import sys
import numpy as np
def xyModN(k,n,x,N,state,cc=-1):
    ret=[]
    for (c_k,v_k) in state:
        if cc!=-1 and v_k[cc]=='0':
                ret.append((c_k,v_k))
                continue
        yval=(int(v_k[k:k+n],2)*x)%N
        #print(yval)
        ret.append((c_k, v_k[:k]+bin(yval)[2:].zfill(n)+v_k[k+n:]))
        #print(ret)
    return RemoveDuplicates(ret)

def II_run(filename):
    with open(filename,'r') as circuit:
        numQubit=int(circuit.readline())
        state=[(1+0j, '0'*numQubit)]
        #state=[(np.sqrt(1/2)+0j, '1'.zfill(numQubit)),(-np.sqrt(1/2)+0j, '100'.zfill(numQubit))]
        #PrettyPrintBinary(state)
        for line in circuit.readlines():
            if len(line)<3: continue
            words=line.split()
            gate=words[0]
            if gate=='INITSTATE':
                stateVec=initState(words[1], words[2])
                state=VecToState(stateVec)
                #PrettyPrintBinary(state)
            if gate=='H':
                state=Hadamard(int(words[1]), numQubit, state)
            if gate=='P':
                state=P(int(words[1]), numQubit, float(words[2]), state)
            if gate=='CNOT':
                state=CNOT(int(words[1]), int(words[2]), numQubit,state)
            if gate=='FUNC':
                k,n=int(words[1]),int(words[2])
                if words[3]=='xyModN':
                    x,N=int(words[4]),int(words[5])
                    state=xyModN(k,n,x,N,state)
            if gate=='CFUNC':
                c,k,n=int(words[1]),int(words[2]),int(words[3])
                if words[4]=='xyModN':
                    x,N=int(words[5]),int(words[6])
                    state=xyModN(k,n,x,N,state,cc=c)
            if gate=='MEASURE':
                #print('Measuring')
                result=measure(StateToVec(state), numTrials=100)
                break
            #print(line)
            #PrettyPrintBinary(state)
        if gate=='MEASURE':
            return result
        return []
        #np.set_printoptions(linewidth=300, precision=3, suppress=True, threshold=50)
        #print(stateVec)


        
if len(sys.argv)>1:
    result=II_run(sys.argv[1])


