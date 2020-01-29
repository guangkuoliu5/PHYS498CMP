import numpy as np
def StateToVec(myState):
    nstates=2**len(myState[0][1])
    myVec=np.full(nstates,0.+0.j)
    for (a,s) in myState:
        myVec[int(s,2)]+=a
    return myVec
def VecToState(myVec):
    nqubits=(int)(np.log2(len(myVec)))
    myState=[]
    for i in range(len(myVec)):
        if(myVec[i]!=0+0j):
            myState.append((myVec[i],bin(i)[2:].zfill(nqubits)))
    return myState
    
def VecToState2(myVec):
    return [(myVec[i],bin(i)[2:].zfill((int)(np.log2(len(myVec))))) for i in range(len(myVec)) if (myVec[i]!=0+0j) ]

def PrettyPrintBinary(myState): #takes in a [(sqrt(0.5),'00'),(sqrt(0.5),'10')], output ( 0.141   |00> + 0.141   |10> )
    myState=VecToState(StateToVec(myState))
    outstring=''
    for (a,s) in myState:
        if a.imag==0:
            if a.real<0:
                outstring+='-'
                a=-a
            else:
                outstring+='+'
            outstring=outstring+' {0:.12f} |{1}> '.format(a.real,s)
        elif a.real==0:
            if a.imag<0:
                outstring+='-'
                a=-a
            else:
                outstring+='+'
            outstring=outstring+' {0:.12f}j |{1}> '.format(a.imag,s)
        else:
            if a.real<0:
                outstring+='-'
                a=-a
            else:
                outstring+='+'
            outstring=outstring+' {0:.12f} |{1}> '.format(a,s)
    if outstring[0]=='+':
        outstring='('+outstring[1:]+')'
    else:
        outstring='( -'+outstring[2:]+')'
    print(outstring)

def PrettyPrintInteger(myState): #takes in a [(sqrt(0.5),'00'),(sqrt(0.5),'10')], output ( 0.141   |0> + 0.141   |2> )
    myVec=StateToVec(myState)
    outstring=''
    for s in range(len(myVec)):
        a=myVec[s]
        if a==0+0j: continue
        if a.imag==0:
            if a.real<0:
                outstring+='-'
                a=-a
            else:
                outstring+='+'
            outstring=outstring+' {0:.12f} |{1}> '.format(a.real,s)
        elif a.real==0:
            if a.imag<0:
                outstring+='-'
                a=-a
            else:
                outstring+='+'
            outstring=outstring+' {0:.12f}j |{1}> '.format(a.imag,s)
        else:
            if a.real<0:
                outstring+='-'
                a=-a
            else:
                outstring+='+'
            outstring=outstring+' {0:.12f} |{1}> '.format(a,s)
    if outstring[0]=='+':
        outstring='('+outstring[1:]+')'
    else:
        outstring='( -'+outstring[2:]+')'
    print(outstring)



myState1=[
        (np.sqrt(0.1)*1.j, '10'),
        (np.sqrt(0.5), '00') ,
        (-np.sqrt(0.4), '01' )
        ]
myState2=[
        (np.sqrt(0.1)*1.j, '101'),
        (np.sqrt(0.5), '000') ,
        (-np.sqrt(0.4), '010' )
        ]
myState3=[
        (1.2+3j, '101'),
        (-1j-5, '000') ,
        (-2+0j, '010' )
        ]

PrettyPrintBinary(myState2)
PrettyPrintInteger(myState2)
print(StateToVec(myState2))
print(VecToState(StateToVec(myState2)))
