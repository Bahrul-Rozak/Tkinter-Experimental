import tkinter as tk

root = tk.Tk()
root.title('Widget Entry')

def show_input():
       user_input = entry.get()
       label.config(text=f"Input: {user_input}")

entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text='Tampilkan Input', command=show_input)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()