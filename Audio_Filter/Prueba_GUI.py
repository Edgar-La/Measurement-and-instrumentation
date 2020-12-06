import os
os.system('clear')
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

def delete_values():
	F_low.set("")
	F_high.set("")
	Name_File.set("")

def close_window(): 
	    root.destroy()
	    exit()

root = Tk()
#root. geometry('1000x1000')
root.title('Filtro Pasa-Banda -- Edgar Lara')
root.configure(background='#696969')
image = PhotoImage( file = "IMG_GUI.png" )

F_low = StringVar(); F_high = StringVar(); #Name_File = StringVar();
F_low.set(400); F_high.set(800); #Name_File.set('Grabacion.wav');

image_label = Label(image = image).grid(row = 0, padx=27, pady=20, columnspan=5)

F_low_label = Label(root, text = "F baja = ").grid(row = 3, column = 0)
F_high_label = Label(root, text = "F alta = ").grid(row = 4, column = 0)
Name_File_label = Label(root, text = "Nombre archivo:").grid(row = 3, column = 2,  padx=2, pady=2)
Section_Record = Label(root, bg = '#20B2AA', text = "    Controles de audio    ").grid(row = 1, column = 3,  padx=2, pady=2)
Section_Record = Label(root, bg = '#20B2AA', text = "    Controles de audio    ").grid(row = 1, column = 3,  padx=2, pady=2)

files_names = ['Grabacion.wav', 'Test.wav','Grabacion_E.wav']
Name_File_box = StringVar(); Name_File_box.set(files_names[0])
F_low__entry = Entry(root, textvariable = F_low, width =10).grid(row = 3, column = 1)
F_high_entry = Entry(root, textvariable = F_high, width =10).grid(row = 4, column = 1)
#Name_File_entry = Entry(root, textvariable = Name_File).grid(row = 3, column = 3)
#Name_file_box = OptionMenu(root, Name_File_box, *files_names).grid(row = 9, column = 3)
Name_file_box = ttk.Combobox(root, value = files_names, width =18)
Name_file_box.current(0)
Name_file_box.grid(row = 3, column = 3)

Erase_button = Button(root, bg ='#008B8B', fg='white', text = "Limpiar valores", width =15, command = delete_values).grid(row = 8, column = 0, padx=2, pady=2)
Record_button = Button(root, bg ='#008B8B', fg='white', text = "Grabar", width =20).grid(row = 2, column = 3, padx=2, pady=2)
Play_Rec_O_button = Button(root, bg ='#483D8B', fg='white', text = "Play Original", width =20).grid(row = 4, column = 3, padx=2, pady=2)
Play_Rec_F_button = Button(root, bg ='#483D8B', fg='white', text = "Play Filtrado", width =20).grid(row = 5, column = 3, padx=2, pady=2)
Plot_Rec_button = Button(root, bg ='#483D8B', fg='white', text = "Graficar", width =20).grid(row = 6, column = 3, padx=2, pady=2)

my_button_close = Button(root, text="Cerrar ventana", bg ='red', fg='white', width =20, command=close_window).grid(row = 8, column = 3) 
root.mainloop()