import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Checked Example')

check_var1 = tk.IntVar()
check_var2 = tk.IntVar()

checkbutton1 = ttk.Checkbutton(root, text = 'Opsi 1', variable=check_var1)
checkbutton1.pack()

checkbutton2 = ttk.Checkbutton(root, text = 'Opsi 2', variable=check_var2)
checkbutton2.pack()

def submit():
       print(f"Opsi 1 : {check_var1.get()}")
       print(f"Opsi 2 : {check_var2.get()}")

submit_button = ttk.Button(root, text = 'Submit', command=submit)
submit_button.pack()

root.mainloop()