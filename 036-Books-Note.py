import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Books Notes')
root.geometry('600x400')

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text='Judul').grid(row=0, column=0)
entry_judul = tk.Entry(frame_input)
entry_judul.grid(row=0, column=1)

tk.Label(frame_input, text='Penulis').grid(row=1, column=0)
entry_penulis = tk.Entry(frame_input)
entry_penulis.grid(row=1, column=1)

tk.Label(frame_input, text='Tahun Terbit').grid(row=2, column=0)
entry_tahun_terbit = tk.Entry(frame_input)
entry_tahun_terbit.grid(row=2, column=1)

columns = ('Judul', 'Penulis', 'Tahun Terbit')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('Judul', text='Judul')
tree.heading('Penulis', text='Penulis')
tree.heading('Tahun Terbit', text='Tahun Terbit')
tree.pack(pady=20)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

data_buku = []

def add_transaction():
       judul = entry_judul.get()
       penulis = entry_penulis.get()
       tahun = entry_tahun_terbit.get()

       if judul and penulis and tahun:
              data_buku.append((judul, penulis, tahun))
              tree.insert("", "end",values=(judul, penulis, tahun))
              entry_judul.delete(0, tk.END)
              entry_penulis.delete(0, tk.END)
              entry_tahun_terbit.delete(0, tk.END)

def delete_transaction():
       selected_item = tree.selection()[0]
       tree.delete(selected_item)
       for i, item in enumerate(data_buku):
              if item == tree.item(selected_item, 'values'):
                     del data_buku[i]
                     break

btn_add = tk.Button(frame_buttons, text='Tambah Buku', command=add_transaction)
btn_add.grid(row=0, column=0, padx=5)

btn_delete = tk.Button(frame_buttons, text='Hapus Buku', command=delete_transaction)
btn_delete.grid(row=0, column=1, padx=5)

root.mainloop()