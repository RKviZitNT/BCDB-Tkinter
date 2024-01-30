from tkinter import *

def but_red():
    label.config(text="Красный")

def but_orange():
    label.config(text="Оранжевый")

def but_yellow():
    label.config(text="Жёлтый")

def but_green():
    label.config(text="Зелёный")

def but_lightblue():
    label.config(text="Голубой")

def but_blue():
    label.config(text="Синий")

def but_violet():
    label.config(text="Фиолетовый")

root = Tk()

label = Label(text="", font="Arial 12", justify="center")
label.pack()

button1 = Button(text="", width=15, height=2, bg="#ff0000")
button1.config(command=but_red)
button1.pack()

button2 = Button(text="", width=15, height=2, bg="#ff7d00")
button2.config(command=but_orange)
button2.pack()

button3 = Button(text="", width=15, height=2, bg="#ffff00")
button3.config(command=but_yellow)
button3.pack()

button4 = Button(text="", width=15, height=2, bg="#00ff00")
button4.config(command=but_green)
button4.pack()

button5 = Button(text="", width=15, height=2, bg="#007dff")
button5.config(command=but_lightblue)
button5.pack()

button6 = Button(text="", width=15, height=2, bg="#0000ff")
button6.config(command=but_blue)
button6.pack()

button7 = Button(text="", width=15, height=2, bg="#7d00ff")
button7.config(command=but_violet)
button7.pack()

root.mainloop()