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
        if abs(a.imag)<=1e-10:
            if a.real<0:
                outstring+='-'
                a=-a
            else:
                outstring+='+'
            outstring=outstring+' {0:.12f} |{1}> '.format(a.real,s)
        elif abs(a.real)<=1e-10:
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
        if abs(a.imag)<=1e-10:
            if a.real<0:
                outstring+='-'
                a=-a
            else:
                outstring+='+'
            outstring=outstring+' {0:.12f} |{1}> '.format(a.real,s)
        elif abs(a.real)<=1e-10:
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

def PArray(i,k,phi):
    listOfMatrices=[np.eye(2) if (i!=j) else np.array([[1,0],[0,np.exp(phi*1j)]]) for j in range(k)]
    return tensorMe(listOfMatrices)

def PArray_braket(c,n,phi):
    size=2**n
    ret=np.full((size,size),0+0j)
    for i in range(size):
        bra=bin(i)[2:].zfill(n)
        ket=bra
        if bra[c]=='1':
            ret[int(bra,2),int(ket,2)]=np.exp(phi*1j)
        else:
            ret[int(bra,2),int(ket,2)]=1.
    return ret
    
def initState_basis(ket):
    return StateToVec([(1,ket[1:-1])])
def initState_file(filename):
    ret=[]
    with open('circuits/'+filename,'r') as infile:
        for line in infile.readlines():
            (re,im)=line.split()
            ret.append(float(re)+float(im)*1j)
    return np.array(ret)

def initState(kind, param):
    if kind=='FILE':
        return initState_file(param)
    else:
        return initState_basis(param)


