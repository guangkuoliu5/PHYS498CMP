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

def tensorMe_recursive(listOfMatrices):
    if len(listOfMatrices)==1:
        return listOfMatrices[0]
    else:
        A=listOfMatrices[0]
        B=tensorMe(listOfMatrices[1:])
        return np.kron(A,B)
def tensorMe(listOfMatrices):
    ret=listOfMatrices[0]
    for M in listOfMatrices[1:]:
        ret=np.kron(ret,M)
    return ret

def HadamardArray(i,k):
    r=np.sqrt(0.5)
    listOfMatrices=[np.eye(2) if (i!=j) else np.array([[r,r],[r,-r]]) for j in range(k) ] 
    return tensorMe(listOfMatrices)

def CNOTArray(c, t, n):
    size=2**n
    ret=np.zeros((size,size))
    for i in range(size):
        bra=bin(i)[2:].zfill(n)
        ket=bra
        if bra[c]=='1':
            ket=bra[:t]+str(1- int(bra[t]))+bra[t+1:]
        ret[int(bra,2),int(ket,2)]=1.
    return ret
