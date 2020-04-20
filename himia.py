from tkinter import *
from random import random
from tkinter import messagebox


root = Tk()
#ЗАГОЛОВОК ПО
root.title("Кислоти")


#ДЛЯ РАМДОМНОГО РОЗКИДУ ХІМІЧНИХ НАЗВ ЕЛЕМЕНТІВ
def randomOrder_key(element):
    return random()


#КНОПКА НАЧАТИ
def output_2(event):
	kusrotu_1 = ["SO4","SO3","S",
				"SiO3","NO2","NO3",
				"Cl","PO4","CO3"]

	kusrotu_1_copi = sorted(kusrotu_1, key = randomOrder_key)
	

	for text_BB in kusrotu_1_copi:
		label_1["text"] = text_BB

	#ТУТ РОБИМО ПЕРЕМЕНІЄ ГЛОБАЛЬНИМИ
	global fff
	fff = kusrotu_1_copi

	global kkk
	kkk = text_BB



#ДЛЯ ТОГО ГОБ ЗРОБИТИ ТЕКТ ГРОБАЛЬНИМ
def ggg():
	return fff, kkk


#КНОПКА ПРОВІРИТИ
def output_1(event):
	kusrotu_2 = {"SO4" :"сульфат",
				"SO3" :"сульфіт",
				"S"   :"сульфід",
				"SiO3":"силікат",
				"NO2" :"нітрит",
				"NO3" :"нітрат",
				"Cl"  :"хлорид",
				"PO4" :"фосфат",
				"CO3" :"карбонат"}
	ggg() # ПЕРЕДАЄ fff and kkk

	text_formul = entry_1.get()


	if text_formul == kusrotu_2[kkk]:
		messagebox.showinfo("Відповідь", "Правильно!")
	else:
		messagebox.showerror("Відповідь", "Це "+ kusrotu_2[kkk] + ", запамятай!")


#ВЕСЬ ІНТЕРФЕЙС ПРОГРАМИ
label_1 = Label(root, width=7, font=15)
entry_1 = Entry(root, width=15, font=15)
button_1 = Button(root, text="Провірити")
button_2 = Button(root, text="Начати")

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)

button_2.grid(row=1, column=0)
button_1.grid(row=1, column=1)

button_1.bind("<Button-1>", output_1)
button_2.bind("<Button-1>", output_2)


root.mainloop()