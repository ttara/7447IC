import numpy as np
import matplotlib.pyplot as plt
############filter#########
f0=50
def H(f):
	s=1j*2*np.pi*f
	den=1+s*C*R
	H=1/den
	return H
########### Time DOmain ############
t=np.linspace(-50e-3,50e-3,1000)
plt.subplot(211)
plt.plot(t,np.cos(2*np.pi*f0*t),label='input cosine wave')
plt.grid()
plt.xlabel('$t $')
plt.ylabel('$amplitude of x(t)$')
########## parameters ##########
R=500
C=10e-6

f=np.linspace(-3*f0,3*f0,1e2)

############ y(t) ###################
plt.subplot(212)
phase=np.angle(H(f0),deg=False)
y=abs(H(f0))*np.cos(2*np.pi*f0*t+phase)

plt.plot(t,y,label='phase')
plt.xlabel('$t $')
plt.ylabel('$amplitude y(t)$')
plt.legend()
plt.grid()
plt.show()

