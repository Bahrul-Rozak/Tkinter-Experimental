import tkinter as tk

root = tk.Tk()
root.title('Listbox bro')

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack(pady=10)

friends = ['Alice', 'Bob', 'Charlie','David', 'Eve']
for friend in friends:
       listbox.insert(tk.END, friend)

root.mainloop()