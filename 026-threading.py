import tkinter as tk
import threading
import time

root = tk.Tk()
root.title('Multi Threading')
root.geometry('300x200')

label = tk.Label(root, text = 'Menunggu tugas ......')
label.pack(pady=20)

def hitung_angka(nilai):
       hasil = 0
       for i in range(1, nilai + 1):
              hasil += 1
              time.sleep(1)
       label.config(text = f'Hasil : {hasil}')

def mulai_hitung():
       nilai = 10
       threading.Thread(target=hitung_angka, args=(nilai, )).start()

button = tk.Button(root, text='Mulai Hitung', command=mulai_hitung)
button.pack(pady=10)

root.mainloop()