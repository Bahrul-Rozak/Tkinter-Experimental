import tkinter as tk

root = tk.Tk()
root.title('Kalkulator App')
root.geometry('500x400')

def button_click(value):
       if value == 'C':
              entry.delete(0, tk.END)
       if value == '=':
              try:
                     result = eval(entry.get())
                     entry.delete(0, tk.END)
                     entry.insert(tk.END, str(result))
              except:
                     entry.delete(0, tk.END)
                     entry.insert(tk.END, 'ERROR')
       else:
              entry.insert(tk.END, value)

entry = tk.Entry(root, width=16, borderwidth=2, relief='solid')
entry.grid(row =0, column=0, columnspan=4)

buttons = [
       '7', '8', '9', '/',
       '4', '5', '6', '*',
       '1', '2', '3', '-',
       '0', '.', '=', '+',
       'C'
]

row_val = 1
col_val = 0

for button in buttons:
       action = lambda x=button: button_click(x)
       tk.Button(root, text=button, width=4, height=2,command=action).grid(row=row_val, column=col_val)
       col_val += 1
       if col_val > 3:
              col_val = 0
              row_val = 1

root.mainloop()