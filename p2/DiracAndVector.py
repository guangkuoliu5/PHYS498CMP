from utils import *


myState2=[
        (np.sqrt(0.1)*1.j, '101'),
        (np.sqrt(0.5), '000') ,
        (-np.sqrt(0.4), '010' )
        ]

PrettyPrintBinary(myState2)
PrettyPrintInteger(myState2)
print(StateToVec(myState2))
print(VecToState(StateToVec(myState2)))
