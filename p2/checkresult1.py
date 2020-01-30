from utils import *
np.set_printoptions(linewidth=300)
myInputState=StateToVec([(1,'0011')])
myOutputState=CNOTArray(3,2,4)@myInputState
PrettyPrintBinary(VecToState(myInputState))
PrettyPrintBinary(VecToState(myOutputState))
