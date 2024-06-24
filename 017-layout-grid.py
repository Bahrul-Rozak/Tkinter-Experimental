import tkinter as tk

def main():
       root = tk.Tk()
       root.title('Grid')

       label1= tk.Label(root, text = 'Label 1', bg='red', fg='white')
       label2= tk.Label(root, text = 'Label 2', bg='green', fg='white')
       label3= tk.Label(root, text = 'Label 3', bg='blue', fg='white')
       label4= tk.Label(root, text = 'Label 4', bg='yellow', fg='white')

       label1.grid(row=0, column=0, padx=10, pady=10)
       label2.grid(row=0, column=1, padx=10, pady=10)
       label3.grid(row=1, column=0, padx=10, pady=10)
       label4.grid(row=1, column=1, padx=10, pady=10)

       root.mainloop()

if __name__ == "__main__":
       main()