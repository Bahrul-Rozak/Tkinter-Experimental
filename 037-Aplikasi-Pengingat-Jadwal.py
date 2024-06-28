import tkinter as tk
from tkinter import messagebox
import datetime
import threading

root = tk.Tk()
root.title('Reminder Notes')
root.geometry('600x400')

tk.Label(root, text='Masukkan Jadwal (YYYY-MM-DD HH:MM)').pack(pady=10)
entry_jadwal = tk.Entry(root, width=30)
entry_jadwal.pack(pady=5)

tk.Label(root, text='Deskripsi Jadwal').pack(pady=10)
entry_deskripsi = tk.Entry(root, width=30)
entry_deskripsi.pack(pady=5)


jadwal_list = []

def tambah_jadwal():
       jadwal_str = entry_jadwal.get()
       deskripsi = entry_deskripsi.get()

       try:
              jadwal = datetime.datetime.strptime(jadwal_str, "%Y-%m-%d %H:5M")
              jadwal_list.append((jadwal, deskripsi))
              messagebox.showinfo('Sukses', 'Jadwal Berhasil Ditambahkan')
              entry_jadwal.delete(0, tk.END)
              entry_deskripsi.delete(0, tk.END)
       except ValueError:
              messagebox.showerror('Error', 'Format Tanggal dan Waktu tidak valid')

btn_add = tk.Button(root, text='Tambah Jadwal', command=tambah_jadwal).pack(pady=20)

def check_jadwal():
       while True:
              now_data = datetime.datetime.now()
              for jadwal, deskripsi in jadwal_list:
                     if now_data >= jadwal:
                            messagebox.showinfo('Peringatan Jadwal', f"Waktunya untuk {deskripsi}")
                            jadwal_list.remove((jadwal, deskripsi))
              root.after(1000, check_jadwal)

thread = threading.Thread(target=check_jadwal)
thread.daemon = True
thread.start()



root.mainloop()