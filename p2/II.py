from utils import *
from datetime import datetime
import sys
import numpy as np
with open(sys.argv[1],'r') as circuit:
    numQubit=int(circuit.readline())
    state=[(1+0j, '0'*numQubit)]
    for line in circuit.readlines():
        words=line.split()
        gate=words[0]
        if gate=='INITSTATE':
            stateVec=initState(words[1], words[2])
            state=VecToState(stateVec)
            #PrettyPrintBinary(VecToState(stateVec))
        if gate=='H':
            state=Hadamard(int(words[1]), numQubit, state)
        if gate=='P':
            state=P(int(words[1]), numQubit, float(words[2]), state)
        if gate=='CNOT':
            state=CNOT(int(words[1]), int(words[2]), numQubit,state)
        if gate=='MEASURE':
            result=measure(StateToVec(state), numTrials=1000)
            break
    #np.set_printoptions(linewidth=300, precision=3, suppress=True, threshold=50)
    #print('The entire circuit as a matrix is: ')
    #print(totalMatrix)
    #print(totalMatrix@np.matrix(totalMatrix).getH())
    print('\nThe final state is: ')
    PrettyPrintBinary(state)
    #print(stateVec)
    if gate=='MEASURE':
        print('\nThe measurement result is: ')
        print(result)
        print('\nThe histogram is saved to:')
        print(createHist(result))
        


        


