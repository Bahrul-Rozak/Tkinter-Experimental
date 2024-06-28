import tkinter as tk
import time

class SplashScreenApp:
       def __init__(self, root):
              self.root = root
              self.root.title('Splash Screen Demo')
              self.root.geometry('400x300')

              self.show_splash_screen()

       def show_splash_screen(self):
              splash_screen = tk.Toplevel(self.root)
              splash_screen.title('Splash Screen')
              splash_screen.geometry('300x200')

              label = tk.Label(splash_screen, text='Selamat Datang')
              label.pack(pady=50)

              self.root.after(3000, splash_screen.destroy)

if __name__ == '__main__':
       root = tk.Tk()
       app = SplashScreenApp(root)
       root.mainloop()