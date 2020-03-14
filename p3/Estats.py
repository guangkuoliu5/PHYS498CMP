import numpy as np
import matplotlib.pyplot as plt
import sys
Elist=[]
Mlist=[]
with open(sys.argv[1], 'r') as inFile:
    for line in inFile.readlines():
        (E,M)=line.split()
        Elist.append(float(E)); Mlist.append(float(M))



plt.plot(range(len(Elist)),Elist)
plt.show()
