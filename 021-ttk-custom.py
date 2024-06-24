import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Contoh Tema dengan TTK')
root.geometry('300x200')

style = ttk.Style()

style.theme_use('classic')

label = ttk.Label(root, text='Helo Warga!', font=('Arial', 16))
label.pack(pady=20)

root.mainloop()