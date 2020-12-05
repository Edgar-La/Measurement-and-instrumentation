import matplotlib.pyplot as plt #modulo para graficar
import sounddevice as sd #modulo para grabar audio
import soundfile as sf #modulo para abrir archivo audio
from scipy.io.wavfile import write #modulo para guardar audio
from scipy.fft import fft, ifft, fftshift
from scipy.signal import butter, filtfilt
import numpy as np
from math import pi
from time import sleep
from tkinter import *
from PIL import ImageTk, Image
import os
os.system('clear')

fs = 44100
########################################## Seccion de Back-End #############################################
def Record_audio():
	global seconds; global y; global fs; 
	seconds = 2
	#Grabar audio
	print('Grabando...')
	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
	sd.wait()
	print('Grabado'); print('Guardando...')
	#Guarda el audio
	write('Test.wav', fs, myrecording)
	print('Guardado')
	y,fs = sf.read('Grabacion_E.wav')

############################################################################################################
#Abre archivo de audio
def Open_audio(name_file):
	global y; global fs; #global Longy; global seconds; global Diftime; global time; 
	y,fs = sf.read(name_file)

############################################################################################################
#Reproduce audio
def Play_audio():
	sd.play(y*50);
	sd.wait()

############################################################################################################
def Definir_variables():
	global Longy; global seconds; global Diftime; global time; 
	Longy = len(y)
	#Diftime = seconds/Longy;
	seconds = Longy/fs
	Diftime = 1/fs
	time = np.arange(0, seconds, Diftime).tolist()


############################################################################################################
#Funcion especial de Nextpow2
def nextpow2(Longy):
	pot = 0
	while 2**pot <= Longy:
		NePw = 2**pot
		pot+=1
	return (pot)

############################################################################################################
# FFT de la señal de audio (RADIOGRAFÍA DE LA SEÑAL)
def Radiografia_senal():
	global f1; global logY1; global PhaseAudio; global Angle; 
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

############################################################################################################
# Frecuencias de corte para análisis de la señal
def Frecuencias_corte(flow, fhigh):
	global FilteredSignal; 
	wclow=flow*1.25*pi
	wchigh=fhigh*1.25*pi
	ffiltro=Longy/max(time)	#ffiltro=Longy/time

	#Filtro de la señal de pasa-banda
	Long_OriginalSignal = len(Angle)
	ffiltro1 = ffiltro*Long_OriginalSignal
	Wnd1=[wclow/ffiltro, wchigh/ffiltro]
	f1a,g1a = butter(4, [Wnd1[0]/2, Wnd1[1]/2,], btype='band')
	FilteredSignal= filtfilt(f1a,g1a,y)

############################################################################################################
#Reproduce audio filtrado
def Play_audio_filtrado():
	sd.play(FilteredSignal*50);
	sd.wait()

############################################################################################################
# FFT de la señal de audio (RADIOGRAFÍA DE LA SEÑAL)
def Radiografia_senal_filtrada():
	global f2; global logY2; global PhaseAudio2; global Angle2;
	AudioAnalysis2 = 2**nextpow2(Longy)		#NUMERO DE MUESTRAS
	AudiOriginal2 = fft(FilteredSignal, AudioAnalysis2)	#Aplicamos la FFT
	f2 = fs*(np.arange((-AudioAnalysis2/2), (AudioAnalysis2/2)))/AudioAnalysis2
	AudiOrg2=fftshift(AudiOriginal2)			#ordenar de mayor a menor las fft
	#Calculo de la magnitud
	b2=2*abs(AudiOrg2)
	logY2=b2**2
	#Calculo de la fase
	#PhaseAudio2=np.angle(AudiOrg2)
	#Angle2=(180/pi)*PhaseAudio2

############################################################################################################
#Graficas de radiografias de senales de audio
def Grafica_radiografias():
	F_3 = plt.plot(f1,logY1,'b', label = 'Radiografia senal original')
	plt.plot(f2,logY2,'r', label = 'Radiografia senal filtrada')
	plt.legend()
	plt.grid(color='k', linestyle='--', linewidth=0.5)
	plt.show()
	#plt.clf()
############################################################################################################
#Graficas de senales de audio
def Grafica_senales():
	F_4 = plt.plot(y,'b', label = 'Senal original')
	plt.plot(FilteredSignal,'r', label = 'Senal filtrada')
	plt.legend()
	plt.grid(color='k', linestyle='--', linewidth=0.5)
	plt.show()
	#linewidth=0.5
############################################################################################################
#Graficas mixta senales-radiografias
def Grafico_mixta():
	f = plt.figure(figsize=(15,4.5))
	senales_ = f.add_subplot(121)
	Radiografia_ = f.add_subplot(122)
	senales_.plot(y,'b', label = 'Senal original')
	senales_.plot(FilteredSignal,'r', label = 'Senal filtrada')
	senales_.legend(); senales_.grid(color='k', linestyle='--', linewidth=0.5)
	Radiografia_.plot(f1,logY1,'b', label = 'Radiografia senal original')
	Radiografia_.plot(f2,logY2,'r', label = 'Radiografia senal filtrada')
	Radiografia_.legend(); Radiografia_.grid(color='k', linestyle='--', linewidth=0.5)
	plt.show()
################################ Seccion de funciones para botones #########################################
#Boton grabar
def Btn_grabar():
	Record_audio()
#Boton play original ###################################
def Btn_play(name_file):
	Open_audio(name_file+'.wav')
	Play_audio()
#Boton ply filtrado ####################################
def Btn_play_filtrado(name_file, flow_, fhigh_):
	Open_audio(name_file+'.wav')
	Definir_variables()
	Radiografia_senal()
	Frecuencias_corte(flow_, fhigh_)
	Play_audio_filtrado()
#Botones para  graficar ########################################
def Btn_graficar_senales(name_file, flow_, fhigh_):
	Open_audio(name_file+'.wav'); Definir_variables(); Radiografia_senal(); Frecuencias_corte(flow_, fhigh_); Radiografia_senal_filtrada()
	Grafica_senales()

def Btn_graficar_radiografias(name_file, flow_, fhigh_):
	Open_audio(name_file+'.wav'); Definir_variables(); Radiografia_senal(); Frecuencias_corte(flow_, fhigh_); Radiografia_senal_filtrada()
	Grafica_radiografias()

def Btn_grafica_mixta(name_file, flow_, fhigh_):
	Open_audio(name_file+'.wav'); Definir_variables(); Radiografia_senal(); Frecuencias_corte(flow_, fhigh_); Radiografia_senal_filtrada()
	Grafico_mixta()

############################################################################################################
########################################## Seccion de Front-End ############################################
############################################################################################################
#Funciones de la ventana
def delete_values():
	F_low.set("")
	F_high.set("")
	Name_File.set("")

def close_window(): 
	    root.destroy()
	    exit()

############################################################################################################
#Configuracion ventana
root = Tk()
#root. geometry('1000x1000')
root.title('Filtro Pasa-Banda -- Edgar Lara')
root.configure(background='#696969')
image = PhotoImage( file = "IMG_GUI.png" )
image_label = Label(image = image).grid(row = 0, padx=27, pady=20, columnspan=5)

############################################################################################################
#Configiracion etiquetas y cajas de texto
F_low = StringVar(); F_high = StringVar(); Name_File = StringVar();
F_low.set(400); F_high.set(800); Name_File.set('Grabacion'); 

F_low_label = Label(root, text = "F baja = ").grid(row = 3, column = 0)
F_high_label = Label(root, text = "F alta = ").grid(row = 4, column = 0)
Name_File_label = Label(root, text = "Nombre archivo:").grid(row = 3, column = 2,  padx=2, pady=2)
Section_Record = Label(root, bg = '#20B2AA', text = "    Controles de audio    ").grid(row = 1, column = 3,  padx=2, pady=2)

F_low__entry = Entry(root, textvariable = F_low, width =10).grid(row = 3, column = 1)
F_high_entry = Entry(root, textvariable = F_high, width =10).grid(row = 4, column = 1)
Name_File_entry = Entry(root, textvariable = Name_File).grid(row = 3, column = 3)

############################################################################################################
#Botones
Erase_button = Button(root, bg ='#008B8B', fg='white', text = "Limpiar valores", width =15, command = delete_values).grid(row = 8, column = 0, padx=2, pady=2)
Record_button = Button(root, bg ='#008B8B', fg='white', text = "Grabar", width =20, command = Btn_grabar).grid(row = 2, column = 3, padx=2, pady=2)
Play_Rec_O_button = Button(root, bg ='#483D8B', fg='white', text = "Play Original", width =20, command = lambda: Btn_play(Name_File.get())).grid(row = 4, column = 3, padx=2, pady=2)
Play_Rec_F_button = Button(root, bg ='#483D8B', fg='white', text = "Play Filtrado", width =20, command = lambda: Btn_play_filtrado(Name_File.get(), float(F_low.get()), float(F_high.get()))).grid(row = 5, column = 3, padx=2, pady=2)
Plot_Rec_button = Button(root, bg ='#483D8B', fg='white', text = "Graficar", width =20, command = lambda: Btn_grafica_mixta(Name_File.get(), float(F_low.get()), float(F_high.get()))).grid(row = 6, column = 3, padx=2, pady=2)
my_button_close = Button(root, text="Cerrar ventana", bg ='red', fg='white', width =20, command=close_window).grid(row = 8, column = 3) 
root.mainloop()
