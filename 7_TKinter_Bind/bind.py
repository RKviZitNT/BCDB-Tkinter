from tkinter import *

def enter_pressed(event):
    text = entry.get()

    listbox.insert(END, text)

    entry.delete(0, END)

def double_click(event):
    selection = listbox.curselection()
    if selection:
        text = listbox.get(selection[0])

        entry.delete(0, END)
        entry.insert(END, text)

root = Tk()

entry = Entry(root)
entry.pack()
entry.bind('<Return>', enter_pressed)

listbox = Listbox(root)
listbox.pack()
listbox.bind('<Double-Button-1>', double_click)

root.mainloop()