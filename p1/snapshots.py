import matplotlib.pyplot as plt
import numpy as np
for i in range(0,10001,500):
    dataname='data/'+str(i).zfill(5)+'.txt'
    with open(dataname, 'r') as infile:
        arr=np.array([np.array([int(x) for x in row.split()]) for row in infile.readlines()])
        plt.matshow(arr)
        plt.savefig('img/'+str(i).zfill(5)+'.png', dpi=300)
        plt.close()
