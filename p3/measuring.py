import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import stats
from scipy.interpolate import UnivariateSpline
dataFolder='27data/'
L=27
startIndex=200
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
    if beta==0:
        Elist_test=[]
        for i in range(5000):
            config=np.random.randint(0,2,(L,L))*2-1
            Elist_test.append((np.sum( np.multiply(np.roll(config,1, axis=0), config)  )
                    +np.sum(np.multiply(np.roll(config,1, axis=1), config)  ))/(L*L))
        plt.hist([Elist_test, Elist],15, weights=[np.ones_like(Elist_test)/float(len(Elist_test)),np.ones_like(Elist)/float(len(Elist))], label=['testing', 'Monte Carlo'])
        print('testing E for beta=0', np.mean(np.array(Elist_test)))
    elif beta>99:
        Elist_test=[-2]
        plt.hist([Elist_test, Elist],15, weights=[np.ones_like(Elist_test)/float(len(Elist_test)),np.ones_like(Elist)/float(len(Elist))], label=['testing', 'Monte Carlo'])
    else:
        plt.hist(Elist,15, weights=np.ones_like(Elist)/float(len(Elist)), label='Monte Carlo')
    (mean, variance, error, ac)=stats.Stats(np.array(Elist))
    plt.axvline(mean, color='r', label='<E>')
    plt.legend()
    plt.title('Energy Probability Histogram at beta='+str(beta))
    plt.savefig('img/Ehist'+str(beta)+'.png', dpi=300)
    plt.close()
    if beta<99:
        aveE.append(mean); errE.append(error); betalist.append(beta);
    #############M plot############
    if beta==0:
        Mlist_test=[]
        for i in range(5000):
            config=np.random.randint(0,2,(L,L))*2-1
            Mlist_test.append((np.sum(config)/(L*L))**2)
        plt.hist([Mlist_test, Mlist],15, weights=[np.ones_like(Mlist_test)/float(len(Mlist_test)),np.ones_like(Mlist)/float(len(Mlist))], label=['testing', 'Monte Carlo'])
        print('testing M for beta=0', np.mean(np.array(Mlist_test)))
    elif beta>99:
        Mlist_test=[1]
        plt.hist([Mlist_test, Mlist],15, weights=[np.ones_like(Mlist_test)/float(len(Mlist_test)),np.ones_like(Mlist)/float(len(Mlist))], label=['testing', 'Monte Carlo'])
    else:
        plt.hist(Mlist,15, weights=np.ones_like(Mlist)/float(len(Mlist)), label='Monte Carlo')
    (mean, variance, error, ac)=stats.Stats(np.array(Mlist))
    plt.axvline(mean, color='r', label=r'$<M^2>$')
    plt.legend()
    plt.title('Total Magnetization Probability Histogram at beta='+str(beta))
    plt.savefig('img/Mhist'+str(beta)+'.png', dpi=300)
    plt.close()
    if beta<99:
        aveM.append(mean); errM.append(error);
        print("beta={}, E={}, errE={}, M={}, errM={}".format(beta, aveE[-1], errE[-1], aveM[-1], errM[-1]))

betalist,aveM,errM=zip(*sorted(zip(betalist,aveM,errM)))
plt.errorbar(betalist, aveM, yerr=errM, fmt='g-.', linewidth=0.2,ecolor='r', elinewidth=2.0)
plt.xlabel(r'$\beta$')
plt.ylabel(r'$\langle M^2 \rangle$')
plt.title(r'$\langle M^2 \rangle$'+' vs '+r'$\beta$')
plt.savefig('img/M2vsbeta.png',dpi=300)
plt.close()

#Tlist,aveE=zip(*sorted(zip(1/np.array(betalist)[1:],aveE[1:])))
spl = UnivariateSpline(betalist, aveE)
x=np.linspace(0,1,1000)
plt.plot(x, spl(x), 'r')
plt.plot(betalist, aveE, 'bo')
plt.xlabel(r'$T=1/\beta$')
plt.ylabel(r'$\langle E \rangle$')
plt.title(r'$C_v=\frac{\partial E}{\partial (1/\beta)}$'+' vs '+r'$T$')
plt.savefig('img/Cv.png',dpi=300)
plt.close()


