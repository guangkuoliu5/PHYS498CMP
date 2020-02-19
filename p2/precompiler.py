import numpy as np
import sys
def get_not(i):
    return 'H {0}\nP {0} {1}\nH {0}\n'.format(i, np.pi)

def get_Rz(i, theta):
    ret='P {0} {1}\n'.format(i, theta/2)
    ret+=get_not(i)
    ret+='P {0} {1}\n'.format(i, -theta/2)
    ret+=get_not(i)
    return ret

def get_CRz(c, t, theta):
    ret='P {} {}\n'.format(t, theta/2)
    ret+='CNOT {} {}\n'.format(c, t)
    ret+='P {} {}\n'.format(t, -theta/2)
    ret+='CNOT {} {}\n'.format(c, t)
    return ret

def get_CP(c, t, theta):
    ret='P {} {}\n'.format(c, theta/2)
    ret+=get_CRz(c, t, theta)
    return ret

def get_SWAP(n, m):
    ret='CNOT {} {}\n'.format(n,m)
    ret+='CNOT {} {}\n'.format(m,n)
    ret+='CNOT {} {}\n'.format(n,m)
    return ret
#print(get_CP(0,1,0.3))
def precompile(filename):
    with open(filename, 'r') as rawcircuit:
        with open(filename+'.compiled', 'w') as outcircuit:
            for line in rawcircuit.readlines():
                if line[0]=='#':
                    continue
                words=line.split()
                gate=words[0]
                if gate=='NOT':
                    outcircuit.write(get_not(int(words[1])))
                elif gate=='Rz':
                    outcircuit.write(get_Rz(int(words[1]), float(words[2])))
                elif gate=='CRz':
                    outcircuit.write(get_CRz(int(words[1]), int(words[2]), float(words[3])))
                elif gate=='CPHASE':
                    outcircuit.write(get_CP(int(words[1]), int(words[2]), float(words[3])))
                elif gate=='SWAP':
                    outcircuit.write(get_SWAP(int(words[1]), int(words[2])))
                else:
                    outcircuit.write(line)

if len(sys.argv)>=2:
    precompile(sys.argv[1])
