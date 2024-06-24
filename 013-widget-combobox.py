import tkinter as tk
from tkinter import ttk

def ubah_warga_bg(event):
       warna = combobox_warna.get()
       if warna == 'Merah':
              root.config(bg = 'red')
       elif warna == 'Hijau':
              root.config(bg  = 'green')
       elif warna == 'Biru':
              root.config(bg = 'blue')
       else:
              root.config(bg = 'white')

root = tk.Tk()
root.title('Ubah Warna BG')
root.geometry('300x200')

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

choices_warna = ['Merah', 'Hijau', 'Biru', 'Putih']
combobox_warna = ttk.Combobox(frame, values=choices_warna)
combobox_warna.set('Pilih Warna')
combobox_warna.state(['readonly'])
combobox_warna.grid(row = 0, column= 0, padx = 10, pady = 10)

combobox_warna.bind('<<ComboboxSelected>>', ubah_warga_bg)

root.mainloop()