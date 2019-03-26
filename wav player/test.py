import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
import matplotlib as mplot

rate, data = wav.read('Summers.wav')
print(data)
#a = data.T[0]
#b = [(ele/2**8.)*2-1 for ele in a]
#c = fft(b)
#d = len(c)
N=10
fdata = fft(data)/N
nyquist = rate/2
frequencies = np.linspace(0, nyquist, N/2+1)
ydata = np.abs(fdata[10000:10006])
print(ydata)


plt.plot(frequencies, ydata)
plt.show()

#matplotlib inline
#plt.plot(data, np.abs(c))
#plt.show()