import numpy as np
import matplotlib.pyplot as plt
########### Time DOmain ############
t=np.linspace(-50e-3,50e-3,1000)
plt.plot(t,np.cos(100*np.pi*t),label='input cosine wave')
plt.grid()
plt.xlabel('$Time $')
plt.ylabel('$amplitude$')
plt.show()
