import tkinter as tk
from tkinter import messagebox
import json
import os

def save_preferences(preferences):
       with open('preferences.json', 'w') as f:
              json.dump(preferences, f)

def load_preferences():
       if os.path.exists('preferences.json'):
              with open('preferences.json', 'r') as f:
                     return json.load(f)
              
       return {}

root = tk.Tk()
preferences = load_preferences()
theme = preferences.get('theme', 'light')
window_size = preferences.get('window_size', '600x300')

if theme == 'dark':
       root.configure(bg='black')
else:
       root.configure(bg='white')

root.geometry(window_size)

def toggle_theme():
       global theme
       if theme == 'light':
              theme = 'dark'
              root.configure(bg='dark')
       else:
              theme == 'light'
              root.configure(bg='white')
       preferences['theme'] = theme
       save_preferences(preferences)

theme_button = tk.Button(root, text='Ubah Tema', command=toggle_theme)
theme_button.pack(pady=20)

def on_closing():
       preferences['window_size'] = root.geometry()
       save_preferences(preferences)
       root.destroy()

root.mainloop()