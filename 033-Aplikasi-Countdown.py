import tkinter as tk
from tkinter import messagebox
import time

root = tk.Tk()
root.title('Countdown App')
root.geometry('300x200')

time_label = tk.Label(root, text='Masukkan Waktu (detik) : ')
time_label.pack()

time_entry = tk.Entry(root)
time_entry.pack()

start_button = tk.Button(root, text='Mulai', command=lambda: start_countdown(int(time_entry.get())))
start_button.pack()

time_display = tk.Label(root, text = '')
time_display.pack()

def start_countdown(seconds):
       for t in range(seconds, -1, -1):
              mins,secs = divmod(t, 60)
              time_format = '{:02d} : {:02d}'.format(mins, secs)
              time_display.config(text=time_format)
              root.update()
              time.sleep(1)
       
       messagebox.showinfo('Waktu Habis!', 'Perhitungan Selesai')

root.mainloop()
