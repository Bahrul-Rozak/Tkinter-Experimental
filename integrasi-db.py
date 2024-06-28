import tkinter as tk
from tkinter import messagebox
import sqlite3


conn = sqlite3.connect('books.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books(
          id INTEGER PRIMARY KEY,
          title TEXT NOT NULL,
          author TEXT NOT NULL,
          year INTEGER NOT NULL)''')

conn.commit()
conn.close()



def connect():
       conn = sqlite3.connect('books.db')
       c = conn.cursor()
       c.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)')
       conn.commit()
       conn.close()

def add_book():
       conn = sqlite3.connect('books.db')
       c = conn.cursor()
       c.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', (title_text.get(), author_text.get(), year_text.get()))
       conn.commit()
       conn.close()
       view_book()
       messagebox.showinfo('Success', 'Books Added Success')

def view_book():
       conn = sqlite3.connect('books.db')
       c = conn.cursor()
       c.execute('SELECT * FROM books')
       rows = c.fetchall()
       listbox.delete(0, tk.END)
       for row in rows:
              listbox.insert(tk.END, row)
       conn.close()

root = tk.Tk()
root.title('Book Management System')

tk.Label(root, text='Title').grid(row=0, column=0)
title_text = tk.StringVar()
tk.Entry(root, textvariable=title_text).grid(row=0, column=1)


tk.Label(root, text='Author').grid(row=1, column=0)
author_text = tk.StringVar()
tk.Entry(root, textvariable=author_text).grid(row=1, column=1)

tk.Label(root, text='Year').grid(row=2, column=0)
year_text = tk.StringVar()
tk.Entry(root, textvariable=year_text).grid(row=2, column=1)
                 
tk.Button(root, text='Add Book', command=add_book).grid(row=3, column=0, columnspan=2)

listbox = tk.Listbox(root, height=10, width=50)
listbox.grid(row=4, column=0, columnspan=2)

scrollbar = tk.Scrollbar(root)
scrollbar.grid(column=2, row=4)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

view_book()

root.mainloop()


