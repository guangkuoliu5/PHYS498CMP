from utils import *
np.set_printoptions(linewidth=300)
myInputState=StateToVec([(1,'0011000000')])
myOutputState=PArray(2,10,np.pi/3)@myInputState
PrettyPrintBinary(VecToState(myInputState))
PrettyPrintBinary(VecToState(myOutputState))
