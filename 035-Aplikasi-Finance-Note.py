import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Finance Notes')
root.geometry('600x400')

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text='Tanggal').grid(row=0, column=0)
entry_date = tk.Entry(frame_input)
entry_date.grid(row=0, column=1)

tk.Label(frame_input, text='Deskripsi').grid(row=1, column=0)
entry_desc = tk.Entry(frame_input)
entry_desc.grid(row=1, column=1)

tk.Label(frame_input, text='Jumlah').grid(row=2, column=0)
entry_amount = tk.Entry(frame_input)
entry_amount.grid(row=2, column=1)

columns = ('Tanggal', 'Deskripsi', 'Jumlah')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('Tanggal', text='Tanggal')
tree.heading('Deskripsi', text='Deskripsi')
tree.heading('Jumlah', text='Jumlah')
tree.pack(pady=20)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

transations = []

def add_transaction():
       date = entry_date.get()
       desc = entry_desc.get()
       amount = entry_amount.get()

       if date and desc and amount:
              transations.append((date, desc, amount))
              tree.insert("", "end",values=(date, desc, amount))
              entry_date.delete(0, tk.END)
              entry_desc.delete(0, tk.END)
              entry_amount.delete(0, tk.END)

def delete_transaction():
       selected_item = tree.selection()[0]
       tree.delete(selected_item)
       for i, item in enumerate(transations):
              if item == tree.item(selected_item, 'values'):
                     del transations[i]
                     break

btn_add = tk.Button(frame_buttons, text='Tambah Transaksi', command=add_transaction)
btn_add.grid(row=0, column=0, padx=5)

btn_delete = tk.Button(frame_buttons, text='Hapus Transaksi', command=delete_transaction)
btn_delete.grid(row=0, column=1, padx=5)

root.mainloop()