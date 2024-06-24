import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Penggunaan Canvas')

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

image = Image.open('gambar.png')

tk_image = ImageTk.PhotoImage(image)

canvas.create_image(400, 400, image=tk_image)

root.mainloop()