import matplotlib.pyplot as plt
import soundfile as sf

import sounddevice as sd
from scipy.io.wavfile import write


fs = 44100  # Sample rate
seconds = 3  # Duration of recording
print('Grabando...')
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
print('Grabado'); print('Guardando...')
write('Grabacion.wav', fs, myrecording)  # Save as WAV file 
print('Guardado')


#fs=44100
y,fs =sf.read('Grabacion.wav')

sd.play(y*20)


plt.plot(y)
plt.show()