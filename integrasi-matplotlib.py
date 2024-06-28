import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.title('Integrated with matplotlib')

root.geometry('800x600')

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

fig = Figure(figsize=(6, 4), dpi=100)
plot = fig.add_subplot(111)
plot.plot(x, y, marker='o', linestyle='-', color='b', label='Data')

plot.set_xlabel('X Axis')
plot.set_ylabel('Y Axis')
plot.set_title('Ex')

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()
          

root.mainloop()