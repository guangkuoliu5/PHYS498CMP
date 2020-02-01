from utils import *
from datetime import datetime
import sys
import numpy as np
with open(sys.argv[1],'r') as circuit:
    numQubit=int(circuit.readline())
    stateVec=np.full(2**numQubit, 0+0j); stateVec[0]=1+0j
    totalMatrix=np.eye(2**numQubit)
    for line in circuit.readlines():
        words=line.split()
        gate=words[0]
        if gate=='INITSTATE':
            stateVec=initState(words[1], words[2])
            #PrettyPrintBinary(VecToState(stateVec))
        if gate=='H':
            totalMatrix=HadamardArray(int(words[1]), numQubit)@totalMatrix
        if gate=='P':
            totalMatrix=PArray(int(words[1]), numQubit, float(words[2]))@totalMatrix
        if gate=='CNOT':
            totalMatrix=CNOTArray(int(words[1]), int(words[2]), numQubit)@totalMatrix
        if gate=='MEASURE':
            stateVec=totalMatrix@stateVec
            result=measure(stateVec, numTrials=1000)
            break
    if gate!='MEASURE':
        stateVec=totalMatrix@stateVec
    np.set_printoptions(linewidth=300, precision=3, suppress=True, threshold=50)
    print('The entire circuit as a matrix is: ')
    print(totalMatrix)
    #print(totalMatrix@np.matrix(totalMatrix).getH())
    print('\nThe final state is: ')
    PrettyPrintBinary(VecToState(stateVec))
    #print(stateVec)
    if gate=='MEASURE':
        print('\nThe measurement result is: ')
        print(result)
        print('\nThe histogram is saved to:')
        print(createHist(result))
        


        


