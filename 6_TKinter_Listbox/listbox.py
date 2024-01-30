from tkinter import *

def add_item():
    selected = listbox1.curselection()
    for index in selected[::-1]:
        listbox2.insert(END, listbox1.get(index))
        listbox1.delete(index)

def remove_item():
    selected = listbox2.curselection()
    for index in selected[::-1]:
        listbox1.insert(END, listbox2.get(index))
        listbox2.delete(index)

root = Tk()

listbox1 = Listbox(root, height=11, width=30, selectmode=MULTIPLE)
listbox2 = Listbox(root, height=11, width=30, selectmode=MULTIPLE)

for item in ["Молоко", "Картофель", "Морковь", "Сыр", "Термоядерная боеукладка M-741"]:
    listbox1.insert(END, item)

buttons = Frame(root)

button1 = Button(buttons, text=">>>", height=5, command=add_item)
button2 = Button(buttons, text="<<<", height=5, command=remove_item)

button1.pack(side=TOP)
button2.pack(side=TOP)

listbox1.pack(side=LEFT)
buttons.pack(side=LEFT)
listbox2.pack(side=LEFT)

root.mainloop()