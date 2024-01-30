from tkinter import *

def motion(event):
    target_x = event.x
    target_y = event.y
    current_x = c.coords(ball)[0] + ball_width // 2
    current_y = c.coords(ball)[1] + ball_height // 2

    #То, что объект перемещается под прямым углом, а не по диагонали - НЕ БАГ, А ФИЧА!

    if current_x < target_x:
        c.move(ball, 1, 0)
        root.after(10, motion, event)
    elif current_x > target_x:
        c.move(ball, -1, 0)
        root.after(10, motion, event)
    elif current_y < target_y:
        c.move(ball, 0, 1)
        root.after(10, motion, event)
    elif current_y > target_y:
        c.move(ball, 0, -1)
        root.after(10, motion, event)

root = Tk()

c = Canvas(root, width=300, height=200, bg="white")
c.pack()

ball_x = 0
ball_y = 100
ball_height = 30
ball_width = 30

ball = c.create_oval(ball_x, ball_y, ball_x + ball_width, ball_y + ball_height, fill='black')

c.bind("<Button-1>", motion)

root.mainloop()