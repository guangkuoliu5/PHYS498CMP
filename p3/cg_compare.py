import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import stats
from scipy.interpolate import InterpolatedUnivariateSpline
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

plt.errorbar(betalist_cg, ave_cgM, yerr=err_cgM, fmt='g-.', linewidth=0.5,ecolor='r', elinewidth=2.0,label='Coarse Grained')
plt.errorbar(betalist, aveM, yerr=errM, fmt='y-.', linewidth=0.5,ecolor='r', elinewidth=2.0,label='Native')
plt.plot([0],[0.00136], 'bo', label='Testing')
plt.xlabel(r'$\beta$')
plt.ylabel(r'$\langle M^2 \rangle$')
plt.legend()
plt.title(r'$\langle M^2 \rangle$'+' vs '+r'$\beta$')
plt.savefig('img81/M2vsbeta_compare.png',dpi=300)
plt.close()

