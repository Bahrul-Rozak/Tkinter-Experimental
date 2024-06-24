import tkinter as tk

root = tk.Tk()
root.title('Frame')

frame1 = tk.Frame(root, borderwidth=2, relief='solid')
frame1.pack(side='top', fill='both', expand=True)

label1 = tk.Label(frame1, text='ini adalah frame pertama', padx=10, pady=10)
label1.pack()

frame2 = tk.Frame(root, borderwidth=2, relief='solid')
frame2.pack(side='top', fill='both', expand=True)

label2 = tk.Label(frame2, text='ini adalah frame pertama', padx=10, pady=10)
label2.pack()

root.mainloop()