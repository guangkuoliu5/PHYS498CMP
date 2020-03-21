import numpy as np
L=27
###not cg###
alist=[]
for i in range(999999):
    A=np.random.randint(0,2,(L,L))*2-1
    alist.append((np.sum(A)/(L*L))**2)
print(np.mean(np.array(alist)))
###cg######
'''
blist=[]
for i in range(9999):
    A=np.random.randint(0,2,(L*3,L*3))*2-1
    B=[]
    for i in range(0,L*3,3):
        B.append([])
        for j in range(0,L*3,3):
            s=0
            for ii in range(i,i+3):
                for jj in range(j,j+3):
                    s+=A[ii,jj]
            B[-1].append(s/abs(s))
    blist.append((np.sum(B)/(L*L))**2)
print(np.mean(np.array(blist)))
                    
'''
