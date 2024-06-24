import tkinter as tk
from tkinter import Menu

root = tk.Tk()
root.title('Aplikasi Menubar yang sangat keren')
root.geometry('400x300')

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = 'File', menu=file_menu)

edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = 'Edit', menu=edit_menu)

file_menu.add_command(label = 'Open', command=lambda: print('Open Clicked'))
file_menu.add_separator()
file_menu.add_command(label = 'Exit', command=root.quit)

edit_menu.add_command(label = 'Cut', command=lambda: print('Cut Clicked'))
edit_menu.add_command(label = 'Copy', command=lambda: print('Copy Clicked'))
edit_menu.add_command(label = 'Paste', command=lambda: print('Paste Clicked'))

label = tk.Label(root, text='Label di posisi tertentu', bg='yellow')
label.place(x=50, y=50, width=150, height=30)

button = tk.Button(root, text='Klik')
button.place(x=220, y=100, width=100, height=30)

root.mainloop()