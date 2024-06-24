import tkinter as tk

root = tk.Tk()
root.title('Hello World')

label = tk.Label(
       root, 
       text='Hello World',
       font=('Arial', 16),
       bg='yellow',
       fg='blue',
       padx=10,
       pady=10,
       width=20,
       height=2,
       anchor='center'
       )
label.pack()

def on_button_click():
       print('Tombol diklik!')

button = tk.Button(root, text='Klik Saya!', command=on_button_click)
button.pack(pady=20)

root.geometry('400x300+10+150')
root.mainloop()