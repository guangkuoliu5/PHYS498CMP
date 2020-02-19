from utils import *
myState=[(1, '010'), (2, '110')]
#print(Hadamard(1, 3, myState))
#PrettyPrintBinary(Hadamard_nocom(1, 3, myState))
#PrettyPrintBinary(Hadamard(1, 3, myState))
#PrettyPrintBinary(VecToState(HadamardArray(1,3)@StateToVec(myState)))
#PrettyPrintBinary(VecToState(CNOTArray(0,1,3)@StateToVec(myState)))
#PrettyPrintBinary(CNOT(0,1,3, myState))
PrettyPrintBinary(VecToState(PArray(0,3,0.3)@StateToVec(myState)))
PrettyPrintBinary(P(0,3,0.3, myState))

