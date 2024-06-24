import tkinter as tk

def update_value(val):
       current_value.set(f'Nilai Saat Ini {scale.get()}')

root = tk.Tk()
root.title('Widget Scale')

current_value = tk.StringVar()
current_value.set(f'Nilai Saat Ini : 0')
label = tk.Label(root,  textvariable=current_value)
label.pack(pady=10)

scale = tk.Scale(root, from_=0,to=100, orient=tk.HORIZONTAL, length=300, tickinterval=10, resolution=1, label='pilih nilai', showvalue=True, command=update_value)
scale.pack(pady=10)

root.mainloop()