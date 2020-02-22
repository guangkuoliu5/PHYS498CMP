import numpy as np
import matplotlib.pyplot as plt
ax=[10,11,12]
ay=[45,47,819]
bx=ax.copy()
by=[42,45,300]
cx=[11,12,20]
cy=[30,39,100]
Ix=[12,20]
Iy=[20,37]

plt.plot(ax,ay, 'o-', label='Simulator Ia')
plt.plot(bx,by, 'o-', label='Simulator Ib')
plt.plot(cx,cy, 'o-', label='Simulator Ic')
plt.plot(Ix,Iy, 'o-', label='Simulator II')
plt.xlabel('number of qubits')
plt.ylabel('memory usage (MB)')
plt.title('Comparison of Memory Consumption between the Simulators')
plt.legend()
#plt.show()
plt.savefig('memory.png', dpi=300)

