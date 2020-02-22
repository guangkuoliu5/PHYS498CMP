from utils import *
import numpy
myState2=[
  (numpy.sqrt(0.1)*1.j, '101'),
  (numpy.sqrt(0.5), '000') ,
  (-numpy.sqrt(0.4), '010' )
]
#PrettyPrintBinary(myState2)
#PrettyPrintInteger(myState2)
print(StateToVec(myState2))
print(VecToState(StateToVec(myState2)))
