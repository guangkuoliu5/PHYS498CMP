import numpy as np
import matplotlib.pyplot as plt
def matshowstr(s):
    l=[]
    for i in range(10):
        l.append([])
        for j in range(10):
            l[-1].append(int(s[i*10+j]))
    plt.matshow(l)
'''
matshowstr('0000000000000000010000000000000000000000000000000000000000000000010000000000100000000001100000000001')
matshowstr('0000000000000000010000000000000000000000000000000000000000000001010000001000100000000001101000000001')
matshowstr('0000000000000100010000000000000000000000000010000000000000000001110000001000100001000001101000000001')
plt.show()
'''
