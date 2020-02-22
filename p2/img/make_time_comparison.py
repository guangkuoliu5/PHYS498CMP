import numpy as np
import matplotlib.pyplot as plt
ax=np.linspace(5,12,8)
ay=[0.65,0.76,1.05,1.07,3.3,18.5,126.7,967]
bx=ax.copy()
by=[0.628,0.643,0.7,0.830,1.544,4.681,16.697,79.8]
cx=[i for i in range(5,13)]+[20]
cy=[0.865,0.949,1,1.045,1.142,1.242,1.37,1.685,100]
Ix=cx.copy()
Iy=[0.67,0.675,0.617,0.616,0.616,0.620, 0.648,0.713,16.68]

plt.plot(ax,ay, 'o-', label='Simulator Ia')
plt.plot(bx,by, 'o-', label='Simulator Ib')
plt.plot(cx,cy, 'o-', label='Simulator Ic')
plt.plot(Ix,Iy, 'o-', label='Simulator II')
plt.xlabel('number of qubits')
plt.ylabel('time (seconds)')
plt.title('Comparison of Time Consumption between the Simulators')
plt.legend()
#plt.show()
plt.savefig('time.png', dpi=300)

