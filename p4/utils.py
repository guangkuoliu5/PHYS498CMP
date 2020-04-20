import numpy as np
import matplotlib.pyplot as plt
def matshowstr(s):
    l=[]
    for i in range(10):
        l.append([])
        for j in range(10):
            l[-1].append(int(s[i*10+j]))
    plt.matshow(l)
def str2int(s):
    return int(s,2)
def int2str(i, size=6):
    return bin(i)[2:].zfill(size)
def int2state(i, size=6):
    s=int2str(i,size=size)
    return np.array([int(c)*2-1 for c in s])
def state2int(s):
    return str2int(''.join(['0' if c==-1 else '1' for c in s]))
def flip(s, i):
    if s[i]=='0':
        return s[:i]+'1'+s[i+1:]
    else:
        return s[:i]+'0'+s[i+1:]
def flipint(i, f,size):
    return str2int(flip(int2str(i,size),f))
        

'''
matshowstr('0000000000000000010000000000000000000000000000000000000000000000010000000000100000000001100000000001')
matshowstr('0000000000000000010000000000000000000000000000000000000000000001010000001000100000000001101000000001')
matshowstr('0000000000000100010000000000000000000000000010000000000000000001110000001000100001000001101000000001')
plt.show()
'''
