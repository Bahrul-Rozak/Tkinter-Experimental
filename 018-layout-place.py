import tkinter as tk

def main():
       root = tk.Tk()
       root.title('Place')
       root.geometry('300x200')

       label1= tk.Label(root, text = 'Label 1', bg='red', fg='white')
       label2= tk.Label(root, text = 'Label 2', bg='green', fg='white')
       label3= tk.Label(root, text = 'Label 3', bg='blue', fg='white')
       label4= tk.Label(root, text = 'Label 4', bg='yellow', fg='white')

       label1.place(x=50, y =50)
       label2.place(x=100, y =100)
       label3.place(x=150, y =150)
       label4.place(relx=0.5, rely=0.5, anchor='s')
    

       root.mainloop()

if __name__ == "__main__":
       main()