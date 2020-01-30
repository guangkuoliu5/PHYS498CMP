from utils import *
import sys
import numpy as np
with open(sys.argv[1],'r') as circuit:
    numQubit=int(circuit.readline())
    for line in circuit.readlines():
        gate=line.split()[0]
        if gate=='INITSTATE':

