import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
def fromInt(i, Lx=3, Ly=3):
    bi=bin(i)[2:].zfill(Lx*Ly)
    ret=np.zeros((Ly,Lx))
    for i in range(Ly):
        for j in range(Lx):
            ret[i][j]=int(bi[i*Ly+j])*2-1
    return ret
def toInt(config):
    ret=''
    for line in config:
        for spin in line:
            if spin==-1:
                ret+='0'
            else:
                ret+='1'
    return int(ret,2)

def Energy(config):
    (h,w)=config.shape
    ret=0
    for i in range(h):
        for j in range(w):
            ret=ret-config[i,j]*config[i-1,j]-config[i,j]*config[i,j-1]
    return ret
def createhist3x3(freq):
    beta=0.3
    histfilename='img/3x3'+datetime.now().strftime('%m%d_%H%M')+'.png' 
    fig, ax=plt.subplots()
    allstates=range(len(freq))
    errfreq=np.sqrt(freq)/np.sum(freq)
    freq=freq/np.sum(freq)
    bars=ax.errorbar(allstates, freq, errfreq, fmt='none', ecolor='r', label='Error Bars')
    bars=ax.bar(allstates, freq, label='Simulated Frequency')
    p=np.array([np.exp(-beta*Energy(fromInt(i))) for i in allstates])
    p=p/np.sum(p)
    ax.plot(allstates, p, 'g--',linewidth=0.5, label='Expected Curve')
    ax.set_xlabel("Spin configurations as binary number")
    ax.set_ylabel("Probability distribution")
    ax.set_title("Results of Monte Carlo on 3x3 grid")
    ax.legend()
    fig.tight_layout()
    fig.savefig(histfilename, dpi=300)
    return histfilename




