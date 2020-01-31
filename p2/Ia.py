from utils import *
import sys
import numpy as np
with open(sys.argv[1],'r') as circuit:
    numQubit=int(circuit.readline())
    stateVec=np.zeros(2**numQubit)
    for line in circuit.readlines():
        words=line.split()
        gate=words[0]
        if gate=='INITSTATE':
            stateVec=initState(words[1], words[2])
            PrettyPrintBinary(VecToState(stateVec))

