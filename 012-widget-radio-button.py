import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Radio Button Example')

radio_var = tk.StringVar()
radio_var.set('Opsi 1')

radiobutton1 = ttk.Radiobutton(root, text = 'Opsi 1', variable=radio_var, value='Opsi 1')
radiobutton1.pack()

radiobutton2 = ttk.Radiobutton(root, text = 'Opsi 2', variable=radio_var, value='Opsi 2')
radiobutton2.pack()



def submit():
       print(f"Opsi 1 : {radio_var.get()}")


submit_button = ttk.Button(root, text = 'Submit', command=submit)
submit_button.pack()

root.mainloop()