import tkinter as tk

def on_button_click():
       label.config(text = 'Tombol Telah Diklik!')

root = tk.Tk()
root.title('Event')

label = tk.Label(root, text = 'Tekan Tombol untuk Mengubah Teks')
label.pack(pady=20)

button = tk.Button(root, text = 'Klik Aku', command=on_button_click)
button.pack(pady=10)

root.mainloop()