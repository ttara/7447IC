import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
f01=50
f02=150
sampleRate=16000
length=20e-3
t=np.linspace(-10e-3,10e-3,sampleRate*length)
R=500
C=10e-6


############filter#########
f0=50
def H(f):
	s=1j*2*np.pi*f
	den=1+s*C*R
	H=1/den
	return H
########### Time DOmain ############
hand=plt.figure()
plt.subplot(211)
plt.plot(t,np.cos(2*np.pi*f01*t)+np.cos(2*np.pi*f02*t))
hand.savefig('input_mixed_signals.pdf')
plt.grid()
plt.xlabel('$t $')
plt.ylabel('$amplitude of x(t)$')
plt.title('input two sinusoidal signals')
input_2=np.cos(2*np.pi*f01*t)+np.cos(2*np.pi*f02*t)
wavfile.write('mixed_signals_input.wav',sampleRate,input_2/max(abs(input_2)))
phase1=np.angle(H(f01),deg=False)
phase2=np.angle(H(f02),deg=False)
y=abs(H(f01))*np.cos(2*np.pi*f01*t+phase1)+abs(H(f02))*np.cos(2*np.pi*f02*t+phase2)
wavfile.write('mixed_signals_output.wav',sampleRate,y/max(abs(y)))
print(len(y))
###############
f=open('input_two_sinusoida_signals.txt','w')
input_2=input_2/max(abs(input_2))
for i in input_2:
	print i
	f.write(str(int(127+127*i))+str(","))
	#f.write(np.asarray(input_2))
f.close()
f=open('mixed_signals_output.txt','w')
y=y/max(abs(y))
for i in y:
	print i
	f.write(str(int(127+127*i))+str(","))
f.close()
#################

x=plt.figure()
plt.subplot(212)

plt.plot(t,y)
x.savefig('mixed_signals_output.pdf')
plt.grid()
plt.xlabel('$t $')
plt.ylabel('$amplitude of x(t)$')
plt.title('output after passing through low pass filter')
plt.show()
