import tkinter as tk

def update_label(*args):
    label.config(text=var.get())

root = tk.Tk()

var = tk.StringVar(value="None")
var.trace("w", update_label)

radiobutton1 = tk.Radiobutton(root, text="Сеня", variable=var, value="(988) 677-13-53", indicatoron=0, width=15)
radiobutton2 = tk.Radiobutton(root, text="Петя", variable=var, value="(924) 134-45-76", indicatoron=0, width=15)
radiobutton3 = tk.Radiobutton(root, text="Федя", variable=var, value="(946) 680-37-45", indicatoron=0, width=15)

label = tk.Label(root, text=var.get())

radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
label.pack()

root.mainloop()