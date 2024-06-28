import tkinter as tk
from tkinter import filedialog
import pygame

def open_file():
       global music_file
       music_file = filedialog.askopenfilename()
       if music_file:
              play_button.config(state=tk.NORMAL)
              pause_button.config(state=tk.NORMAL)
              stop_button.config(state=tk.NORMAL)

def play_music():
       pygame.mixer.music.load(music_file)
       pygame.mixer.music.play()

def pause_music():
       if pause_button['text'] == 'Pause':
              pygame.mixer.music.pause()
              pause_button['text'] = 'Resume'
       
       else:
              pygame.mixer.unpause()
              pause_button['text'] = 'Pause'

def stop_music():
       pygame.mixer.music.stop()

pygame.init()

root = tk.Tk()
root.title('Music App')

open_button = tk.Button(root, text='Pilih Music', command=open_file)
open_button.pack(pady=10)

play_button = tk.Button(root, text='Play Music', command=play_music, state=tk.DISABLED)
play_button.pack(pady=10)

pause_button = tk.Button(root, text='Pause Music', command=pause_music, state=tk.DISABLED)
pause_button.pack(pady=10)

stop_button = tk.Button(root, text='Stop Music', command=stop_music, state=tk.DISABLED)
stop_button.pack(pady=10)

root.mainloop()