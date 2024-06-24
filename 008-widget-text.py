import tkinter as tk
from tkinter import Tk, Text, Scrollbar, Button, END, Frame

def get_text():
       teks = text_widget.get('1.0', END)
       print(teks)

def clear_text():
       text_widget.delete("1.0", END)

root = tk.Tk()
root.title('Widget Text')

text_widget = Text(root, height=10, width=40, bg='light yellow', fg='black', wrap='word')
text_widget.pack()

scrollbar = Scrollbar(root, command=text_widget.yview)
scrollbar.pack(side='right', fill='y')
text_widget.config(yscrollcommand=scrollbar.set)

button_frame = Frame(root)
button_frame.pack()

get_button = Button(button_frame,text='Get Text', command=get_text)
get_button.pack(side='left')

clear_button = Button(button_frame,text='Clear Text', command=clear_text)
clear_button.pack(side='left')

root.mainloop()