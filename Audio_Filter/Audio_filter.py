import matplotlib.pyplot as plt #modulo para graficar
import sounddevice as sd #modulo para grabar audio
import soundfile as sf #modulo para abrir archivo audio
from scipy.io.wavfile import write #modulo para guardar audio
from scipy.fft import fft, ifft, fftshift
from scipy.signal import butter, filtfilt
import numpy as np
from math import pi
from time import sleep
from tkinter import *; from tkinter import ttk, messagebox; from tkinter import font as tkFont
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
	write('Grabacion.wav', fs, myrecording)
	print('Guardado')
	#y,fs = sf.read('Grabacion_E.wav')

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
	#seconds = 2
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
	senales_.plot(y,'b', label = 'Senal original', linewidth=0.5)
	senales_.plot(FilteredSignal,'r', label = 'Senal filtrada', linewidth=0.5)
	senales_.legend(); senales_.grid(color='k', linestyle='--', linewidth=0.5)
	Radiografia_.plot(f1,logY1,'b', label = 'Radiografia senal original')
	Radiografia_.plot(f2,logY2,'r', label = 'Radiografia senal filtrada')
	Radiografia_.legend(); Radiografia_.grid(color='k', linestyle='--', linewidth=0.5)
	plt.show()
################################ Seccion de funciones para botones #########################################
#Boton grabar
def Btn_grabar():
	messagebox.showinfo(message="Comenzará grabacion de 2 segundos", title="")
	Record_audio()#-----------------------------------------------------------------------------------------

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
        cerrar = messagebox.askyesno(message="Seguro que quieres salir?")
        if cerrar == True:
            root.destroy()

############################################################################################################
#Configuracion ventana
root = Tk()
#root. geometry('1000x1000')
root.title('Filtro Pasa-Banda -- Edgar Lara')
root.protocol("WM_DELETE_WINDOW", close_window)
root.configure(background='#696969')
imagen_portada = Image.open('IMG_GUI.png')
imagen_portada = imagen_portada. resize((700, 400), Image. ANTIALIAS)
imagen_portada = ImageTk. PhotoImage(imagen_portada)
image_label = Label(image = imagen_portada).grid(row = 0, padx=20, pady=10, columnspan=5)

#image = PhotoImage( file = "IMG_GUI.png" )
#image_label = Label(image = image).grid(row = 0, padx=27, pady=20, columnspan=5)

#imagen_rec = PhotoImage( file = "Btn_verde.png" ); imagen_rec.resize((450, 350))
image_rec = Image.open('micro.png')
image_rec = image_rec. resize((40, 40), Image. ANTIALIAS)
image_rec = ImageTk. PhotoImage(image_rec)

############################################################################################################
#Configiracion etiquetas y cajas de texto
helv36 = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)
F_low = StringVar(); F_high = StringVar(); #Name_File = StringVar();
F_low.set(400); F_high.set(800); #Name_File.set('Grabacion'); 

F_low_label = Label(root, text = "Frecuencia baja = ", font=helv36).grid(row = 3, column = 0)
F_high_label = Label(root,text = "Frecuencia alta = ", font=helv36).grid(row = 4, column = 0)
Rec_img = Label(root, image=image_rec).grid(row = 2, column = 2, padx=2)
Name_File_label = Label(root, text = "Nombre archivo:", font=helv36).grid(row = 3, column = 2,  padx=2, pady=2)
Section_Record = Label(root, bg = '#20B2AA', text = "    Controles de audio    ", font=helv36).grid(row = 1, column = 3,  padx=2, pady=2)

F_low__entry = Entry(root, textvariable = F_low, width =6, font=helv36,).grid(row = 3, column = 1)
F_high_entry = Entry(root, textvariable = F_high, width =6, font=helv36,).grid(row = 4, column = 1)
#Name_File_entry = Entry(root, textvariable = Name_File).grid(row = 3, column = 3)
files_names = ['Grabacion', 'Campana_1', 'Campana_2', 'Chasquidos',  'Dedos_purados',
				'Esferas_Newton', 'Escribir',  'Guitarra_1', 'Guitarra_2', 'Toc_Toc']
Name_file_box = ttk.Combobox(root, value = files_names, width =18, font=helv36,)
Name_file_box.current(0)
Name_file_box.grid(row = 3, column = 3)

############################################################################################################
#Botones
#helv36 = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)
Erase_button = Button(root, bg ='#008B8B', fg='white', font=helv36, text = "Limpiar valores", width =15, command = delete_values).grid(row = 8, column = 0, padx=2, pady=2)
Record_button = Button(root, bg ='#008B8B', fg='white', font=helv36, text = "Grabar", width =20, command = Btn_grabar).grid(row = 2, column = 3, padx=2, pady=2)
Play_Rec_O_button = Button(root, bg ='#483D8B', fg='white', font=helv36, text = "Play Original", width =20, command = lambda: Btn_play(Name_file_box.get())).grid(row = 4, column = 3, padx=2, pady=2)
Play_Rec_F_button = Button(root, bg ='#483D8B', fg='white', font=helv36, text = "Play Filtrado", width =20, command = lambda: Btn_play_filtrado(Name_file_box.get(), float(F_low.get()), float(F_high.get()))).grid(row = 5, column = 3, padx=2, pady=2)
Plot_Rec_button = Button(root, bg ='#483D8B', fg='white', font=helv36, text = "Graficar", width =20, command = lambda: Btn_grafica_mixta(Name_file_box.get(), float(F_low.get()), float(F_high.get()))).grid(row = 6, column = 3, padx=2, pady=2)
my_button_close = Button(root, text="Cerrar ventana", bg ='red', fg='white', font=helv36, width =20, command=close_window).grid(row = 8, column = 3) 
root.mainloop()
