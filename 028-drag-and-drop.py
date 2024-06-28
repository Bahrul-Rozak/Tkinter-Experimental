import tkinter as tk

class DragDropApp:
       def __init__(self, root):
              self.root = root
              self.root.title('Drag dan Drop APP')

              self.canvas = tk.Canvas(root, width=400, height=400)
              self.canvas.pack()

              self.rect = self.canvas.create_rectangle(50, 50, 100, 100, fill='blue')

              self.canvas.tag_bind(self.rect, '<ButtonPress-1>', self.on_start)
              self.canvas.tag_bind(self.rect, '<B1-Motion>', self.on_drag)
              self.canvas.tag_bind(self.rect, '<ButtonRelease-1>', self.on_drop)

       def on_start(self, event):
              self.start_x = event.x
              self.start_y = event.y

       def on_drag(self,event):
             dx = event.x - self.start_x
             dy = event.y - self.start_y
             self.canvas.move(self.rect, dx,dy)
             self.start_x = event.x
             self.start_y = event.y

       def on_drop(self, event):
              print('Dropped at', event.x ,event.y)

if __name__ == "__main__":
       root = tk.Tk()
       app = DragDropApp(root)
       root.mainloop()