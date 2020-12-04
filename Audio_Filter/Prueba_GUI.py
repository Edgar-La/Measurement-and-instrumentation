import os
os.system('clear')
from tkinter import *
from PIL import ImageTk, Image

def delete_values():
	F_low.set("")
	F_high.set("")
	Name_File.set("")
	R3.set("")
	R4.set("")

def calculate(Vs_, R1_, R2_, R3_, R4_):
	Vo_ = (Vs_*R3_*(R2_+R4_))/(R3_*(-R1_-R2_+R4_)-R2_*(3*R2_+2*R1_)-R4_*(R1_+R2_))
	Isc_ = (-1*Vs_*(R2_+R4_))/(R2_*(2*R1_+3*R2_+R4_)+R1_*R4_)
	Rth_ = Vo_/Isc_
	Vo.set(Vo_); Isc.set(Isc_); Rth.set(Rth_);
	Vo_label_ = Label(root, textvariable = str(Vo)).grid(row = 6, column = 1)
	Isc_label_ = Label(root, textvariable = str(Isc)).grid(row = 7, column = 1)
	Rth_label_ = Label(root, textvariable = str(Rth)).grid(row = 8, column = 1)

root = Tk()
#root. geometry('1000x1000')
root.title('Filtro Pasa-Banda -- Edgar Lara')
root.configure(background='#F5F5F5')
image = PhotoImage( file = "IMG_GUI.png" )

F_low = StringVar(); F_high = StringVar(); Name_File = StringVar(); R3 = StringVar(); R4 = StringVar();
F_low.set(400); F_high.set(800); Name_File.set('Grabacion'); R3.set(500); R4.set(10000);
Vo = StringVar(); Isc = StringVar(); Rth = StringVar();
Vo.set(""); Isc.set(""); Rth.set("") 

image_label = Label(image = image).grid(row = 0, padx=27, pady=20, columnspan=5)

F_low_label = Label(root, text = "F low = ").grid(row = 2, column = 0)
F_high_label = Label(root, text = "F high = ").grid(row = 3, column = 0)
Name_File_label = Label(root, text = "File = ").grid(row = 2, column = 3)
Section_Record = Label(root, bg = '#20B2AA', text = "Controles audio nuevo").grid(row = 1, column = 2)
Section_ = Label(root, bg = '#20B2AA', text = "Controles pregrabado").grid(row = 1, column = 4)
#R3_label = Label(root, text = "R3 = ").grid(row = 4, column = 0)
#R4_label = Label(root, text = "R4 = ").grid(row = 5, column = 0)
#Vo_label = Label(root, text = "Vo = ").grid(row = 6, column = 0)
#Isc_label = Label(root, text = "Isc = ").grid(row = 7, column = 0)
#Rth_label = Label(root, text = "Rth = ").grid(row = 8, column = 0)

F_low__entry = Entry(root, textvariable = F_low).grid(row = 2, column = 1)
F_high_entry = Entry(root, textvariable = F_high).grid(row = 3, column = 1)
Name_File_entry = Entry(root, textvariable = Name_File).grid(row = 2, column = 4)
#R3_entry = Entry(root, textvariable = R3).grid(row = 4, column = 1)
#R4_entry = Entry(root, textvariable = R4).grid(row = 5, column = 1)
#Vo_label_ = Label(root, textvariable = str(Vo)).grid(row = 6, column = 1)
#Isc_label_ = Label(root, textvariable = str(Isc)).grid(row = 7, column = 1)
#Rth_label_ = Label(root, textvariable = str(Rth)).grid(row = 8, column = 1)

Erase_button = Button(root, bg ='red', fg='white', text = "Erase values", width =20, command = delete_values).grid(row = 9, column = 0, padx=2, pady=2)
#Calculate_button = Button(root, bg ='blue', fg='white', text = "Calculate", command = lambda: calculate(float(Vs.get()), float(R1.get()), float(R2.get()), float(R3.get()), float(R4.get())))
#Calculate_button.grid(row = 9, column = 1)
Record_button = Button(root, bg ='#008B8B', fg='white', text = "Grabar", width =20).grid(row = 2, column = 2, padx=2, pady=2)
Play_Rec_O_button = Button(root, bg ='#008B8B', fg='white', text = "Play Original", width =20).grid(row = 3, column = 2, padx=2, pady=2)
Play_Rec_F_button = Button(root, bg ='#008B8B', fg='white', text = "Play Filtrado", width =20).grid(row = 4, column = 2, padx=2, pady=2)
Plot_Rec_button = Button(root, bg ='#008B8B', fg='white', text = "Graficar", width =20).grid(row = 5, column = 2, padx=2, pady=2)

Play_File_O_button = Button(root, bg ='#483D8B', fg='white', text = "Play Original", width =20).grid(row = 3, column = 4, padx=2, pady=2)
Play_File_F_button = Button(root, bg ='#483D8B', fg='white', text = "Play Filtrado", width =20).grid(row = 4, column = 4, padx=2, pady=2)
Plot_File_button = Button(root, bg ='#483D8B', fg='white', text = "Graficar", width =20).grid(row = 5, column = 4, padx=2, pady=2)
#Plot_button = Button(root, bg ='blue', fg='white', text = "Graficar").grid(row = 9, column = 3)
root.mainloop()