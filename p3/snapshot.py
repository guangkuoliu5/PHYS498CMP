import numpy as np
import matplotlib.pyplot as plt
import os
for inFileName in os.listdir('81data_cgcg/'):
    if inFileName[0]!='s': continue
    beta=float(inFileName.split('_')[1])
    with open('81data_cgcg/'+inFileName, 'r') as inFile:
        outFileName='img81/snapshot_cgcg_'+str(beta)+'.png'
        A=[ [int(i) for i in line.split()] for line in inFile.readlines()]
        plt.matshow(A)
        plt.title('beta='+str(beta))
        plt.savefig(outFileName)
        plt.close()


    
