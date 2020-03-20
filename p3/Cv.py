import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import stats
from scipy.interpolate import InterpolatedUnivariateSpline
dataFolder='27data1/'
L=27
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
        print("beta={}, E={}, errE={}, M={}, errM={}".format(beta, aveE[-1], errE[-1], aveM[-1], errM[-1]))

betalist,aveM,errM=zip(*sorted(zip(betalist,aveM,errM)))
plt.errorbar(betalist, aveM, yerr=errM, fmt='g-.', linewidth=0.5,ecolor='r', elinewidth=2.0)
plt.xlabel(r'$\beta$')
plt.ylabel(r'$\langle M^2 \rangle$')
plt.title(r'$\langle M^2 \rangle$'+' vs '+r'$\beta$')
plt.savefig('img/M2vsbeta1.png',dpi=300)
plt.close()

Tlist,aveE=zip(*sorted(zip(1/np.array(betalist)[1:],aveE[1:])))
#spl = InterpolatedUnivariateSpline(Tlist, aveE, k=2).derivative()
#x=np.linspace(1,10,1000)
#plt.plot(x, spl(x), 'r')
dTdE=[]
Tlist1=[]
for i in range(1,len(Tlist)-1):
    Tlist1.append(Tlist[i])
    dTdE.append((Tlist[i+1]-Tlist[i-1])/(aveE[i+1]-aveE[i-1]))
    
x,y=zip(*sorted(zip(1/np.array(Tlist1),1/np.array(dTdE))))
plt.plot(x, y, 'r')
plt.axvline(x[np.argmax(y)], color='g', label='Transition Temperature\n at '+ r'$\beta={}$'.format(x[np.argmax(y)]))
plt.xlim(-0.02,1.02)
plt.legend()
plt.xlabel(r'$\beta$')
plt.ylabel(r'$C_v$')
plt.title(r'$C_v=\frac{\partial E}{\partial (1/\beta)}$'+' vs '+r'$\beta$')
plt.savefig('img/Cv.png',dpi=300)
plt.close()


