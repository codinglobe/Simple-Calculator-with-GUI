#Simple Calculator with GUI
#Created by codinglobe 2021

from tkinter import *

def buttonadd():
    number1 = float(entryNumber1.get())
    number2 = float(entryNumber2.get())
    summe = number1 + number2
    labelsumme.config(text=str(summe))

def buttonsub():
    number1 = float(entryNumber1.get())
    number2 = float(entryNumber2.get())
    summe = number1 - number2
    labelsumme.config(text=str(summe))

def buttonmultiply():
    number1 = float(entryNumber1.get())
    number2 = float(entryNumber2.get())
    summe = number1 * number2
    labelsumme.config(text=str(summe))

def buttondiv():
    number1 = float(entryNumber1.get())
    number2 = float(entryNumber2.get())
    summe = number1 / number2
    labelsumme.config(text=str(summe))

#GUI Window
tkWindow = Tk()
tkWindow.title("Simple Calculator with GUI")
tkWindow.geometry("400x150")

#Number 1 row
labelnumber1 = Label(master=tkWindow, bg="grey", text="Number 1", width="20")
labelnumber1.grid(row=0, column=0, padx="5", pady="5", sticky="ew")

entryNumber1 = Entry(master=tkWindow, bg="white", width="20")
entryNumber1.grid(row=0, column=1, padx="5", pady="5", sticky="ew")

#Number 2 row
labelnumber2 = Label(master=tkWindow, bg="grey", text="Number 2", width="20")
labelnumber2.grid(row=1, column=0, padx="5", pady="5", sticky="ew")

entryNumber2 = Entry(master=tkWindow, bg="white", width="20")
entryNumber2.grid(row=1, column=1, padx="5", pady="5", sticky="ew")

#Button Add
buttonadd = Button(master=tkWindow, text="+", width="10", bg="grey", command=buttonadd)
buttonadd.grid(row=0, column=2, padx="5", pady="5")

#Button Sub
buttonsub = Button(master=tkWindow, text="-", width="10", bg="grey", command=buttonsub)
buttonsub.grid(row=1, column=2, padx="5", pady="5")

#Button multiply
buttonmultiply = Button(master=tkWindow, text="*", width="10", bg="grey", command=buttonmultiply)
buttonmultiply.grid(row=2, column=2, padx="5", pady="5")

#Button div
buttondiv = Button(master=tkWindow, text="/", width="10", bg="grey", command=buttondiv)
buttondiv.grid(row=3, column=2, padx="5", pady="5")

#summe
labeltitlesumme = Label(master=tkWindow, bg="green", text="Summe")
labeltitlesumme.grid(row=3, column=0, padx="5", pady="5", sticky="ew")

labelsumme = Label(master=tkWindow, bg="grey", width="20", text="")
labelsumme.grid(row=3, column=1, padx="5", pady="5", sticky="ew")

tkWindow.mainloop()