import numpy as np
from utils import *
import matplotlib.pyplot as plt
inFile=open('3x3.out', 'r')
freq=np.zeros(2**9)
for line in inFile.readlines():
    (i,f)=line.split()
    freq[int(i)]=int(f)
createhist3x3(freq)
