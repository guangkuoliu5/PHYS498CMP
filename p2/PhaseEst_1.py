from utils import *
from precompiler import *
from datetime import datetime
import sys
import numpy as np
filename='PhaseEst/PhaseEst_1.temp.circuit'
def write_phase_circuit_1(phase, filename):
    with open(filename, 'w') as out:
        out.write('2\nH 0\nCPHASE 0 1 {}\nH 0'.format(phase))

est_x=[]
est_y=[]
for phase in np.linspace(0,2*np.pi,100):
    write_phase_circuit_1(phase, filename)
    precompile(filename)
    with open(filename+'.compiled','r') as circuit:
        numQubit=int(circuit.readline())
        state=[(1+0j, '0'*(numQubit-1)+'1')]
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
            print(line)
            #print(state)
            PrettyPrintBinary(state)
        newstate=[(c,v[:-1]) for (c,v) in state]
        result=measure(StateToVec(newstate), numTrials=100)
        est_x.append(phase)
        est_y.append(np.argmax(result)/(2**(numQubit-1))*2*np.pi)
        print('State: ', newstate)
        print('est: ', est_y[-1])

plt.plot(est_x, est_y, '.', label='Phase Estimation')
plt.plot(est_x, est_x, '--', label='Actual Phase')
plt.legend()
plt.show()

        


        


