import tkinter as tk

def open_shape_window():
    second_window = tk.Toplevel(root)
    label1 = tk.Label(second_window, text="X1:")
    label1.grid(row=0, column=0)
    x1_entry = tk.Entry(second_window)
    x1_entry.grid(row=0, column=1)

    label2 = tk.Label(second_window, text="Y1:")
    label2.grid(row=1, column=0)
    y1_entry = tk.Entry(second_window)
    y1_entry.grid(row=1, column=1)

    label3 = tk.Label(second_window, text="X2:")
    label3.grid(row=2, column=0)
    x2_entry = tk.Entry(second_window)
    x2_entry.grid(row=2, column=1)

    label4 = tk.Label(second_window, text="Y2:")
    label4.grid(row=3, column=0)
    y2_entry = tk.Entry(second_window)
    y2_entry.grid(row=3, column=1)

    shape_type = tk.StringVar()
    shape_type.set("rectangle")
    rect_radio = tk.Radiobutton(second_window, text="Прямоугольник", variable=shape_type, value="rectangle")
    rect_radio.grid(row=4, column=0)
    oval_radio = tk.Radiobutton(second_window, text="Овал", variable=shape_type, value="oval")
    oval_radio.grid(row=4, column=1)

    def draw_shape():
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
        if shape_type.get() == "rectangle":
            c.create_rectangle(x1, y1, x2, y2, outline='black', fill='')
        else:
            c.create_oval(x1, y1, x2, y2, outline='black', fill='')

        second_window.destroy()

    draw_button = tk.Button(second_window, text="Нарисовать", command=draw_shape)
    draw_button.grid(row=5, column=0, columnspan=2)

root = tk.Tk()
root.title("Рисование фигур")

c = tk.Canvas(root, width=600, height=400)
c.pack()

add_button = tk.Button(root, text="Добавить фигуру", command=open_shape_window)
add_button.pack()

root.mainloop()