import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
from datetime import datetime
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
            outstring=outstring+'+ ({0:.12f}) |{1}> '.format(a,s)
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
            outstring=outstring+'+ ({0:.12f}) |{1}> '.format(a,s)
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
def tensorMe_sparse(listOfMatrices):
    ret=listOfMatrices[0]
    for M in listOfMatrices[1:]:
        ret=sparse.kron(ret,M)
    return ret

def HadamardArray(i,k):
    r=np.sqrt(0.5)
    listOfMatrices=[np.eye(2) if (i!=j) else np.array([[r,r],[r,-r]]) for j in range(k) ] 
    return tensorMe(listOfMatrices)
def HadamardArray_sparse(i,k):
    r=np.sqrt(0.5)
    listOfMatrices=[sparse.csr_matrix(np.eye(2)) if (i!=j) else sparse.csr_matrix(np.array([[r,r],[r,-r]])) for j in range(k) ] 
    return tensorMe_sparse(listOfMatrices)

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
def CNOTArray_sparse(c, t, n):
    size=2**n
    row=[]
    col=[]
    data=[]
    for i in range(size):
        bra=bin(i)[2:].zfill(n)
        ket=bra
        if bra[c]=='1':
            ket=bra[:t]+str(1- int(bra[t]))+bra[t+1:]
        row.append(int(bra,2))
        col.append(int(ket,2))
        data.append(1+0j)
    return sparse.csr_matrix((data,(row,col)), shape=(size,size))

def PArray(i,k,phi):
    listOfMatrices=[np.eye(2) if (i!=j) else np.array([[1,0],[0,np.exp(phi*1j)]]) for j in range(k)]
    return tensorMe(listOfMatrices)
def PArray_sparse(i,k,phi):
    listOfMatrices=[sparse.csr_matrix(np.eye(2)) if (i!=j) else sparse.csr_matrix(np.array([[1,0],[0,np.exp(phi*1j)]])) for j in range(k)]
    return tensorMe_sparse(listOfMatrices)

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

def measure(stateVec, numTrials=100):
    n=len(stateVec)
    result=np.zeros(n)
    dist=np.square(np.absolute(stateVec))
    for i in range(numTrials):
        shot=np.random.choice(range(n), p=dist)
        result[shot]+=1
    return result

def createHist(result,annotate=True):
    histfilename='img/result_'+datetime.now().strftime('%m%d_%H%M')+'.png'
    fig, ax=plt.subplots()
    allstates=range(len(result))
    numQubits=int(np.log2(len(result)))
    bars=ax.barh(allstates,result)
    ax.set_yticks(allstates)
    ax.set_yticklabels(['|{}>'.format(bin(i)[2:].zfill(numQubits)) for i in allstates])
    ax.set_ylabel('States')
    ax.set_xlabel('Frequencies')
    ax.set_xlim(0,result.max()*1.2)
    ax.set_title('Result of {} Measurements'.format(int(np.sum(result))))
    if annotate:
        for bar in bars:
            w=int(bar.get_width())
            ax.annotate(str(w),
                    xy=(w,bar.get_y()+bar.get_height()/2),
                    xytext=(1,0),
                    textcoords='offset points',
                    ha='left', va='center')
    plt.xticks(rotation=45)
    fig.tight_layout()
    fig.savefig(histfilename, dpi=300)
    return histfilename
