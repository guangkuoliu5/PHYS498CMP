import numpy as np
import matplotlib.pyplot as plt
import os
for inFileName in os.listdir('27data/'):
    if inFileName[0]!='s': continue
    beta=float(inFileName.split('_')[1])
    with open('27data/'+inFileName, 'r') as inFile:
        outFileName='img/snapshot_'+str(beta)+'.png'
        A=[ [int(i) for i in line.split()] for line in inFile.readlines()]
        plt.matshow(A)
        plt.title('beta='+str(beta))
        plt.savefig(outFileName)


    
