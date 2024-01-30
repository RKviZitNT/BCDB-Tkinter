from tkinter import *

def draw_scene():
    canvas.delete('all')
    
    canvas.create_rectangle(50, 150, 150, 250, fill='lightblue')
    canvas.create_polygon(50, 150, 150, 150, 100, 100, fill='darkblue')

    canvas.create_oval(200, 50, 250, 100, fill='yellow')

    for i in range(0, 300, 10):
        canvas.create_arc(i, 250, i+10, 270, start=0, extent=180, fill='green')

root = Tk()

canvas = Canvas(root, width=300, height=300)
canvas.pack()

draw_scene()

root.mainloop()