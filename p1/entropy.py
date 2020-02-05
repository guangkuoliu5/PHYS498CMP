import numpy as np
import sys
import matplotlib.pyplot as plt
import gzip
xarr=[]
yarr=[]
step=1
for i in range(0,10001, step):
    with open('data/'+str(i).zfill(5)+'.txt','r') as infile:
        xarr.append(i)
        yarr.append(sys.getsizeof(gzip.compress(bytes(infile.read(), 'utf-8'))))
xarr=np.array(xarr)
yarr=np.array(yarr)
#print(len(yarr[int(8000/step):]))
aveH=np.average(yarr[int(8000/step):])
y2arr=np.array([aveH for i in range(0,10001,step)])
plt.plot(xarr,yarr, 'c-')
plt.plot(xarr,y2arr, 'r-')
plt.xlabel("Sweeps")
plt.ylabel("Number of Compressed Bits")
plt.title("Entropy vs. Sweeps")
plt.xticks(range(0,10001,2000))
plt.yticks(np.linspace(min(yarr), max(yarr),10))
plt.show()
plt.savefig('img/entropy.png', dpi=300)
plt.close()

