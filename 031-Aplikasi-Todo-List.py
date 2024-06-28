import tkinter as tk

root = tk.Tk()
root.title('Todo App')
root.geometry('400x400')

entry_task = tk.Entry(root, width=30)
entry_task.pack(pady = 10)

def add_task():
       task = entry_task.get()
       if task != '':
              listbox_tasks.insert(tk.END, task)
              entry_task.delete(0, tk.END)

def delete_task():
       try:
              selected_task_index = listbox_tasks.curselection()[0]
              listbox_tasks.delete(selected_task_index)

       except IndexError:
              pass

button_add = tk.Button(root, text='Add Task', command=add_task)
button_add.pack(pady = 5)

listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)

button_delete = tk.Button(root, text='Delete Task', command=delete_task)
button_delete.pack(pady=5)
root.mainloop()