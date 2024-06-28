import tkinter as tk
from tkinter import messagebox
import hashlib

def validate_input(username, password):
       if not username or not password:
              return False
       if len(password) < 8:
              return False
       return True

def hash_password(password):
       return hashlib.sha256(password.encode()).hexdigest()

def handle_login():
       username = entry_username.get()
       password = entry_password.get()

       if not validate_input(username, password):
              messagebox.showerror('Eror', 'Username atau Password tidaklah valid')
              return
       
       hashed_password = hash_password(password)

       if username == 'user' and hashed_password == hash_password('securepassword'):
              messagebox.showinfo('Success', 'Login Berhasil')
       else:
              messagebox.showerror('Eror', 'Username atau Password salah!')

root = tk.Tk()
root.title('Contoh Secure App')

tk.Label(root, text='Username:').pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text='Password:').pack(pady=5)
entry_password = tk.Entry(root)
entry_password.pack(pady=5)

tk.Button(root, text='login', command=handle_login).pack(pady=20)

root.mainloop()