import tkinter as tk

def main():
       root = tk.Tk()
       root.title('Pack')

       btn1 = tk.Button(root, text = 'Tombol 1')
       btn1.pack(side=tk.TOP, fill=tk.X)

       btn2 = tk.Button(root, text = 'Tombol 2')
       btn2.pack(side=tk.TOP, fill=tk.X)

       btn3 = tk.Button(root, text = 'Tombol 3')
       btn3.pack(side=tk.BOTTOM, fill=tk.X)

       root.mainloop()

if __name__ == "__main__":
       main()