import numpy as np
import matplotlib.pyplot as plt
############filter#########
def H(f):
	s=1j*2*np.pi*f
	den=1+s*C*R
	H=1/den
	return H
########### Time DOmain ############
t=np.linspace(0,4*np.pi,1000)
plt.subplot(311)
plt.plot(t,np.cos(t),label='input cosine wave')
plt.grid()
plt.xlabel('$Time$')
plt.ylabel('$amplitude$')
########## parameters ##########
R=500
C=10e-6
f0=50
f=np.linspace(-3*f0,3*f0,1e2)
######### Maginitude Response ########
plt.subplot(312)
plt.plot(f,abs(H(f)))
plt.grid()
plt.xlabel('$freq$')
plt.ylabel('$H(f)$')

############ Phase Response ###################
plt.subplot(313)
phase=np.angle(H(f),deg=True)
plt.plot(f,phase,label='phase')
plt.xlabel('$freq$')
plt.ylabel('$angle H(f)$')
plt.legend()
plt.grid()
plt.show()

