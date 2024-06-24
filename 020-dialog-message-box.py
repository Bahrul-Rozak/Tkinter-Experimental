import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

root = tk.Tk()
root.title('Dialog Dan Message Box')
root.geometry('500x400')

label = tk.Label(root, text='Selamat Datang')
label.place(x=100, y=50)

def show_info():
       messagebox.showinfo('Informasi', 'Ini adalah message box informasi')

button_info = tk.Button(root, text='Tampilkan Info Ngab', command=show_info)
button_info.place(x=150, y=100)

def ask_confirmation():
       response = messagebox.askyesno('Konfirmasi', 'Apakah Anda Yakin ingin Melanjutkan Jabatan Ini?')
       if response:
              messagebox.showinfo('Informasi', 'Anda Memilih Ya')
       else:
              messagebox.showinfo('Informasi', 'Anda Memiliki Tidak')

button_confirm = tk.Button(root, text='Minta Konfirmasi', command=ask_confirmation)
button_confirm.place(x=250, y=250)

def open_file():
       file_path = filedialog.askopenfilename(title='Buka File', filetypes=(('Text Files', '*.txt'),('All Files', '*.*')))
       if file_path:
              messagebox.showinfo('File Terpilih', f'Anda memilih file: {file_path}')

button_open = tk.Button(root, text='Buka File', command=open_file)
button_open.place(x=150, y=150)

root.mainloop()