import tkinter as tk

class LabeledEntry(tk.Frame):
       def __init__(self, master=None, label_text="", *args, **kwargs):
              super().__init__(master, *args, **kwargs)

              self.label = tk.Label(self, text=label_text)
              self.label.pack(side=tk.LEFT)

              self.entry = tk.Entry(self)
              self.entry.pack(side=tk.LEFT)

       def get_text(self):
              return self.entry.get()
       
       def set_text(self, text):
              self.entry.delete(0, tk.END)
              self.entry.insert(0, text)

root = tk.Tk()
root.title('custom widget')

labeled_entry = LabeledEntry(root, label_text='Username : ')
labeled_entry.pack(pady=10)

def show_text():
       print(labeled_entry.get_text())

btn = tk.Button(root, text='show text', command=show_text)
btn.pack(pady=10)

root.mainloop()