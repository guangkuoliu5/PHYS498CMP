import numpy as np
import sys
def _get_QFT(n):
    if n==1 :
        return 'H 0\n'
    ret=_get_QFT(n-1)
    for t in range(0, n-1):
        ret+='CPHASE {} {} {}\n'.format(n-1, t, np.pi/(2**(n-t-1))) 
    ret+='H {}\n'.format(n-1)
    return ret

def get_QFT(n, initstate=False, withreverse=True):
    ret=str(n)+'\n'
    if initstate:
        ret+='INITSTATE FILE myInputState\n'
    ret+=_get_QFT(n)
    if withreverse:
        for i in range(int(np.ceil((n-1)/2))): #4->2 5->2
            ret+='SWAP {} {}\n'.format(i, n-1-i)
    return ret
def get_QFT_inv(n):
    ret=''
    for i in range(int(np.ceil((n-1)/2))): #4->2 5->2
        ret+='SWAP {} {}\n'.format(i, n-1-i)
    lines=_get_QFT(n).split('\n')
    for i in range(len(lines)-1, -1, -1):
        if len(lines[i])<1:
            continue
        words=lines[i].split()
        if words[0]=='H':
            ret+=lines[i]+'\n'
        elif words[0]=='CPHASE':
            ret+='CPHASE {} {} {}\n'.format(words[1], words[2], -float(words[3]))
    return ret

#print(get_QFT(3))

#print('n=3:')
#print(get_QFT(3))
#print('n=5:')
#print(get_QFT(5))
if len(sys.argv)>1:
    n=int(sys.argv[1])
    with open('QFT/QFT{}.circuit'.format(n), 'w') as out:
        out.write(get_QFT(n, initstate=True))




