import matplotlib.pyplot as plt #modulo para graficar
import sounddevice as sd #modulo para grabar audio
import soundfile as sf #modulo para abrir archivo audio
from scipy.io.wavfile import write #modulo para guardar audio
import numpy as np
import os
os.system('clear')
fs = 44100
seconds = 2
'''
#Grabar audio
print('Grabando...')
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
print('Grabado'); print('Guardando...')
#Guarda el audio
write('Grabacion.wav', fs, myrecording)
print('Guardado')

'''
#Abre archivo de audio
y,fs = sf.read('Grabacion.wav')
Longy = len(y)
Diftime = seconds/Longy;
Freq = 1/Diftime;
#time = 0:Diftime:seconds-Diftime;
time = np.arange(0, seconds, Diftime).tolist()
#Longtime = len(time);
print(len(y))
print(len(time))

#Reproduce audio
sd.play(y*20)

#Grafica la señal de audio
#plt.plot(y, label = 'y')
plt.plot(time, y, label = 'time vs y', linewidth=0.5)
plt.legend()
plt.grid(color='k', linestyle='--', linewidth=0.5)
plt.show()