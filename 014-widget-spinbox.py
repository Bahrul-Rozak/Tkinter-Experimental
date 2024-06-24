import tkinter as tk
from tkinter import ttk

def on_spinbox_change():
       current_value = spinbox.get()
       label.config(text = f'Nilai yang dipilih {current_value}')

root = tk.Tk()
root.title('Spinbox')

label = ttk.Label(root, text = 'Pilih nilai dari spinbox')
label.pack(pady=10)

spinbox = tk.Spinbox(root, from_=0, to=10, increment=1, command=on_spinbox_change)
spinbox.pack(pady=10)

button = ttk.Button(root, text='Tampilkan Nilai', command=on_spinbox_change)
button.pack(pady=10)

root.mainloop()