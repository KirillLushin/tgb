import numpy as np
import matplotlib.pyplot as plt


data = np.genfromtxt(r"", delimiter="\t")

FD = 2e+4
x = data[:, 0]
y = data[:, 1]

for i in range(5):
    x = np.append(x, x+x[-1])
    y = np.append(y, y)

N = len(y)

'''N = 4000
x = np.array([np.sin(2.*np.pi*2000.0*t/FD)+np.sin(2.*np.pi*4000.0*t/FD) for x in range(N)])
y = np.arange(N)/FD'''

spectrum = np.fft.rfft(y)

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
ax1.plot(x, y)
ax1.set_xlim(left=0, right=x[-1])
ax1.grid()
ax2.plot(np.fft.rfftfreq(N, 1./FD), np.abs(spectrum)/N)
ax2.set_xlim(left=0, right=200)
ax2.set_xlabel('Частота')
ax2.set_ylabel('Амплитуда')
plt.tight_layout()

fig, ax = plt.subplots()
f, t, Zxx = signal.stft(y, FD, nperseg=1000)
plt.pcolormesh(t, f, np.abs(Zxx))
plt.ylabel('Частота, Гц')
plt.xlabel('Время, с')
plt.tight_layout()

plt.show()
