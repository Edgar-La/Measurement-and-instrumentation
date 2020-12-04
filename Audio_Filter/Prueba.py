import matplotlib.pyplot as plt #modulo para graficar
import sounddevice as sd #modulo para grabar audio
import soundfile as sf #modulo para abrir archivo audio
from scipy.io.wavfile import write #modulo para guardar audio
from scipy.fft import fft, ifft, fftshift
from scipy.signal import butter, filtfilt
import numpy as np
from math import pi
from time import sleep
import os
#os.system('clear')

############################################################################################################
#Seccion de funciones
def nextpow2(Longy):
	pot = 0
	while 2**pot <= Longy:
		NePw = 2**pot
		pot+=1
	return (pot)

############################################################################################################
fs = 44100
#seconds = 9
'''
#Grabar audio
print('Grabando...')
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
print('Grabado'); print('Guardando...')
#Guarda el audio
write('Grabacion_E.wav', fs, myrecording)
print('Guardado')
y,fs = sf.read('Grabacion_E.wav')
'''

#Abre archivo de audio
y,fs = sf.read('CRACK1.wav')
Longy = len(y)
#Diftime = seconds/Longy;
seconds = Longy/fs
Diftime = 1/fs
time = np.arange(0, seconds, Diftime).tolist()
#Reproduce audio
'''
sd.play(y*50);
sd.wait()
sd.wait()
sd.wait()'''
#-------------------------------------------------------------------------
# FFT de la señal de audio (RADIOGRAFÍA DE LA SEÑAL)
AudioAnalysis = 2**nextpow2(Longy)		#NUMERO DE MUESTRAS
AudiOriginal = fft(y, AudioAnalysis)	#Aplicamos la FFT

f1 = fs*(np.arange((-AudioAnalysis/2), (AudioAnalysis/2)))/AudioAnalysis
AudiOrg=fftshift(AudiOriginal)			#ordenar de mayor a menor las fft

#Calculo de la magnitud
b1=2*abs(AudiOrg);
logY1=b1**2;


#Calculo de la fase
PhaseAudio=np.angle(AudiOrg);
Angle=(180/pi)*PhaseAudio

#-------------------------------------------------------------------------
# Frecuencias de corte para análisis de la señal
flow = 400								#frecuencia baja
fhigh = 800								#frecuencia alta
wclow=flow*1.25*pi
wchigh=fhigh*1.25*pi
ffiltro=Longy/max(time)
#ffiltro=Longy/time

#Filtro de la señal de pasa-banda
Long_OriginalSignal = len(Angle)
ffiltro1 = ffiltro*Long_OriginalSignal
Wnd1=[wclow/ffiltro, wchigh/ffiltro]
f1a,g1a = butter(4, [Wnd1[0]/2, Wnd1[1]/2,], btype='band')
FilteredSignal= filtfilt(f1a,g1a,y)
#sd.play(FilteredSignal*50); sd.wait()

#-------------------------------------------------------------------------
# FFT de la señal de audio (RADIOGRAFÍA DE LA SEÑAL)
AudioAnalysis2 = 2**nextpow2(Longy)		#NUMERO DE MUESTRAS
AudiOriginal2 = fft(FilteredSignal, AudioAnalysis2)	#Aplicamos la FFT
f2 = fs*(np.arange((-AudioAnalysis2/2), (AudioAnalysis2/2)))/AudioAnalysis2
AudiOrg2=fftshift(AudiOriginal2)			#ordenar de mayor a menor las fft

#Calculo de la magnitud
b2=2*abs(AudiOrg2)
logY2=b2**2


#Calculo de la fase
PhaseAudio2=np.angle(AudiOrg2)
Angle2=(180/pi)*PhaseAudio2

#-------------------------------------------------------------------------

#Grafica la señal de audio
F_3 = plt.plot(f1,logY1,'b', f2,logY2,'r', label = 'time vs y', linewidth=0.5)
plt.legend()
plt.grid(color='k', linestyle='--', linewidth=0.5)
plt.show()


F_4 = plt.plot(y,'b', label = 'time vs y', linewidth=0.5)
plt.plot(FilteredSignal,'r', label = 'time vs y', linewidth=0.5)
plt.legend()
plt.grid(color='k', linestyle='--', linewidth=0.5)
plt.show()
