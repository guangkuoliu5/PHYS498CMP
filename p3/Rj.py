import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import stats
from scipy.interpolate import interp1d,UnivariateSpline
#### cg #######
dataFolder_cg='81data_cg/'
startIndex=1000
ave_cgE=[]
ave_cgM=[]
err_cgE=[]
err_cgM=[]
betalist_cg=[]
for inFileName in sorted(os.listdir(dataFolder_cg)):
    ###########read data#############
    if inFileName[0]!='o': continue
    beta=float(inFileName.split('_')[-1])
    Elist=[]
    Mlist=[]
    with open(dataFolder_cg+inFileName, 'r') as inFile:
        for line in inFile.readlines()[startIndex:]:
            (E,M)=line.split()
            Elist.append(float(E)); Mlist.append(float(M))
    ########E plot##########
    (mean, variance, error, ac)=stats.Stats(np.array(Elist))
    if beta<99:
        ave_cgE.append(mean); err_cgE.append(error); betalist_cg.append(beta);
    #############M plot############
    (mean, variance, error, ac)=stats.Stats(np.array(Mlist))
    if beta<99:
        ave_cgM.append(mean); err_cgM.append(error);
        #if beta==0:
            #print("beta={}, E={}, err_cgE={}, M={}, err_cgM={}".format(beta, ave_cgE[-1], err_cgE[-1], ave_cgM[-1], err_cgM[-1]))
##### native #########
dataFolder='27data1/'
startIndex=1000
aveE=[]
aveM=[]
errE=[]
errM=[]
betalist=[]
for inFileName in sorted(os.listdir(dataFolder)):
    ###########read data#############
    if inFileName[0]!='o': continue
    beta=float(inFileName.split('_')[-1])
    Elist=[]
    Mlist=[]
    with open(dataFolder+inFileName, 'r') as inFile:
        for line in inFile.readlines()[startIndex:]:
            (E,M)=line.split()
            Elist.append(float(E)); Mlist.append(float(M))
    ########E plot##########
    (mean, variance, error, ac)=stats.Stats(np.array(Elist))
    if beta<99:
        aveE.append(mean); errE.append(error); betalist.append(beta);
    #############M plot############
    (mean, variance, error, ac)=stats.Stats(np.array(Mlist))
    if beta<99:
        aveM.append(mean); errM.append(error);
        #if beta==0:
            #print("beta={}, E={}, errE={}, M={}, errM={}".format(beta, aveE[-1], errE[-1], aveM[-1], errM[-1]))


betalist_cg=np.array(betalist_cg)
ave_cgM=np.array(ave_cgM)
bjnative=interp1d(aveM, betalist,kind='linear',bounds_error=0 )
#plt.plot(betalist,aveM, 'bo',alpha=0.5,label='beta vs M')
#plt.plot(betalist_cg,ave_cgM, 'ro',alpha=0.5,label='beta vs M')
#plt.plot(bjnative(aveM),aveM, 'b-',label='beta vs M')
plt.plot(betalist_cg, bjnative(ave_cgM),'r-',alpha=0.5,label=r'$R(J)$')
plt.plot(betalist_cg, betalist_cg, 'g--', label=r'$y=x$')
plt.ylim(0,1)
crT=betalist_cg[np.argmin(abs(np.array(betalist_cg)-np.array(bjnative(ave_cgM)))[40:50])+40]
print(abs(np.array(betalist_cg)-np.array(bjnative(ave_cgM))))
print((abs(np.array(betalist_cg)-np.array(bjnative(ave_cgM)))[40:50]))
print(np.argmin(abs(np.array(betalist_cg)-np.array(bjnative(ave_cgM)))[40:50]))
print(crT)
###########arrows################
rjspline=UnivariateSpline(betalist_cg[3:60], bjnative(ave_cgM[3:60]))
#print(rjspline(betalist_cg))
#plt.plot(betalist_cg,rjspline(betalist_cg), 'r-.')
plt.plot([0.44],[rjspline(0.44)], 'bo')
J=[0.43, 0.45]
for jj in J:
    j=jj
    for i in range(5):
        rj=rjspline(j)
        plt.arrow(j,rj,rj-j,rjspline(rj)-rj,head_width=0.01)
        print(j,rj)
        j=rj


plt.xlabel(r'$J$')
plt.ylabel(r'$R(J)$')
plt.legend()
plt.title(r'$R(J)$'+' vs '+r'$J$')
plt.savefig('img81/Rj2.png',dpi=300)
plt.close()

k=rjspline.derivative()(0.44)
print(1/(np.log(k)/np.log(3)))
