import os
os.system('clear')
from tkinter import *
from PIL import ImageTk, Image

def delete_values():
	Vs.set("")
	R1.set("")
	R2.set("")
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
	#Rth_ = (-R3*(R2*(2*R1+3*R2+R4)+R1*R4))/(R3*(-R1-R2+R4)-R2*(3*R2+2*R1)-R4*(R1+R2))

root = Tk()
root.title('Thevenin Estimation - Edgar Lara')
root.configure(background='#212F3C')
image = PhotoImage( file = "Circuit_diagram.png" )

Vs = StringVar(); R1 = StringVar(); R2 = StringVar(); R3 = StringVar(); R4 = StringVar();
Vs.set(5); R1.set(2000); R2.set(1000); R3.set(500); R4.set(10000);
Vo = StringVar(); Isc = StringVar(); Rth = StringVar();
Vo.set(""); Isc.set(""); Rth.set("") 

image_label = Label(image = image).grid(row = 0, padx=27, pady=20, columnspan=2)

Vs_label = Label(root, text = "Vs = ").grid(row = 1, column = 0)
R1_label = Label(root, text = "R1 = ").grid(row = 2, column = 0)
R2_label = Label(root, text = "R2 = ").grid(row = 3, column = 0)
R3_label = Label(root, text = "R3 = ").grid(row = 4, column = 0)
R4_label = Label(root, text = "R4 = ").grid(row = 5, column = 0)
Vo_label = Label(root, text = "Vo = ").grid(row = 6, column = 0)
Isc_label = Label(root, text = "Isc = ").grid(row = 7, column = 0)
Rth_label = Label(root, text = "Rth = ").grid(row = 8, column = 0)

Vs_entry = Entry(root, textvariable = Vs).grid(row = 1, column = 1)
R1_entry = Entry(root, textvariable = R1).grid(row = 2, column = 1)
R2_entry = Entry(root, textvariable = R2).grid(row = 3, column = 1)
R3_entry = Entry(root, textvariable = R3).grid(row = 4, column = 1)
R4_entry = Entry(root, textvariable = R4).grid(row = 5, column = 1)
Vo_label_ = Label(root, textvariable = str(Vo)).grid(row = 6, column = 1)
Isc_label_ = Label(root, textvariable = str(Isc)).grid(row = 7, column = 1)
Rth_label_ = Label(root, textvariable = str(Rth)).grid(row = 8, column = 1)

Erase_button = Button(root, bg ='red', fg='white', text = "Erase values", command = delete_values).grid(row = 9, column = 0)
Calculate_button = Button(root, bg ='blue', fg='white', text = "Calculate", command = lambda: calculate(float(Vs.get()), float(R1.get()), float(R2.get()), float(R3.get()), float(R4.get())))
Calculate_button.grid(row = 9, column = 1)
root.mainloop()