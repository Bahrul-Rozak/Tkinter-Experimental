import tkinter as tk

def update_label():
       label_text.set(entry_text.get())

root = tk.Tk()
root.title('String Var')

entry_text = tk.StringVar()
label_text = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_text)
entry.pack()

label = tk.Label(root, textvariable=label_text)
label.pack()

update_button = tk.Button(root, text='Update', command=update_label)
update_button.pack()

root.mainloop()