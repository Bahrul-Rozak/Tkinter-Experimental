import tkinter as tk
from tkinter import filedialog

def open_file():
       file_path = filedialog.askopenfilename(title='Pilih File', filetypes=[('Text Files', "*.txt"), ('All Files', '*.*')])

       if file_path:
              try:
                     with open(file_path, 'r') as file:
                            content = file.read()
                            text_area.delete(1.0, tk.END)
                            text_area.insert(tk.END, content)

              except Exception as e:
                     print(f'Terjadi kesalahan {e}')

def save_file():
       file_path = filedialog.asksaveasfilename(title='Simpan File', defaultextension='.txt', filetypes=[('Text Files', "*.txt"), ('All Files', '*.*')])

       if file_path:
              try:
                     with open(file_path, 'w') as file:
                            content =  text_area.get(1.0, tk.END)
                            file.write(content)

              except Exception as e:
                     print(f'Terjadi kesalahan {e}')

root = tk.Tk()
root.title('Aplikasi Pengelolaan File')

text_area = tk.Text(root, wrap='word')
text_area.pack(expand=1, fill='both')

button_frame = tk.Frame(root)
button_frame.pack(fill='x')

open_button = tk.Button(button_frame, text='Buka File', command=open_file)
open_button.pack(side='left', padx=5, pady = 5)

save_button = tk.Button(button_frame, text='Save File', command=save_file)
save_button.pack(side='left', padx=5, pady = 5)

root.mainloop()