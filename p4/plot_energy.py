import numpy as np
import matplotlib.pyplot as plt
dat=np.loadtxt('energy.dat')
for line in dat:
    plt.plot(range(len(line)), line,'o-', lw=0.5, ms=1.3)
plt.xlabel('Steps/100')
plt.ylabel('Energy')
plt.title('Energy vs Step in Hopfield Network')
plt.savefig('img/energygoesdown.png',dpi=300)
plt.close()
