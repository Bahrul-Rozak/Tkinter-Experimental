import tkinter as tk

root = tk.Tk()
root.title('Hello World')

label = tk.Label(root, text='Hello World')
label.pack()

root.geometry('400x300')
root.mainloop()