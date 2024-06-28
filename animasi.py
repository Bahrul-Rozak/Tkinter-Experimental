import tkinter as tk

root = tk.Tk()
root.title('Animasi Ex')

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

circle = canvas.create_oval(50, 50, 100, 100, fill='blue')

dx = 2
dy = 2

def move_circle():
       global dx, dy
       x1, y1, x2, y2 = canvas.coords(circle)
       if x1 <= 0 or x2 >=600:
              dx = -dx
       if y1 <= 0 or y2 >= 400:
              dy = -dy

       canvas.move(circle, dx, dy)
       canvas.after(20, move_circle)

move_circle()

root.mainloop()
