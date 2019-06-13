import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
f01=50
f02=150
t=np.linspace(-10e-3,10e-3,1000)
Fs=1000
w=np.linspace(0,2*np.pi,1000)
############filter#########
z=np.exp(-1*1j*w)
alpha=0.9
beta=np.cos((2*np.pi*f02)/Fs)
print(beta)
def H(z):
	num=1-(2*beta*z)+(z**2)
	den=1-(beta*(1+alpha)*z)+(alpha*(z**2))
	N_D=num/den
	K=(N_D*(1+alpha))/2
	return K

plt.subplot(511)
plt.plot(t,np.cos(2*np.pi*f01*t)+np.cos(2*np.pi*f02*t))
plt.grid()
plt.xlabel('$t $')
plt.ylabel('$amplitude)$')
plt.title('input two sinusoidal signals')
#############################
plt.subplot(514)
plt.plot(t,np.cos(2*np.pi*f01*t),label='waveform with 50 hz')
plt.grid()
plt.xlabel('$t $')
plt.ylabel('$amplitude$')
plt.title('individual signal')
###################IIR Filter #################
plt.subplot(512)
new_arr_x=(w*Fs)/(2*np.pi)
new_arr_y=abs(H(z))
plt.plot(new_arr_x[0:250],new_arr_y[0:250],label='notch filter')
plt.grid()
plt.xlabel('$ freq $')
plt.ylabel('$ |H(z)| $')
plt.title('band stop filter')
############# Reconstruction original signal ############

z1=np.exp((-1*1j*2*np.pi*f01)/Fs)
z2=np.exp((-1*1j*2*np.pi*f02)/Fs)
Y=abs(H(z1))*np.cos(2*np.pi*f01*t+np.angle(H(z1),deg=False))+abs(H(z2))*np.cos(2*np.pi*f02*t+np.angle(H(z1),deg=False))
plt.subplot(513)
plt.plot(t,Y,label='recovered 50 hz signal from mixed signal ')
plt.grid()
plt.xlabel('$t $')
plt.ylabel('$ amplitude$')
plt.title('Recoverd signal')
################################
plt.subplot(515)
plt.plot(t,np.cos(2*np.pi*f02*t),label='waveform with 150 hz')
plt.grid()
plt.xlabel('$t $')
plt.ylabel('$amplitude$')
plt.title('individual signal')

plt.show()

